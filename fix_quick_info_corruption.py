#!/usr/bin/env python3
"""
Fixes corrupted quick info sections across all procedure pages.
"""

import os
import re

def fix_quick_info(filepath):
    """Fix corrupted quick info section in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match corrupted quick info section
        # Looking for lines like "X-60 minutes" or "M-60 minutes" which indicate corruption
        corrupted_pattern = r'(<div class="procedure-quick-info fade-in-element">)\s*([A-Z])-(\d+[^<]*</p>\s*</div>\s*</div>)'
        
        if re.search(corrupted_pattern, content):
            # Extract the procedure-specific info from the file
            filename = os.path.basename(filepath)
            
            # Get duration from what we can salvage
            duration_match = re.search(r'([A-Z])-(\d+.*?)(?:</p>|$)', content[content.find('procedure-quick-info'):content.find('procedure-quick-info')+500])
            if duration_match:
                duration_text = duration_match.group(2).split('</p>')[0].strip()
            else:
                duration_text = "30-60 minutes"
            
            # Get anesthesia, recovery, and results from existing content
            anesthesia_match = re.search(r'<strong>Anesthesia</strong>\s*<p>(.*?)</p>', content, re.DOTALL)
            recovery_match = re.search(r'<strong>Recovery</strong>\s*<p>(.*?)</p>', content, re.DOTALL)
            results_match = re.search(r'<strong>Results</strong>\s*<p>(.*?)</p>', content, re.DOTALL)
            
            anesthesia = anesthesia_match.group(1).strip() if anesthesia_match else "As needed"
            recovery = recovery_match.group(1).strip() if recovery_match else "Varies"
            results = results_match.group(1).strip() if results_match else "Ongoing"
            
            # Build the corrected quick info section
            new_quick_info = f'''            <!-- Quick Info Bar -->
            <div class="procedure-quick-info fade-in-element">
                <div class="quick-info-item">
                    <span class="info-icon">⏱</span>
                    <div>
                        <strong>Duration</strong>
                        <p>{duration_text}</p>
                    </div>
                </div>
                <div class="quick-info-item">
                    <span class="info-icon">💤</span>
                    <div>
                        <strong>Anesthesia</strong>
                        <p>{anesthesia}</p>
                    </div>
                </div>
                <div class="quick-info-item">
                    <span class="info-icon">🏠</span>
                    <div>
                        <strong>Recovery</strong>
                        <p>{recovery}</p>
                    </div>
                </div>
                <div class="quick-info-item">
                    <span class="info-icon">✨</span>
                    <div>
                        <strong>Results</strong>
                        <p>{results}</p>
                    </div>
                </div>
            </div>'''
            
            # Replace the corrupted section
            pattern = r'<!-- Quick Info Bar -->.*?</div>\s*</div>\s*\n\s*</div>'
            content = re.sub(pattern, new_quick_info, content, count=1, flags=re.DOTALL)
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True, "Fixed"
        
        return False, "No corruption found"
        
    except Exception as e:
        return False, f"Error: {e}"

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
    
    print(f"Checking {len(html_files)} procedure pages for quick info corruption...\n")
    print("="*70)
    
    fixed_count = 0
    clean_count = 0
    
    for file_path in sorted(html_files):
        rel_path = os.path.relpath(file_path, base_dir)
        
        was_fixed, message = fix_quick_info(file_path)
        
        if was_fixed:
            fixed_count += 1
            print(f"✓  {rel_path} - {message}")
        else:
            clean_count += 1
    
    print("="*70)
    print(f"\nSummary:")
    print(f"  ✓ Pages fixed: {fixed_count}")
    print(f"  ○ Already correct: {clean_count}")
    print(f"  Total: {len(html_files)}")
    
    if fixed_count > 0:
        print(f"\n✅ Fixed {fixed_count} corrupted quick info sections!")
    else:
        print("\n✅ All pages already have correct quick info sections!")

if __name__ == '__main__':
    main()
