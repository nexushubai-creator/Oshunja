#!/usr/bin/env python3
"""
Intelligent content generation for all OSHUNJA procedure pages.
Generates high-quality, SEO/GEO-optimized content for Kingston, Jamaica.
"""

import os
import re
from pathlib import Path

# Import predefined content
from procedure_content_database import PROCEDURES

# Intelligent content templates by category
CATEGORY_TEMPLATES = {
    'sexual-health': {
        'meta_suffix': 'Kingston Jamaica | Sexual Wellness Treatment | OSHUNJA',
        'hero_suffix': 'in Kingston, Jamaica',
        'duration_default': '30-60 minutes',
        'anesthesia_default': 'Local numbing',
        'recovery_default': '1-3 days',
        'results_default': '6-12 months',
        'overview_template': [
            '{procedure} at OSHUNJA offers advanced sexual wellness treatments in Kingston, Jamaica. Our experienced medical team provides discreet, professional care in a private, comfortable setting designed specifically for intimate health concerns.',
            'Sexual wellness is an important aspect of overall health and quality of life. Our Kingston clinic combines medical expertise with compassionate care to address concerns that many find difficult to discuss elsewhere.',
            'Each treatment is personalized to your unique anatomy and goals. We prioritize your comfort, privacy, and satisfaction throughout the entire process from consultation through follow-up care.'
        ]
    },
    'pelvic-intimate': {
        'meta_suffix': 'Kingston Jamaica | Intimate Surgery | OSHUNJA',
        'hero_suffix': 'in Kingston, Jamaica',
        'duration_default': '1-2 hours',
        'anesthesia_default': 'Local or general',
        'recovery_default': '2-4 weeks',
        'results_default': 'Permanent',
        'overview_template': [
            '{procedure} at OSHUNJA provides expert cosmetic gynecology in Kingston, Jamaica. Our board-certified surgeon specializes in intimate procedures that enhance comfort, confidence, and quality of life with natural-looking results.',
            'Many women in Kingston seek intimate procedures to address functional concerns, aesthetic preferences, or post-childbirth changes. We provide judgment-free, compassionate care in a private, luxurious setting.',
            'Your consultation includes a thorough examination, discussion of your goals, and creation of a personalized surgical plan. We ensure you feel comfortable and informed every step of the way.'
        ]
    },
    'pelvic-reproductive': {
        'meta_suffix': 'Kingston Jamaica | Gynecological Care | OSHUNJA',
        'hero_suffix': 'in Kingston, Jamaica',
        'duration_default': '30-90 minutes',
        'anesthesia_default': 'Local or conscious sedation',
        'recovery_default': '1-7 days',
        'results_default': 'Varies by procedure',
        'overview_template': [
            '{procedure} at OSHUNJA provides comprehensive gynecological care in Kingston, Jamaica. Our experienced physicians offer advanced diagnostic and treatment procedures in a comfortable, modern facility.',
            'Women\'s health is our specialty. We combine clinical excellence with personalized care to address your gynecological concerns with the latest evidence-based techniques.',
            'From routine screenings to advanced procedures, we provide the full spectrum of gynecological care. Our Kingston team ensures you receive thorough, compassionate treatment at every visit.'
        ]
    },
    'wellness': {
        'meta_suffix': 'Kingston Jamaica | Wellness Services | OSHUNJA',
        'hero_suffix': 'in Kingston, Jamaica',
        'duration_default': '30-60 minutes',
        'anesthesia_default': 'Not required',
        'recovery_default': 'Immediate',
        'results_default': 'Ongoing',
        'overview_template': [
            '{procedure} at OSHUNJA supports your whole-body wellness goals in Kingston, Jamaica. Our comprehensive wellness services combine medical expertise with holistic approaches to help you achieve optimal health and vitality.',
            'Kingston\'s vibrant lifestyle deserves wellness support that matches your ambitions. We provide personalized programs designed to enhance your energy, appearance, and overall quality of life.',
            'Each wellness plan is customized to your unique needs, goals, and lifestyle. Our team provides ongoing support and guidance to ensure you achieve and maintain the results you desire.'
        ]
    }
}

def format_procedure_name(filename):
    """Convert filename to readable procedure name."""
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
        '360': '360'
    }
    for old, new in replacements.items():
        name = name.replace(old, new)
    return name

def get_category_from_path(filepath):
    """Extract category from file path."""
    parts = filepath.split(os.sep)
    if 'sexual-health' in parts:
        return 'sexual-health'
    elif 'pelvic-intimate' in parts:
        return 'pelvic-intimate'
    elif 'pelvic-reproductive' in parts:
        return 'pelvic-reproductive'
    elif 'wellness' in parts:
        return 'wellness'
    elif 'facial' in parts:
        return 'facial'
    elif 'hair' in parts:
        return 'hair'
    elif 'body' in parts:
        return 'body'
    return 'general'

def generate_intelligent_content(filename, filepath):
    """Generate intelligent content for any procedure."""
    # Check if we have predefined content
    if filename in PROCEDURES:
        return PROCEDURES[filename]
    
    # Generate intelligent content based on category and name
    procedure_name = format_procedure_name(filename)
    category = get_category_from_path(filepath)
    
    # Get category template or use defaults
    template = CATEGORY_TEMPLATES.get(category, {
        'meta_suffix': 'Kingston Jamaica | OSHUNJA',
        'hero_suffix': 'in Kingston, Jamaica',
        'duration_default': '30-90 minutes',
        'anesthesia_default': 'As needed',
        'recovery_default': '1-7 days',
        'results_default': 'Varies',
        'overview_template': [
            f'{procedure_name} at OSHUNJA provides expert medical care in Kingston, Jamaica.',
            'Our experienced medical team combines advanced techniques with personalized attention.',
            'Each treatment is customized to your unique needs and goals for optimal results.'
        ]
    })
    
    # Generate content
    content = {
        'category': category,
        'title': procedure_name,
        'meta_title': f'{procedure_name} {template["meta_suffix"]}',
        'meta_description': f'Professional {procedure_name} services in Kingston, Jamaica. Expert medical care with personalized treatment plans at OSHUNJA.',
        'og_title': f'{procedure_name} Kingston Jamaica | OSHUNJA',
        'og_description': f'Expert {procedure_name} treatment in Kingston, Jamaica. Personalized care and advanced techniques.',
        'hero_title': procedure_name,
        'hero_subtitle': f'Expert {procedure_name.lower()} treatment {template["hero_suffix"]}',
        'duration': template['duration_default'],
        'anesthesia': template['anesthesia_default'],
        'recovery': template['recovery_default'],
        'results': template['results_default'],
        'overview': [t.format(procedure=procedure_name) for t in template['overview_template']],
        'cta_heading': f'Ready to Learn More About {procedure_name}?',
        'cta_text': f'Book a consultation with OSHUNJA in Kingston to discover how {procedure_name.lower()} can help you achieve your goals. We\'ll create a personalized treatment plan designed specifically for your needs.'
    }
    
    return content

def update_procedure_page(filepath, content, home_path):
    """Update a procedure page with new content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Update meta title
        html = re.sub(
            r'<title>.*?</title>',
            f'<title>{content["meta_title"]}</title>',
            html,
            flags=re.DOTALL
        )
        
        # Update meta description
        html = re.sub(
            r'<meta name="description" content=".*?">',
            f'<meta name="description" content="{content["meta_description"]}">',
            html
        )
        
        # Update Open Graph title
        html = re.sub(
            r'<meta property="og:title" content=".*?">',
            f'<meta property="og:title" content="{content["og_title"]}">',
            html
        )
        
        # Update Open Graph description
        html = re.sub(
            r'<meta property="og:description" content=".*?">',
            f'<meta property="og:description" content="{content["og_description"]}">',
            html
        )
        
        # Update Twitter card title
        html = re.sub(
            r'<meta name="twitter:title" content=".*?">',
            f'<meta name="twitter:title" content="{content["og_title"]}">',
            html
        )
        
        # Update Twitter card description
        html = re.sub(
            r'<meta name="twitter:description" content=".*?">',
            f'<meta name="twitter:description" content="{content["og_description"]}">',
            html
        )
        
        # Update hero title
        def replace_hero_title(match):
            return match.group(1) + content["hero_title"] + match.group(2)
        html = re.sub(
            r'(<section class="procedure-hero">.*?<h1>).*?(</h1>)',
            replace_hero_title,
            html,
            flags=re.DOTALL
        )
        
        # Update hero subtitle
        def replace_hero_subtitle(match):
            return match.group(1) + content["hero_subtitle"] + match.group(2)
        html = re.sub(
            r'(<p class="hero-subtitle">).*?(</p>)',
            replace_hero_subtitle,
            html,
            flags=re.DOTALL
        )
        
        # Update quick info - duration
        def replace_duration(match):
            return match.group(1) + content["duration"] + match.group(2)
        html = re.sub(
            r'(<div class="quick-info-item">.*?<strong>Duration</strong>.*?<p>).*?(</p>)',
            replace_duration,
            html,
            flags=re.DOTALL
        )
        
        # Update quick info - anesthesia
        def replace_anesthesia(match):
            return match.group(1) + content["anesthesia"] + match.group(2)
        html = re.sub(
            r'(<div class="quick-info-item">.*?<strong>Anesthesia</strong>.*?<p>).*?(</p>)',
            replace_anesthesia,
            html,
            flags=re.DOTALL
        )
        
        # Update quick info - recovery
        def replace_recovery(match):
            return match.group(1) + content["recovery"] + match.group(2)
        html = re.sub(
            r'(<div class="quick-info-item">.*?<strong>Recovery</strong>.*?<p>).*?(</p>)',
            replace_recovery,
            html,
            flags=re.DOTALL
        )
        
        # Update quick info - results
        def replace_results(match):
            return match.group(1) + content["results"] + match.group(2)
        html = re.sub(
            r'(<div class="quick-info-item">.*?<strong>Results</strong>.*?<p>).*?(</p>)',
            replace_results,
            html,
            flags=re.DOTALL
        )
        
        # Update overview section
        overview_html = '\n'.join([f'                <p>{p}</p>' for p in content['overview']])
        def replace_overview(match):
            return match.group(1) + '\n' + overview_html + '\n            ' + match.group(3)
        html = re.sub(
            r'(<section class="procedure-section fade-in-element">.*?<h2>Overview</h2>)(.*?)(</section>)',
            replace_overview,
            html,
            flags=re.DOTALL
        )
        
        # Update CTA heading
        def replace_cta_heading(match):
            return match.group(1) + content["cta_heading"] + match.group(2)
        html = re.sub(
            r'(<section class="procedure-cta fade-in-element">.*?<h2>).*?(</h2>)',
            replace_cta_heading,
            html,
            flags=re.DOTALL
        )
        
        # Update CTA text
        def replace_cta_text(match):
            return match.group(1) + content["cta_text"] + match.group(2)
        html = re.sub(
            r'(<section class="procedure-cta fade-in-element">.*?<h2>.*?</h2>.*?<p>).*?(</p>)',
            replace_cta_text,
            html,
            flags=re.DOTALL
        )
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def calculate_relative_path(file_path, base_dir):
    """Calculate relative path from file to base directory."""
    file_dir = os.path.dirname(file_path)
    rel_path = os.path.relpath(base_dir, file_dir)
    if rel_path == '.':
        return ''
    return rel_path + '/'

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
    
    print(f"Found {len(html_files)} procedure pages to update with SEO/GEO content\n")
    print("="*70)
    
    success_count = 0
    for file_path in html_files:
        try:
            filename = os.path.basename(file_path)
            
            # Generate or retrieve content
            content = generate_intelligent_content(filename, file_path)
            
            # Calculate relative path
            home_path = calculate_relative_path(file_path, base_dir)
            
            # Update page
            if update_procedure_page(file_path, content, home_path):
                rel_path = os.path.relpath(file_path, base_dir)
                status = "✓ [PRE-DEFINED]" if filename in PROCEDURES else "✓ [GENERATED]"
                print(f"{status} {rel_path}")
                print(f"   Title: {content['title']}")
                print(f"   Category: {content['category']}")
                print()
                success_count += 1
        except Exception as e:
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"✗ Failed: {rel_path} - {e}\n")
    
    print("="*70)
    print(f"Successfully updated {success_count}/{len(html_files)} files")
    print("="*70)
    print("\nNote: [PRE-DEFINED] = Custom SEO content from database")
    print("      [GENERATED] = Intelligent auto-generated content")
    print("\nAll pages now have Kingston, Jamaica SEO/GEO optimization!")

if __name__ == '__main__':
    main()
