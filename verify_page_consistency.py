#!/usr/bin/env python3
"""
Verification script to check all procedure pages for consistency.
Ensures all content refers to the correct procedure.
"""

import os
import re
from collections import defaultdict

def get_procedure_name_from_filename(filename):
    """Extract procedure name from filename."""
    name = filename.replace('.html', '').replace('-', ' ').title()
    # Special cases
    replacements = {
        'Prp': 'PRP',
        'Iv': 'IV',
        'O Shot': 'O-Shot',
        'P Shot': 'P-Shot',
        'Clit Shot': 'Clit Shot',
        'Thinprep Pap': 'ThinPrep Pap',
        '360 180': '360/180',
    }
    for old, new in replacements.items():
        name = name.replace(old, new)
    return name

def check_page_consistency(filepath):
    """Check a single page for consistency issues."""
    issues = []
    filename = os.path.basename(filepath)
    expected_procedure = get_procedure_name_from_filename(filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check title tag
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1)
            if expected_procedure.lower() not in title.lower():
                # Check for variations
                base_name = expected_procedure.replace('360/180', '360').replace('PRP', '').strip()
                if base_name and base_name.lower() not in title.lower():
                    issues.append(f"Title doesn't mention procedure: '{title}'")
        
        # Check meta description
        meta_desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
        if meta_desc_match:
            meta_desc = meta_desc_match.group(1)
            if expected_procedure.lower() not in meta_desc.lower():
                base_name = expected_procedure.replace('360/180', '360').replace('PRP', '').strip()
                if base_name and base_name.lower() not in meta_desc.lower():
                    issues.append(f"Meta description doesn't mention procedure clearly")
        
        # Check hero title
        hero_title_match = re.search(r'<section class="procedure-hero">.*?<h1>(.*?)</h1>', content, re.DOTALL)
        if hero_title_match:
            hero_title = hero_title_match.group(1)
            if expected_procedure.lower() not in hero_title.lower():
                base_name = expected_procedure.replace('360/180', '360').replace('PRP', '').strip()
                if base_name and base_name.lower() not in hero_title.lower():
                    issues.append(f"Hero title doesn't match: '{hero_title}' vs '{expected_procedure}'")
        
        # Check for common template issues (references to wrong procedures)
        wrong_procedures = [
            'liposuction', 'botox', 'juvederm', 'laser hair', 'prp facial',
            'renuvion', 'o-shot', 'p-shot', 'labiaplasty', 'vaginoplasty',
            'hysterectomy', 'ozempic', 'mounjaro'
        ]
        
        # Get the main content sections
        overview_match = re.search(r'<h2>Overview</h2>(.*?)</section>', content, re.DOTALL)
        if overview_match:
            overview_text = overview_match.group(1).lower()
            
            # Remove expected procedure from check
            check_procedures = [p for p in wrong_procedures if p != expected_procedure.lower().replace('-', ' ')]
            
            for wrong_proc in check_procedures:
                if wrong_proc in overview_text:
                    # Make sure it's not just a mention in proper context
                    context_words = ['combine', 'complement', 'together with', 'along with', 'similar to', 'like']
                    is_context = any(word in overview_text for word in context_words)
                    if not is_context:
                        issues.append(f"Overview mentions '{wrong_proc}' - may be template residue")
        
        # Check CTA section
        cta_match = re.search(r'<section class="procedure-cta.*?<h2>(.*?)</h2>.*?<p>(.*?)</p>', content, re.DOTALL)
        if cta_match:
            cta_heading = cta_match.group(1)
            cta_text = cta_match.group(2)
            
            if expected_procedure.lower() not in cta_heading.lower() and expected_procedure.lower() not in cta_text.lower():
                base_name = expected_procedure.replace('360/180', '360').replace('PRP', '').strip()
                if base_name and base_name.lower() not in cta_heading.lower() and base_name.lower() not in cta_text.lower():
                    issues.append(f"CTA doesn't reference the correct procedure")
        
        return issues
        
    except Exception as e:
        return [f"Error reading file: {e}"]

def main():
    base_dir = '/home/jmatthewlee/claude-test'
    procedures_dir = os.path.join(base_dir, 'pages', 'procedures')
    
    # Find all procedure HTML files
    html_files = []
    for root, dirs, files in os.walk(procedures_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                html_files.append(file_path)
    
    print(f"Checking {len(html_files)} procedure pages for consistency...\n")
    print("="*70)
    
    pages_with_issues = []
    clean_pages = []
    
    for file_path in sorted(html_files):
        rel_path = os.path.relpath(file_path, base_dir)
        filename = os.path.basename(file_path)
        expected_procedure = get_procedure_name_from_filename(filename)
        
        issues = check_page_consistency(file_path)
        
        if issues:
            pages_with_issues.append((rel_path, expected_procedure, issues))
            print(f"⚠️  {rel_path}")
            print(f"    Expected: {expected_procedure}")
            for issue in issues:
                print(f"    - {issue}")
            print()
        else:
            clean_pages.append(rel_path)
    
    print("="*70)
    print(f"\nSummary:")
    print(f"  ✓ Clean pages: {len(clean_pages)}/{len(html_files)}")
    print(f"  ⚠️  Pages with potential issues: {len(pages_with_issues)}/{len(html_files)}")
    
    if pages_with_issues:
        print(f"\n{'='*70}")
        print("Pages needing review:")
        for rel_path, proc, issues in pages_with_issues:
            print(f"  - {rel_path}")
    else:
        print("\n✅ All pages are consistent! No issues found.")

if __name__ == '__main__':
    main()
