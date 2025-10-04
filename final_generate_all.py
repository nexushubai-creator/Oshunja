#!/usr/bin/env python3
"""Complete Automated Procedure Page Generator - Final Version"""
import os

BASE_DIR = "/home/jmatthewlee/claude-test"
TEMPLATE_PATH = f"{BASE_DIR}/pages/procedures/body/liposuction-360.html"

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

# All 49 procedures
PROCEDURES = [
    ("facial", "botox-enhanced", "Enhanced Botox Treatment", "Advanced Botox with extended coverage zones"),
    ("facial", "botox-luxury", "Luxury Botox Experience", "Premium Botox service with comprehensive facial mapping"),
    ("facial", "juvederm", "Juvederm Dermal Fillers", "Restore volume and smooth lines with hyaluronic acid fillers"),
    ("facial", "microneedling", "Microneedling with PRP", "Collagen induction therapy for skin rejuvenation"),
    ("facial", "prp-facial", "PRP Facial (Vampire Facial)", "Platelet-rich plasma for natural skin renewal"),
    ("body", "liposuction-360-180", "Liposuction 360 & 180", "Comprehensive or targeted body contouring"),
    ("body", "prp-breast-lift", "PRP Breast Lift", "Non-surgical breast rejuvenation with platelet-rich plasma"),
    ("body", "renuvion-abdomen", "Renuvion Abdomen", "Skin tightening for the abdominal area"),
    ("body", "renuvion-arms", "Renuvion Arms", "Non-surgical arm skin tightening"),
    ("body", "renuvion-back", "Renuvion Back", "Skin tightening for the back area"),
    ("body", "renuvion-neck", "Renuvion Neck", "Neck skin tightening and rejuvenation"),
    ("hair", "laser-hair-removal", "Laser Hair Removal", "Permanent hair reduction with advanced laser technology"),
    ("hair", "prp-hair-restoration", "PRP Hair Restoration", "Natural hair regrowth with platelet-rich plasma"),
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
    ("pelvic-reproductive", "annual-exam", "Annual Gynecological Exam", "Comprehensive wellness check with pelvic screening"),
    ("pelvic-reproductive", "colposcopy", "Colposcopy", "Detailed cervical examination for abnormal cells"),
    ("pelvic-reproductive", "endometrial-ablation", "Endometrial Ablation", "Minimally invasive treatment for heavy periods"),
    ("pelvic-reproductive", "hysterectomy", "Hysterectomy", "Surgical removal of the uterus with advanced techniques"),
    ("pelvic-reproductive", "hysteroscopy", "Hysteroscopy", "Minimally invasive uterine examination and treatment"),
    ("pelvic-reproductive", "laparoscopy", "Laparoscopy", "Minimally invasive pelvic surgery"),
    ("pelvic-reproductive", "myomectomy", "Myomectomy", "Fibroid removal while preserving the uterus"),
    ("pelvic-reproductive", "thinprep-pap", "ThinPrep Pap Test", "Advanced cervical cancer screening"),
    ("sexual-health", "bioidentical-hormones-men", "Bioidentical Hormones for Men", "Natural hormone optimization for male vitality"),
    ("sexual-health", "bioidentical-hormones-women", "Bioidentical Hormones for Women", "Natural hormone balance for women's health"),
    ("sexual-health", "clit-shot", "Clit Shot", "Enhanced clitoral sensitivity and sexual response"),
    ("sexual-health", "emsella-chair", "Emsella Chair", "Non-invasive pelvic floor strengthening"),
    ("sexual-health", "menopause-management", "Menopause Management", "Comprehensive care through hormonal transition"),
    ("sexual-health", "o-shot", "O-Shot (Orgasm Shot)", "Platelet-rich plasma for enhanced sexual wellness"),
    ("sexual-health", "p-shot", "P-Shot (Priapus Shot)", "Male sexual enhancement with PRP therapy"),
    ("sexual-health", "shockwave-therapy", "Shockwave Therapy", "Non-invasive treatment for sexual dysfunction"),
    ("sexual-health", "testosterone-optimization", "Testosterone Optimization", "Medical testosterone management for men"),
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

TEMPLATES = {
    "facial": ("30-60 minutes", "Topical numbing", "Minimal (1-3 days)", "3-12 months", 
               "{title} at OSHUNJA combines medical expertise with aesthetic precision to enhance your facial appearance. Our Kingston-based physicians use advanced techniques tailored to Caribbean skin tones and the tropical climate."),
    "body": ("1-4 hours", "Local with sedation or general", "2-6 weeks", "Long-lasting (6-12 months)",
             "{title} at OSHUNJA offers advanced body contouring for patients seeking sculpted, natural-looking results. Our fellowship-trained surgeons utilize the latest technology to minimize downtime and maximize outcomes."),
    "hair": ("30-90 minutes", "Topical anesthetic", "Immediate", "6-12 months",
             "{title} at OSHUNJA provides effective treatment for hair concerns using state-of-the-art technology. Our specialists understand the unique characteristics of diverse hair types common in the Caribbean."),
    "pelvic-intimate": ("1-2 hours", "Local or general", "4-6 weeks", "Permanent",
                       "{title} at OSHUNJA is performed with complete discretion and compassion. Our gynecologic specialists provide expert intimate care in a judgment-free, private environment designed for your comfort."),
    "pelvic-reproductive": ("30 minutes - 2 hours", "None to general (varies)", "Same day to 6 weeks", "Varies by procedure",
                           "{title} at OSHUNJA combines gynecologic expertise with patient-centered care. Our board-certified physicians provide comprehensive reproductive health services in Kingston's premier medical facility."),
    "sexual-health": ("30-60 minutes", "Topical or none", "Minimal (1-3 days)", "3-18 months",
                     "{title} at OSHUNJA addresses sexual wellness with medical precision and complete confidentiality. Our specialists provide evidence-based treatments to enhance intimate function and satisfaction."),
    "wellness": ("30-90 minutes", "None", "None", "Ongoing with regular sessions",
                "{title} at OSHUNJA supports your overall health and vitality. Our wellness programs combine medical oversight with personalized care plans tailored to your lifestyle and goals."),
}

def generate(cat, file, title, sub):
    t = TEMPLATES[cat]
    c = TEMPLATE
    c = c.replace("<title>Liposuction 360 in Kingston, Jamaica | Sculpted Silhouette</title>", f"<title>{title} in Kingston, Jamaica | OSHUNJA</title>", 1)
    c = c.replace('Liposuction 360 at OSHUNJA in Kingston, Jamaica sculpts the waist, abdomen, and back with advanced contouring and concierge recovery support.', f"{sub}. Expert {title.lower()} at OSHUNJA in Kingston, Jamaica.", 1)
    c = c.replace('<body class="liposuction-page">', f'<body class="{file}-page">', 1)
    c = c.replace('<h1>Liposuction 360</h1>', f'<h1>{title}</h1>', 1)
    c = c.replace('<p class="hero-subtitle">Artistically remove stubborn fat around the torso with power-assisted liposuction and fluid contouring</p>', f'<p class="hero-subtitle">{sub}</p>', 1)
    c = c.replace('<p>2.5 - 4 hours</p>', f'<p>{t[0]}</p>', 1)
    c = c.replace('<p>Twilight or general</p>', f'<p>{t[1]}</p>', 1)
    c = c.replace('<p>6 weeks</p>', f'<p>{t[2]}</p>', 1)
    c = c.replace('<p>Final at 3-6 months</p>', f'<p>{t[3]}</p>', 1)
    c = c.replace("Liposuction 360 treats the abdomen, waist, flanks, and back in one session to create a smooth, snatched silhouette. OSHUNJA utilises power-assisted cannulas and vibration technology to minimise trauma while maximising precision.", t[4].format(title=title), 1)
    c = c.replace("Our surgeons map each torso individually, considering posture, pelvic tilt, and Caribbean lifestyle habits to deliver results that look balanced in athleisure, beachwear, and tailored fashion.", f"Our Kingston facility provides a private, comfortable environment where you receive personalized attention from consultation through recovery. We understand the unique needs of Caribbean patients and tailor our approach accordingly.", 1)
    c = c.replace("Recovery is supported by onsite lymphatic specialists, IV therapy, and compression fittings, ensuring you feel cared for from consultation through final reveal.", f"Each {title.lower()} treatment plan is customized to your anatomy, goals, and lifestyle. Our team ensures you have realistic expectations and comprehensive aftercare support.", 1)
    c = c.replace("Ready to Design Your Silhouette?", f"Ready to Learn More About {title}?", 1)
    c = c.replace("Reserve a consultation to map a 360 liposuction plan with OSHUNJA's surgical team in Kingston. We'll create a personalized treatment plan tailored to your unique body shape and goals.", f"Book a private consultation to discuss how {title.lower()} can help you achieve your goals. Our Kingston team is here to answer all your questions and create your personalized treatment plan.", 1)
    return c

print("="*70)
print("GENERATING ALL PROCEDURE PAGES")
print("="*70)
success = 0
for cat, file, title, sub in PROCEDURES:
    try:
        content = generate(cat, file, title, sub)
        path = f"{BASE_DIR}/pages/procedures/{cat}/{file}.html"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        success += 1
        print(f"[{success}/{len(PROCEDURES)}] ✓ {cat}/{file}.html")
    except Exception as e:
        print(f"[{success}/{len(PROCEDURES)}] ✗ {cat}/{file}.html - {e}")

print("="*70)
print(f"✓ SUCCESS: Generated {success}/{len(PROCEDURES)} pages!")
print("="*70)
