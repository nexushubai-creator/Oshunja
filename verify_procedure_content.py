#!/usr/bin/env python3
"""
Comprehensive verification script to ensure all procedure pages contain
procedure-specific content that actually matches the procedure name.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def extract_procedure_name_from_path(file_path: str) -> str:
    """Extract the procedure name from the file path"""
    return Path(file_path).stem

def extract_page_title(content: str) -> str:
    """Extract the H1 title from the page"""
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content, re.IGNORECASE)
    return title_match.group(1).strip() if title_match else "NO TITLE FOUND"

def extract_hero_subtitle(content: str) -> str:
    """Extract the hero subtitle"""
    subtitle_match = re.search(r'<p class="hero-subtitle"[^>]*>([^<]+)</p>', content, re.IGNORECASE)
    return subtitle_match.group(1).strip() if subtitle_match else "NO SUBTITLE FOUND"

def extract_benefits_section(content: str) -> str:
    """Extract the benefits section content"""
    benefits_match = re.search(r'<h2>Benefits & Results</h2>\s*<p>([^<]+)', content, re.IGNORECASE | re.DOTALL)
    return benefits_match.group(1).strip() if benefits_match else "NO BENEFITS SECTION FOUND"

def extract_candidates_section(content: str) -> str:
    """Extract the candidates section content"""
    candidates_match = re.search(r'<h2>Ideal Candidates & Considerations</h2>\s*<p>([^<]+)', content, re.IGNORECASE | re.DOTALL)
    return candidates_match.group(1).strip() if candidates_match else "NO CANDIDATES SECTION FOUND"

def check_for_generic_content(content: str) -> List[str]:
    """Check for any remaining generic content patterns"""
    generic_patterns = [
        r"This procedure provides",
        r"Good candidates for this procedure",
        r"specific concerns related to this treatment area",
        r"This procedure can be combined with other treatments for comprehensive results",
        r"meaningful benefits for your health and wellness goals",
        r"Our Kingston team will discuss",
        r"During your consultation, we'll discuss complementary options that align with your goals"
    ]
    
    found_generic = []
    for pattern in generic_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found_generic.append(pattern)
    
    return found_generic

def verify_procedure_specific_content(file_path: str, procedure_name: str) -> Dict:
    """Verify that a procedure page contains procedure-specific content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract key sections
        title = extract_page_title(content)
        subtitle = extract_hero_subtitle(content)
        benefits = extract_benefits_section(content)
        candidates = extract_candidates_section(content)
        
        # Check for generic content
        generic_issues = check_for_generic_content(content)
        
        # Check if procedure name appears in key sections
        procedure_terms = procedure_name.replace('-', ' ').lower()
        procedure_variations = [
            procedure_name.replace('-', ' '),
            procedure_name.replace('-', ''),
            procedure_name.title().replace('-', ' '),
            procedure_name.upper().replace('-', ' ')
        ]
        
        title_matches = any(term.lower() in title.lower() for term in procedure_variations)
        subtitle_matches = any(term.lower() in subtitle.lower() for term in procedure_variations)
        benefits_specific = len(benefits) > 50 and not any(generic in benefits for generic in ["This procedure", "meaningful benefits"])
        candidates_specific = len(candidates) > 50 and not any(generic in candidates for generic in ["Good candidates for this procedure"])
        
        return {
            'file': procedure_name,
            'title': title,
            'subtitle': subtitle,
            'title_matches': title_matches,
            'subtitle_matches': subtitle_matches,
            'benefits_length': len(benefits),
            'benefits_specific': benefits_specific,
            'benefits_preview': benefits[:100] + "..." if len(benefits) > 100 else benefits,
            'candidates_length': len(candidates),
            'candidates_specific': candidates_specific,
            'candidates_preview': candidates[:100] + "..." if len(candidates) > 100 else candidates,
            'generic_issues': generic_issues,
            'overall_status': (
                title_matches and 
                subtitle_matches and 
                benefits_specific and 
                candidates_specific and 
                len(generic_issues) == 0
            )
        }
        
    except Exception as e:
        return {
            'file': procedure_name,
            'error': str(e),
            'overall_status': False
        }

def main():
    """Main verification function"""
    base_dir = Path("pages/procedures")
    html_files = list(base_dir.rglob("*.html"))
    
    print(f"🔍 COMPREHENSIVE PROCEDURE CONTENT VERIFICATION")
    print(f"=" * 60)
    print(f"Checking {len(html_files)} procedure pages...\n")
    
    results = []
    issues_found = 0
    
    for file_path in html_files:
        procedure_name = extract_procedure_name_from_path(str(file_path))
        result = verify_procedure_specific_content(str(file_path), procedure_name)
        results.append(result)
        
        if not result['overall_status']:
            issues_found += 1
    
    # Print summary
    print(f"📊 VERIFICATION SUMMARY")
    print(f"=" * 40)
    print(f"Total files checked: {len(results)}")
    print(f"✅ Passing: {len(results) - issues_found}")
    print(f"❌ Issues found: {issues_found}")
    print()
    
    # Print detailed results for pages with issues
    if issues_found > 0:
        print(f"🚨 PAGES WITH ISSUES:")
        print(f"=" * 40)
        
        for result in results:
            if not result.get('overall_status', False):
                print(f"\n❌ {result['file']}.html")
                
                if 'error' in result:
                    print(f"   Error: {result['error']}")
                    continue
                
                print(f"   Title: {result['title']}")
                print(f"   Title matches procedure: {'✅' if result['title_matches'] else '❌'}")
                print(f"   Subtitle matches procedure: {'✅' if result['subtitle_matches'] else '❌'}")
                print(f"   Benefits section length: {result['benefits_length']} chars")
                print(f"   Benefits specific: {'✅' if result['benefits_specific'] else '❌'}")
                print(f"   Candidates section length: {result['candidates_length']} chars")
                print(f"   Candidates specific: {'✅' if result['candidates_specific'] else '❌'}")
                
                if result['generic_issues']:
                    print(f"   Generic content found: {', '.join(result['generic_issues'])}")
                
                print(f"   Benefits preview: {result['benefits_preview']}")
                print(f"   Candidates preview: {result['candidates_preview']}")
    
    # Print sample of good pages
    good_pages = [r for r in results if r.get('overall_status', False)]
    if good_pages:
        print(f"\n✅ SAMPLE OF PROPERLY UPDATED PAGES:")
        print(f"=" * 40)
        
        for result in good_pages[:5]:  # Show first 5 good pages
            print(f"\n✅ {result['file']}.html")
            print(f"   Title: {result['title']}")
            print(f"   Benefits: {result['benefits_preview']}")
    
    print(f"\n{'='*60}")
    if issues_found == 0:
        print(f"🎉 ALL PAGES VERIFIED - PROCEDURE-SPECIFIC CONTENT CONFIRMED!")
        print(f"✅ All {len(results)} procedure pages contain proper procedure-specific content.")
    else:
        print(f"⚠️  {issues_found} pages need attention to ensure procedure-specific content.")
    
    return issues_found == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)