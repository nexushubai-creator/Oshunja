#!/usr/bin/env python3
"""
Removes template contamination from all procedure pages.
Specifically targets sections that weren't updated in the initial content generation.
"""

import os
import re

def clean_page(filepath):
    """Remove template contamination from a page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        filename = os.path.basename(filepath)
        
        # Skip files that should have detailed content
        skip_files = [
            'liposuction-360-180.html', 'liposuction-360.html',
            'botox.html', 'juvederm.html', 'microneedling.html', 'prp-facial.html',
            'laser-hair-removal.html', 'prp-hair-restoration.html',
            'prp-breast-lift.html', 'renuvion-abdomen.html', 'renuvion-back.html',
            'renuvion-neck.html', 'renuvion-arms.html'
        ]
        
        if filename in skip_files:
            return False, "Skipped - has custom content"
        
        # Remove specific liposuction contamination patterns
        liposuction_phrases = [
            r'360-degree treatment addresses all angles of your torso',
            r'Many patients combine Liposuction 360',
            r'How soon can I travel after liposuction 360',
            r'Is liposuction 360 painful',
            r'How much does liposuction 360 cost',
            r'Circumferential Liposuction',
            r'Liposuction 360 treats the abdomen',
            r'snatched silhouette',
            r'power-assisted cannulas',
            r'compression garment',
            r'lymphatic drainage',
            r'torso in one surgical session',
            r'flanks, and back',
            r'abdomen, waist, flanks',
        ]
        
        # Find and remove contaminated sections
        # Remove "How It Works" section if it contains liposuction content
        how_it_works_pattern = r'(<section id="how-it-works".*?<h2>How It Works.*?</h2>)(.*?)(</section>)'
        match = re.search(how_it_works_pattern, content, re.DOTALL)
        if match:
            section_content = match.group(2)
            if any(re.search(phrase, section_content, re.IGNORECASE) for phrase in liposuction_phrases):
                # Replace with generic content
                new_section = '''
                <p>During your consultation at OSHUNJA in Kingston, our medical team will explain the procedure steps, answer your questions, and create a personalized treatment plan tailored to your unique needs and goals.</p>
                <p>The treatment process is designed for your comfort and privacy. We ensure you understand what to expect before, during, and after your procedure.</p>
            '''
                content = content.replace(match.group(0), match.group(1) + new_section + match.group(3))
        
        # Remove "Candidates" section if contaminated
        candidates_pattern = r'(<section.*?<h2>Ideal Candidates.*?</h2>)(.*?)(</section>)'
        match = re.search(candidates_pattern, content, re.DOTALL)
        if match:
            section_content = match.group(2)
            if any(re.search(phrase, section_content, re.IGNORECASE) for phrase in liposuction_phrases):
                new_section = '''
                <p>Good candidates for this procedure are in good overall health, have realistic expectations, and are seeking to address specific concerns related to this treatment area.</p>
                <p>During your consultation in Kingston, we'll evaluate your medical history, discuss your goals, and determine if this procedure is right for you.</p>
            '''
                content = content.replace(match.group(0), match.group(1) + new_section + match.group(3))
        
        # Remove "Recovery" section if contaminated
        recovery_pattern = r'(<section.*?<h2>Recovery & Aftercare</h2>)(.*?)(</section>)'
        match = re.search(recovery_pattern, content, re.DOTALL)
        if match:
            section_content = match.group(2)
            if any(re.search(phrase, section_content, re.IGNORECASE) for phrase in liposuction_phrases):
                new_section = '''
                <p>Recovery varies by procedure and individual. Our Kingston team provides detailed aftercare instructions and is available for any questions or concerns during your recovery period.</p>
                <p>We schedule follow-up appointments to monitor your progress and ensure optimal results.</p>
            '''
                content = content.replace(match.group(0), match.group(1) + new_section + match.group(3))
        
        # Remove "Complementary Treatments" section if contaminated
        complementary_pattern = r'(<section.*?<h2>Complementary Treatments.*?</h2>)(.*?)(</section>)'
        match = re.search(complementary_pattern, content, re.DOTALL)
        if match:
            section_content = match.group(2)
            if any(re.search(phrase, section_content, re.IGNORECASE) for phrase in liposuction_phrases):
                new_section = '''
                <p>This procedure can be combined with other treatments for comprehensive results. During your consultation, we'll discuss complementary options that align with your goals.</p>
            '''
                content = content.replace(match.group(0), match.group(1) + new_section + match.group(3))
        
        # Clean FAQs section
        faq_pattern = r'<details class="faq-item.*?<summary>(.*?)</summary>.*?<p>(.*?)</p>.*?</details>'
        faqs = re.findall(faq_pattern, content, re.DOTALL)
        for question, answer in faqs:
            if any(re.search(phrase, question + answer, re.IGNORECASE) for phrase in liposuction_phrases):
                # Remove this specific FAQ
                faq_full_pattern = r'<details class="faq-item.*?<summary>' + re.escape(question) + r'</summary>.*?</details>'
                content = re.sub(faq_full_pattern, '', content, flags=re.DOTALL)
        
        # Clean structured data
        structured_data_pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
        match = re.search(structured_data_pattern, content, re.DOTALL)
        if match:
            json_content = match.group(2)
            if any(re.search(phrase, json_content, re.IGNORECASE) for phrase in liposuction_phrases):
                # Get procedure name from filename
                procedure_name = filename.replace('.html', '').replace('-', ' ').title()
                replacements = {
                    'Prp': 'PRP', 'Iv': 'IV', 'O Shot': 'O-Shot', 'P Shot': 'P-Shot'
                }
                for old, new in replacements.items():
                    procedure_name = procedure_name.replace(old, new)
                
                # Simple generic structured data
                new_json = f'''
    {{
      "@context": "https://schema.org",
      "@type": "MedicalProcedure",
      "name": "{procedure_name}",
      "description": "{procedure_name} at OSHUNJA in Kingston, Jamaica. Expert medical care with personalized treatment plans.",
      "medicalSpecialty": "PlasticSurgery",
      "areaServed": {{
        "@type": "City",
        "name": "Kingston",
        "containedIn": "Jamaica"
      }}
    }}
    '''
                content = content.replace(match.group(0), match.group(1) + new_json + match.group(3))
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Cleaned contamination"
        else:
            return False, "No contamination found"
            
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
    
    print(f"Cleaning {len(html_files)} procedure pages...\n")
    print("="*70)
    
    cleaned_count = 0
    skipped_count = 0
    clean_count = 0
    
    for file_path in sorted(html_files):
        rel_path = os.path.relpath(file_path, base_dir)
        
        was_cleaned, message = clean_page(file_path)
        
        if "Skipped" in message:
            skipped_count += 1
            print(f"⊘  {rel_path} - {message}")
        elif was_cleaned:
            cleaned_count += 1
            print(f"✓  {rel_path} - {message}")
        else:
            clean_count += 1
            print(f"○  {rel_path} - {message}")
    
    print("="*70)
    print(f"\nSummary:")
    print(f"  ✓ Pages cleaned: {cleaned_count}")
    print(f"  ○ Already clean: {clean_count}")
    print(f"  ⊘ Skipped (custom content): {skipped_count}")
    print(f"  Total: {len(html_files)}")
    print("\n✅ All pages checked and cleaned!")

if __name__ == '__main__':
    main()
