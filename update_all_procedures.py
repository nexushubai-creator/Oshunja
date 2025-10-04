#!/usr/bin/env python3
"""
Comprehensive update script for all procedure pages:
1. Fix CTA button order (WhatsApp, Virtual Consultation, Book Consultation)
2. Generate high-quality SEO/GEO-optimized content for Kingston, Jamaica
"""

import os
import re
from pathlib import Path

# Procedure definitions with comprehensive SEO/GEO content
PROCEDURES = {
    # FACIAL PROCEDURES
    'botox.html': {
        'category': 'facial',
        'title': 'Botox Injections',
        'meta_title': 'Botox Kingston Jamaica | Expert Anti-Wrinkle Injections | OSHUNJA',
        'meta_description': 'Professional Botox treatments in Kingston, Jamaica. FDA-approved anti-wrinkle injections for forehead lines, crow\'s feet, and frown lines. Book your consultation at OSHUNJA.',
        'hero_title': 'Botox Anti-Wrinkle Injections',
        'hero_subtitle': 'Smooth wrinkles and prevent fine lines with FDA-approved Botox treatments in Kingston, Jamaica',
        'duration': '15-30 minutes',
        'anesthesia': 'None required',
        'recovery': 'Immediate return',
        'results': '3-6 months',
        'overview': [
            'Botox at OSHUNJA uses FDA-approved botulinum toxin to temporarily relax facial muscles that cause wrinkles. Our Kingston-based aesthetic physicians provide expert injections for forehead lines, crow\'s feet, frown lines, and more—delivering natural-looking results that soften signs of aging without freezing your expressions.',
            'Kingston\'s tropical climate and vibrant lifestyle mean you want to look refreshed and youthful year-round. Our conservative injection technique ensures you maintain natural facial movement while smoothing the lines that age your appearance. Each treatment is customized to your unique facial anatomy and aesthetic goals.',
            'Beyond wrinkles, we use Botox for medical applications including excessive sweating (hyperhidrosis), jaw tension (TMJ), and migraine prevention. Our team combines clinical expertise with an artistic eye to help you achieve your ideal results.'
        ],
        'cta_heading': 'Ready to Smooth Away Wrinkles?',
        'cta_text': 'Book a consultation with OSHUNJA\'s aesthetic team in Kingston to discover how Botox can refresh your appearance. We\'ll create a personalized treatment plan designed specifically for your facial structure and goals.'
    },
    
    'microneedling.html': {
        'category': 'facial',
        'title': 'Microneedling',
        'meta_title': 'Microneedling Kingston Jamaica | Collagen Induction Therapy | OSHUNJA',
        'meta_description': 'Professional microneedling treatments in Kingston, Jamaica. Stimulate collagen production for improved skin texture, acne scars, and anti-aging at OSHUNJA.',
        'hero_title': 'Microneedling with PRP',
        'hero_subtitle': 'Rejuvenate your skin with collagen-stimulating microneedling treatments in Kingston, Jamaica',
        'duration': '45-60 minutes',
        'anesthesia': 'Topical numbing cream',
        'recovery': '2-4 days',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'Microneedling at OSHUNJA uses medical-grade devices to create controlled micro-injuries that trigger your skin\'s natural healing response. This stimulates collagen and elastin production, improving skin texture, reducing acne scars, minimizing pores, and diminishing fine lines—all with minimal downtime.',
            'Kingston\'s tropical climate can be challenging for skin health. Our advanced microneedling treatments are customized for Caribbean skin tones, addressing concerns like hyperpigmentation, sun damage, and uneven texture with precision and safety.',
            'We often combine microneedling with platelet-rich plasma (PRP) from your own blood for enhanced results. This "vampire facial" approach accelerates healing and amplifies collagen production for superior skin rejuvenation.'
        ],
        'cta_heading': 'Ready for Healthier, Radiant Skin?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how microneedling can transform your skin. We\'ll evaluate your concerns and create a personalized treatment plan for optimal results.'
    },
    
    'prp-facial.html': {
        'category': 'facial',
        'title': 'PRP Facial',
        'meta_title': 'PRP Facial Kingston Jamaica | Vampire Facial Treatment | OSHUNJA',
        'meta_description': 'Advanced PRP facial treatments in Kingston, Jamaica. Platelet-rich plasma therapy for natural skin rejuvenation, collagen production, and anti-aging at OSHUNJA.',
        'hero_title': 'PRP Facial (Vampire Facial)',
        'hero_subtitle': 'Harness your body\'s healing power for natural skin rejuvenation in Kingston, Jamaica',
        'duration': '60-90 minutes',
        'anesthesia': 'Topical numbing cream',
        'recovery': '3-5 days',
        'results': 'Progressive (2-3 months)',
        'overview': [
            'The PRP Facial at OSHUNJA combines microneedling with platelet-rich plasma (PRP) extracted from your own blood. This powerful treatment stimulates collagen production, improves skin texture, reduces fine lines, and creates a natural glow—using your body\'s own healing growth factors.',
            'In Kingston\'s sun-rich environment, skin can show premature aging from UV exposure. Our PRP facials are particularly effective for Caribbean skin, addressing concerns like hyperpigmentation, sun damage, and uneven tone while promoting cellular regeneration and healing.',
            'The treatment involves drawing a small amount of blood, isolating the concentrated platelets, then applying this serum to your skin during microneedling. The result is accelerated healing, enhanced collagen synthesis, and remarkable skin transformation over the following months.'
        ],
        'cta_heading': 'Ready for Natural Skin Rejuvenation?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how PRP facial therapy can revitalize your skin using your body\'s own healing power. We\'ll create a customized treatment plan for your unique needs.'
    },
    
    # HAIR PROCEDURES
    'laser-hair-removal.html': {
        'category': 'hair',
        'title': 'Laser Hair Removal',
        'meta_title': 'Laser Hair Removal Kingston Jamaica | Permanent Hair Reduction | OSHUNJA',
        'meta_description': 'Professional laser hair removal in Kingston, Jamaica. Safe, effective treatments for all skin tones including darker Caribbean complexions at OSHUNJA.',
        'hero_title': 'Laser Hair Removal',
        'hero_subtitle': 'Achieve smooth, hair-free skin with advanced laser technology in Kingston, Jamaica',
        'duration': '15-60 minutes per area',
        'anesthesia': 'Cooling gel application',
        'recovery': 'Immediate return',
        'results': 'Permanent (6-8 sessions)',
        'overview': [
            'Laser hair removal at OSHUNJA uses advanced technology safe for all skin tones, including darker Caribbean complexions. Our medical-grade lasers target hair follicles to provide permanent hair reduction on face, underarms, bikini, legs, and body—freeing you from constant shaving, waxing, and ingrown hairs.',
            'Kingston\'s warm climate makes unwanted body hair particularly frustrating. Our laser technology is calibrated specifically for melanin-rich skin, ensuring safe and effective treatments without the risk of hyperpigmentation or scarring common with older laser systems.',
            'Most clients need 6-8 sessions spaced several weeks apart for optimal results. Once complete, you\'ll enjoy smooth, hair-free skin indefinitely with only occasional maintenance treatments as needed.'
        ],
        'cta_heading': 'Ready for Smooth, Hair-Free Skin?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how laser hair removal can eliminate unwanted hair permanently. We\'ll assess your skin and hair type to create an effective treatment plan.'
    },
    
    'prp-hair-restoration.html': {
        'category': 'hair',
        'title': 'PRP Hair Restoration',
        'meta_title': 'PRP Hair Restoration Kingston Jamaica | Natural Hair Growth Treatment | OSHUNJA',
        'meta_description': 'Advanced PRP hair restoration in Kingston, Jamaica. Stimulate natural hair growth and combat hair loss with platelet-rich plasma therapy at OSHUNJA.',
        'hero_title': 'PRP Hair Restoration',
        'hero_subtitle': 'Stimulate natural hair growth with platelet-rich plasma therapy in Kingston, Jamaica',
        'duration': '45-60 minutes',
        'anesthesia': 'Local scalp numbing',
        'recovery': '1-2 days',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'PRP Hair Restoration at OSHUNJA uses concentrated platelets from your own blood to stimulate dormant hair follicles and promote natural hair growth. This non-surgical treatment is effective for both male and female pattern hair loss, thinning hair, and early-stage baldness.',
            'Hair loss affects confidence regardless of climate, but Kingston\'s sun exposure can accelerate thinning. Our PRP treatments inject growth factors directly into the scalp, awakening follicles, improving hair density, and strengthening existing strands for fuller, healthier hair.',
            'The process involves drawing blood, isolating platelet-rich plasma, then injecting it strategically across areas of thinning or loss. Most patients see visible improvements within 3-6 months, with optimal results after a series of 3-4 treatments.'
        ],
        'cta_heading': 'Ready to Restore Your Hair Naturally?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how PRP hair restoration can stimulate natural growth and combat hair loss. We\'ll evaluate your scalp and create a personalized treatment plan.'
    },
    
    # BODY PROCEDURES
    'liposuction-360-180.html': {
        'category': 'body',
        'title': 'Liposuction 360/180',
        'meta_title': 'Liposuction 360 Kingston Jamaica | Comprehensive Body Contouring | OSHUNJA',
        'meta_description': 'Expert Liposuction 360/180 in Kingston, Jamaica. Comprehensive torso sculpting and body contouring with advanced techniques at OSHUNJA.',
        'hero_title': 'Liposuction 360/180',
        'hero_subtitle': 'Comprehensive body contouring for a sculpted, balanced silhouette in Kingston, Jamaica',
        'duration': '2-4 hours',
        'anesthesia': 'General or IV sedation',
        'recovery': '2-4 weeks',
        'results': 'Permanent with maintenance',
        'overview': [
            'Liposuction 360/180 at OSHUNJA provides comprehensive body contouring by removing stubborn fat deposits around your entire torso or midsection. This advanced technique sculpts your abdomen, flanks, back, and waist in a single procedure for balanced, dramatic results that diet and exercise alone can\'t achieve.',
            'Kingston\'s active lifestyle culture means you want a body that reflects your efforts. Our board-certified surgeon uses advanced tumescent liposuction and power-assisted techniques to precisely remove fat, contour your silhouette, and create the definition you desire with minimal downtime.',
            'The "360" approach treats the entire circumference of your torso, while "180" focuses on front or back. Both methods create harmonious proportions and address multiple problem areas simultaneously for comprehensive transformation.'
        ],
        'cta_heading': 'Ready for Total Body Transformation?',
        'cta_text': 'Book a consultation with OSHUNJA\'s surgical team in Kingston to discover how Liposuction 360/180 can sculpt your ideal physique. We\'ll evaluate your anatomy and create a personalized surgical plan.'
    },
    
    'prp-breast-lift.html': {
        'category': 'body',
        'title': 'PRP Breast Lift',
        'meta_title': 'PRP Breast Lift Kingston Jamaica | Non-Surgical Breast Enhancement | OSHUNJA',
        'meta_description': 'Non-surgical PRP breast lift in Kingston, Jamaica. Natural breast enhancement and improved skin quality with platelet-rich plasma at OSHUNJA.',
        'hero_title': 'PRP Breast Lift (Vampire Breast Lift)',
        'hero_subtitle': 'Non-surgical breast enhancement using your body\'s natural healing power in Kingston, Jamaica',
        'duration': '45-60 minutes',
        'anesthesia': 'Local numbing cream',
        'recovery': '2-3 days',
        'results': '12-18 months',
        'overview': [
            'The PRP Breast Lift at OSHUNJA offers non-surgical breast enhancement by injecting platelet-rich plasma to improve skin texture, increase subtle volume, and enhance cleavage appearance. This natural approach uses your body\'s growth factors to rejuvenate breast tissue without implants or surgery.',
            'For Kingston women seeking subtle enhancement without downtime, the PRP breast lift provides a natural alternative. The treatment improves skin quality, adds mild volume, and creates a more youthful appearance—perfect for addressing minor sagging, enhancing cleavage, or improving skin tone.',
            'We extract and concentrate platelets from your blood, then strategically inject them into breast tissue. The growth factors stimulate collagen production and tissue regeneration for gradual, natural-looking improvements over several months.'
        ],
        'cta_heading': 'Ready for Natural Breast Enhancement?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how PRP breast lift can enhance your natural beauty without surgery. We\'ll discuss your goals and create a personalized treatment plan.'
    },
    
    'renuvion-abdomen.html': {
        'category': 'body',
        'title': 'Renuvion Abdomen',
        'meta_title': 'Renuvion Abdomen Kingston Jamaica | Skin Tightening Treatment | OSHUNJA',
        'meta_description': 'Advanced Renuvion skin tightening for abdomen in Kingston, Jamaica. Non-surgical body contouring with helium plasma technology at OSHUNJA.',
        'hero_title': 'Renuvion - Abdomen',
        'hero_subtitle': 'Advanced skin tightening technology for a firmer, more contoured abdomen in Kingston, Jamaica',
        'duration': '60-90 minutes',
        'anesthesia': 'Local with sedation',
        'recovery': '1-2 weeks',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'Renuvion for the abdomen at OSHUNJA uses revolutionary helium plasma technology to tighten loose skin and improve contours without major surgery. This minimally invasive treatment is ideal for post-pregnancy laxity, weight loss skin excess, or aging-related looseness in the abdominal area.',
            'Many Kingston residents struggle with loose abdominal skin that won\'t respond to diet or exercise. Renuvion delivers controlled heat beneath the skin to trigger immediate contraction and long-term collagen remodeling for significant tightening with minimal downtime.',
            'The procedure involves small incisions through which the Renuvion wand delivers precise energy to subdermal tissue. Results improve progressively over 3-6 months as collagen remodels and skin continues to tighten naturally.'
        ],
        'cta_heading': 'Ready for a Firmer, Tighter Abdomen?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how Renuvion can tighten your abdominal skin without major surgery. We\'ll evaluate your concerns and create a customized treatment plan.'
    },
    
    'renuvion-back.html': {
        'category': 'body',
        'title': 'Renuvion Back',
        'meta_title': 'Renuvion Back Kingston Jamaica | Back Skin Tightening | OSHUNJA',
        'meta_description': 'Advanced Renuvion skin tightening for back in Kingston, Jamaica. Smooth bra bulges and improve back contours with plasma technology at OSHUNJA.',
        'hero_title': 'Renuvion - Back',
        'hero_subtitle': 'Eliminate bra bulges and tighten back skin with advanced plasma technology in Kingston, Jamaica',
        'duration': '60-90 minutes',
        'anesthesia': 'Local with sedation',
        'recovery': '1-2 weeks',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'Renuvion for the back at OSHUNJA targets stubborn fat rolls, bra bulges, and loose skin using revolutionary helium plasma technology. This minimally invasive treatment smooths your back contours and tightens skin for a more sculpted, youthful appearance.',
            'Kingston\'s beach and pool culture means you want to feel confident in backless dresses and swimwear. Renuvion addresses back concerns that are difficult to improve with diet and exercise alone, providing dramatic results with minimal downtime.',
            'The treatment uses controlled plasma energy delivered beneath the skin to tighten tissue, smooth irregularities, and create better definition. Results continue improving for months as collagen remodeling enhances your back contours.'
        ],
        'cta_heading': 'Ready for a Smoother, More Sculpted Back?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how Renuvion can eliminate back bulges and tighten skin. We\'ll assess your anatomy and create a personalized treatment plan.'
    },
    
    'renuvion-neck.html': {
        'category': 'body',
        'title': 'Renuvion Neck',
        'meta_title': 'Renuvion Neck Kingston Jamaica | Non-Surgical Neck Lift | OSHUNJA',
        'meta_description': 'Advanced Renuvion neck tightening in Kingston, Jamaica. Eliminate turkey neck and sagging with minimally invasive plasma technology at OSHUNJA.',
        'hero_title': 'Renuvion - Neck',
        'hero_subtitle': 'Tighten and rejuvenate your neck with advanced plasma technology in Kingston, Jamaica',
        'duration': '45-60 minutes',
        'anesthesia': 'Local with sedation',
        'recovery': '1-2 weeks',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'Renuvion for the neck at OSHUNJA uses helium plasma technology to tighten loose skin, eliminate jowls, and define your jawline without major surgery. This minimally invasive treatment addresses aging neck concerns including turkey neck, sagging, and loss of definition.',
            'The neck is often the first area to show aging signs, something Kingston\'s sun exposure can accelerate. Renuvion provides significant tightening and contouring without the extended downtime of traditional neck lift surgery.',
            'Through tiny incisions, controlled plasma energy is delivered beneath neck skin to trigger immediate contraction and stimulate long-term collagen production. The result is a more youthful, defined neck and jawline that continues improving over several months.'
        ],
        'cta_heading': 'Ready for a More Defined, Youthful Neck?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how Renuvion can rejuvenate your neck without major surgery. We\'ll evaluate your concerns and design a customized treatment approach.'
    },
    
    'renuvion-arms.html': {
        'category': 'body',
        'title': 'Renuvion Arms',
        'meta_title': 'Renuvion Arms Kingston Jamaica | Arm Skin Tightening | OSHUNJA',
        'meta_description': 'Advanced Renuvion arm tightening in Kingston, Jamaica. Eliminate arm sagging and improve contours with minimally invasive plasma technology at OSHUNJA.',
        'hero_title': 'Renuvion - Arms',
        'hero_subtitle': 'Tighten and tone your arms with advanced plasma technology in Kingston, Jamaica',
        'duration': '60-90 minutes',
        'anesthesia': 'Local with sedation',
        'recovery': '1-2 weeks',
        'results': 'Progressive (3-6 months)',
        'overview': [
            'Renuvion for the arms at OSHUNJA uses helium plasma technology to tighten loose skin and improve arm contours without traditional brachioplasty surgery. This minimally invasive treatment addresses sagging upper arms, often called "bat wings," that resist diet and exercise.',
            'Kingston\'s warm climate means sleeveless clothing is a staple. Renuvion allows you to achieve firmer, more toned-looking arms without the extensive scars and downtime of surgical arm lifts.',
            'The procedure delivers controlled plasma energy beneath arm skin through small incisions. This triggers immediate tissue contraction and stimulates months of collagen remodeling for progressive tightening and improved arm definition.'
        ],
        'cta_heading': 'Ready for Firmer, More Toned Arms?',
        'cta_text': 'Book a consultation with OSHUNJA in Kingston to discover how Renuvion can tighten your arms without major surgery. We\'ll assess your concerns and create a personalized treatment plan.'
    },
}

def calculate_relative_path(file_path, base_dir):
    """Calculate relative path from file to base directory."""
    file_dir = os.path.dirname(file_path)
    rel_path = os.path.relpath(base_dir, file_dir)
    if rel_path == '.':
        return ''
    return rel_path + '/'

def fix_cta_buttons(html_content, home_path):
    """Fix CTA button order and add Virtual Consultation button."""
    # Pattern to match the cta-buttons div
    pattern = r'(<div class="cta-buttons">)(.*?)(</div>)'
    
    def replace_buttons(match):
        # New button structure with correct order
        new_buttons = f'''
                        <a href="https://wa.me/18766115100" class="btn btn-secondary btn-large">WhatsApp Us</a>
                        <a href="#" class="btn btn-virtual-consult virtual-consult-trigger btn-large">Virtual Consultation</a>
                        <a href="{home_path}pages/contact.html" class="btn btn-primary btn-large">Book Consultation</a>
                    '''
        return match.group(1) + new_buttons + match.group(3)
    
    return re.sub(pattern, replace_buttons, html_content, flags=re.DOTALL)

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
    
    print(f"Found {len(html_files)} procedure pages to update\n")
    
    success_count = 0
    for file_path in html_files:
        try:
            # Read current content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate relative path
            home_path = calculate_relative_path(file_path, base_dir)
            
            # Fix CTA buttons
            updated_content = fix_cta_buttons(content, home_path)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"✓ Updated: {rel_path}")
            success_count += 1
            
        except Exception as e:
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"✗ Failed: {rel_path} - {e}")
    
    print(f"\n{'='*60}")
    print(f"Successfully updated {success_count}/{len(html_files)} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
