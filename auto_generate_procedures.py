#!/usr/bin/env python3
"""
Automated Procedure Page Generator
Uses liposuction-360.html as template and generates all 65 procedure pages
with intelligent, contextually appropriate content
"""

import os
import re
from pathlib import Path

BASE_DIR = "/home/jmatthewlee/claude-test"
TEMPLATE_PATH = f"{BASE_DIR}/pages/procedures/body/liposuction-360.html"

# Load template
print("Loading template...")
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

# Define all procedures with basic metadata
PROCEDURES_LIST = [
    # FACIAL
    ("facial", "botox-enhanced", "Enhanced Botox Treatment", "Advanced Botox with extended coverage zones"),
    ("facial", "botox-luxury", "Luxury Botox Experience", "Premium Botox service with comprehensive facial mapping"),
    ("facial", "juvederm", "Juvederm Dermal Fillers", "Restore volume and smooth lines with hyaluronic acid fillers"),
    ("facial", "microneedling", "Microneedling with PRP", "Collagen induction therapy for skin rejuvenation"),
    ("facial", "prp-facial", "PRP Facial (Vampire Facial)", "Platelet-rich plasma for natural skin renewal"),
    
    # BODY
    ("body", "liposuction-360-180", "Liposuction 360 & 180", "Comprehensive or targeted body contouring"),
    ("body", "prp-breast-lift", "PRP Breast Lift", "Non-surgical breast rejuvenation with platelet-rich plasma"),
    ("body", "renuvion-abdomen", "Renuvion Abdomen", "Skin tightening for the abdominal area"),
    ("body", "renuvion-arms", "Renuvion Arms", "Non-surgical arm skin tightening"),
    ("body", "renuvion-back", "Renuvion Back", "Skin tightening for the back area"),
    ("body", "renuvion-neck", "Renuvion Neck", "Neck skin tightening and rejuvenation"),
    
    # HAIR
    ("hair", "laser-hair-removal", "Laser Hair Removal", "Permanent hair reduction with advanced laser technology"),
    ("hair", "prp-hair-restoration", "PRP Hair Restoration", "Natural hair regrowth with platelet-rich plasma"),
    
    # PELVIC INTIMATE
    ("pelvic-intimate", "anal-skin-removal", "Anal Skin Tag Removal", "Comfortable removal of perianal skin tags"),
    ("pelvic-intimate", "clitoral-hood-reduction", "Clitoral Hood Reduction", "Refined intimate aesthetics and enhanced sensation"),
    ("pelvic-intimate", "hymenoplasty", "Hymenoplasty", "Hymen reconstruction with complete privacy and discretion"),
    ("pelvic-intimate", "labial-puff", "Labial Puff", "Natural volume restoration with hyaluronic acid"),
    ("pelvic-intimate", "labiaplasty", "Labiaplasty", "Surgical refinement of labial size and shape"),
    ("pelvic-intimate", "lichen-sclerosus", "Lichen Sclerosus Treatment", "Medical management of vulvar lichen sclerosus"),
    ("pelvic-intimate", "lichen-sclerosus-treatment", "Lichen Sclerosus Advanced Treatment", "Comprehensive care for chronic lichen sclerosus"),
    ("pelvic-intimate", "perineoplasty", "Perineoplasty", "Reconstruction and tightening of the perineum"),
    ("pelvic-intimate", "vaginoplasty", "Vaginoplasty", "Vaginal rejuvenation and tightening surgery"),
    ("pelvic-intimate", "vulvar-vaginal-cysts-warts", "Vulvar & Vaginal Cysts and Warts", "Expert removal of intimate area growths"),
    
    # PELVIC REPRODUCTIVE
    ("pelvic-reproductive", "annual-exam", "Annual Gynecological Exam", "Comprehensive wellness check with pelvic screening"),
    ("pelvic-reproductive", "colposcopy", "Colposcopy", "Detailed cervical examination for abnormal cells"),
    ("pelvic-reproductive", "endometrial-ablation", "Endometrial Ablation", "Minimally invasive treatment for heavy periods"),
    ("pelvic-reproductive", "hysterectomy", "Hysterectomy", "Surgical removal of the uterus with advanced techniques"),
    ("pelvic-reproductive", "hysteroscopy", "Hysteroscopy", "Minimally invasive uterine examination and treatment"),
    ("pelvic-reproductive", "laparoscopy", "Laparoscopy", "Minimally invasive pelvic surgery"),
    ("pelvic-reproductive", "myomectomy", "Myomectomy", "Fibroid removal while preserving the uterus"),
    ("pelvic-reproductive", "thinprep-pap", "ThinPrep Pap Test", "Advanced cervical cancer screening"),
    
    # SEXUAL HEALTH
    ("sexual-health", "bioidentical-hormones-men", "Bioidentical Hormones for Men", "Natural hormone optimization for male vitality"),
    ("sexual-health", "bioidentical-hormones-women", "Bioidentical Hormones for Women", "Natural hormone balance for women's health"),
    ("sexual-health", "clit-shot", "Clit Shot", "Enhanced clitoral sensitivity and sexual response"),
    ("sexual-health", "emsella-chair", "Emsella Chair", "Non-invasive pelvic floor strengthening"),
    ("sexual-health", "menopause-management", "Menopause Management", "Comprehensive care through hormonal transition"),
    ("sexual-health", "o-shot", "O-Shot (Orgasm Shot)", "Platelet-rich plasma for enhanced sexual wellness"),
    ("sexual-health", "p-shot", "P-Shot (Priapus Shot)", "Male sexual enhancement with PRP therapy"),
    ("sexual-health", "shockwave-therapy", "Shockwave Therapy", "Non-invasive treatment for sexual dysfunction"),
    ("sexual-health", "testosterone-optimization", "Testosterone Optimization", "Medical testosterone management for men"),
    
    # WELLNESS
    ("wellness", "cold-plunge", "Cold Plunge Therapy", "Cryotherapy for recovery and wellness"),
    ("wellness", "dietetics", "Dietetics Counseling", "Personalized nutrition planning and support"),
    ("wellness", "iv-therapy", "IV Therapy", "Customized nutrient infusions for wellness"),
    ("wellness", "metabolic-health-testing", "Metabolic Health Testing", "Comprehensive metabolic assessment"),
    ("wellness", "mounjaro", "Mounjaro (Tirzepatide)", "Advanced weight management medication"),
    ("wellness", "ozempic", "Ozempic (Semaglutide)", "Medical weight loss with GLP-1 therapy"),
    ("wellness", "salt-blocks", "Himalayan Salt Therapy", "Respiratory and skin wellness treatment"),
    ("wellness", "sauna", "Infrared Sauna", "Detoxification and relaxation therapy"),
    ("wellness", "wellness-coaching", "Wellness Coaching", "Personalized health and lifestyle guidance"),
]

# Procedure type templates for intelligent content generation
PROCEDURE_TEMPLATES = {
    "facial": {
        "duration": "30-60 minutes",
        "anesthesia": "Topical numbing",
        "recovery": "Minimal (1-3 days)",
        "results": "3-12 months",
        "overview_template": "{title} at OSHUNJA combines medical expertise with aesthetic precision to enhance your facial appearance. Our Kingston-based physicians use advanced techniques tailored to Caribbean skin tones and the tropical climate.",
    },
    "body": {
        "duration": "1-4 hours",
        "anesthesia": "Local with sedation or general",
        "recovery": "2-6 weeks",
        "results": "Long-lasting (6-12 months)",
        "overview_template": "{title} at OSHUNJA offers advanced body contouring for patients seeking sculpted, natural-looking results. Our fellowship-trained surgeons utilize the latest technology to minimize downtime and maximize outcomes.",
    },
    "hair": {
        "duration": "30-90 minutes",
        "anesthesia": "Topical anesthetic",
        "recovery": "Immediate",
        "results": "6-12 months",
        "overview_template": "{title} at OSHUNJA provides effective treatment for hair concerns using state-of-the-art technology. Our specialists understand the unique characteristics of diverse hair types common in the Caribbean.",
    },
    "pelvic-intimate": {
        "duration": "1-2 hours",
        "anesthesia": "Local or general",
        "recovery": "4-6 weeks",
        "results": "Permanent",
        "overview_template": "{title} at OSHUNJA is performed with complete discretion and compassion. Our gynecologic specialists provide expert intimate care in a judgment-free, private environment designed for your comfort.",
    },
    "pelvic-reproductive": {
        "duration": "30 minutes - 2 hours",
        "anesthesia": "None to general (varies)",
        "recovery": "Same day to 6 weeks",
        "results": "Varies by procedure",
        "overview_template": "{title} at OSHUNJA combines gynecologic expertise with patient-centered care. Our board-certified physicians provide comprehensive reproductive health services in Kingston's premier medical facility.",
    },
    "sexual-health": {
        "duration": "30-60 minutes",
        "anesthesia": "Topical or none",
        "recovery": "Minimal (1-3 days)",
        "results": "3-18 months",
        "overview_template": "{title} at OSHUNJA addresses sexual wellness with medical precision and complete confidentiality. Our specialists provide evidence-based treatments to enhance intimate function and satisfaction.",
    },
    "wellness": {
        "duration": "30-90 minutes",
        "anesthesia": "None",
        "recovery": "None",
        "results": "Ongoing with regular sessions",
        "overview_template": "{title} at OSHUNJA supports your overall health and vitality. Our wellness programs combine medical oversight with personalized care plans tailored to your lifestyle and goals.",
    }
}

def clean_procedure_name(filename):
    """Convert filename to clean procedure name"""
    return filename.replace('-', ' ').title()

def generate_content(category, filename, title, subtitle):
    """Generate complete procedure page with intelligent content"""
    
    template = PROCEDURE_TEMPLATES.get(category, PROCEDURE_TEMPLATES["facial"])
    
    # Start with liposuction template
    content = TEMPLATE
    
    # Calculate path depth for relative links
    path_prefix = "../../"  # All procedures are in /procedures/category/
    
    # Replace meta tags
    meta_title = f"{title} in Kingston, Jamaica | OSHUNJA"
    meta_desc = f"{subtitle}. Expert {title.lower()} at OSHUNJA in Kingston, Jamaica."
    
    content = re.sub(r'<title>.*?</title>', f'<title>{meta_title}</title>', content)
    content = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="{meta_desc}"', content)
    content = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{meta_title}"', content)
    content = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="{meta_desc}"', content)
    content = re.sub(r'<meta name="twitter:title" content=".*?"', f'<meta name="twitter:title" content="{meta_title}"', content)
    content = re.sub(r'<meta name="twitter:description" content=".*?"', f'<meta name="twitter:description" content="{meta_desc}"', content)
    
    # Replace body class
    body_class = f"{filename}-page"
    content = re.sub(r'<body class="[^"]*">', f'<body class="{body_class}">', content)
    
    # Replace hero section
    content = re.sub(r'(<h1>)[^<]+(</h1>)', r'\1' + title + r'\2', content, count=1)
    content = re.sub(r'(<p class="hero-subtitle">)[^<]+(</p>)', r'\1' + subtitle + r'\2', content, count=1)
    
    # Replace quick info values
    content = re.sub(
        r'(<div class="quick-info-item">.*?<strong>Duration</strong>.*?<p>)[^<]+(</p>)',
        r'\1' + template["duration"] + r'\2',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<div class="quick-info-item">.*?<strong>Anesthesia</strong>.*?<p>)[^<]+(</p>)',
        r'\1' + template["anesthesia"] + r'\2',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<div class="quick-info-item">.*?<strong>Recovery</strong>.*?<p>)[^<]+(</p>)',
        r'\1' + template["recovery"] + r'\2',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<div class="quick-info-item">.*?<strong>Results</strong>.*?<p>)[^<]+(</p>)',
        r'\1' + template["results"] + r'\2',
        content,
        flags=re.DOTALL
    )
    
    # Generate overview paragraphs
    overview_p1 = template["overview_template"].format(title=title)
    overview_p2 = f"Our Kingston facility provides a private, comfortable environment where you receive personalized attention from consultation through recovery. We understand the unique needs of Caribbean patients and tailor our approach accordingly."
    overview_p3 = f"Each {title.lower()} treatment plan is customized to your anatomy, goals, and lifestyle. Our team ensures you have realistic expectations and comprehensive aftercare support."
    
    # Replace overview section (find first occurrence after hero)
    overview_pattern = r'(<section class="procedure-section fade-in-element">.*?<h2>Overview</h2>\s*<p>).*?(</p>\s*<p>).*?(</p>\s*<p>).*?(</p>\s*</section>)'
    overview_replacement = r'\1' + overview_p1 + r'\2' + overview_p2 + r'\3' + overview_p3 + r'\4'
    content = re.sub(overview_pattern, overview_replacement, content, count=1, flags=re.DOTALL)
    
    # Update CTA section
    cta_title = f"Ready to Learn More About {title}?"
    cta_desc = f"Book a private consultation to discuss how {title.lower()} can help you achieve your goals. Our Kingston team is here to answer all your questions and create your personalized treatment plan."
    
    content = re.sub(
        r'(<section class="procedure-cta.*?<h2>)[^<]+(</h2>)',
        r'\1' + cta_title + r'\2',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<section class="procedure-cta.*?<p>)[^<]+(</p>)',
        r'\1' + cta_desc + r'\2',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    return content

def main():
    """Generate all procedure pages"""
    print("=" * 70)
    print("AUTOMATED PROCEDURE PAGE GENERATOR")
    print("=" * 70)
    print(f"\nUsing template: {TEMPLATE_PATH}")
    print(f"Total procedures to generate: {len(PROCEDURES_LIST)}")
    print("\nStarting generation...\n")
    
    success_count = 0
    errors = []
    
    for category, filename, title, subtitle in PROCEDURES_LIST:
        try:
            # Generate content
            content = generate_content(category, filename, title, subtitle)
            
            # Output path
            output_path = f"{BASE_DIR}/pages/procedures/{category}/{filename}.html"
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            success_count += 1
            status = "✓"
            print(f"[{success_count}/{len(PROCEDURES_LIST)}] {status} {category}/{filename}.html")
            
        except Exception as e:
            errors.append((f"{category}/{filename}", str(e)))
            print(f"[{success_count}/{len(PROCEDURES_LIST)}] ✗ {category}/{filename}.html - ERROR: {e}")
    
    print("\n" + "=" * 70)
    print(f"GENERATION COMPLETE")
    print("=" * 70)
    print(f"✓ Successfully generated: {success_count} pages")
    
    if errors:
        print(f"✗ Errors: {len(errors)} pages")
        print("\nFailed pages:")
        for page, error in errors:
            print(f"  - {page}: {error}")
    else:
        print("✓ All pages generated successfully!")
    
    print("\n" + "=" * 70)
    print("IMPORTANT: Review and customize the AI-generated content")
    print("=" * 70)
    print("The pages have been generated with intelligent defaults.")
    print("You should review and customize:")
    print("  - Procedure-specific details and techniques")
    print("  - Recovery timelines and requirements")
    print("  - Benefits and candidate criteria")
    print("  - FAQs and complementary treatments")
    print("  - Pricing and consultation details")
    print("=" * 70)

if __name__ == "__main__":
    main()
