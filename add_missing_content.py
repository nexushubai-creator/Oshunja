#!/usr/bin/env python3
"""
Script to add missing Benefits & Results and Candidates sections to procedure pages
"""

import os
import re
from pathlib import Path

# Content database for procedures missing benefits and candidates sections
MISSING_CONTENT = {
    # Body procedures
    'liposuction-360': {
        'benefits': """Liposuction 360 provides comprehensive body contouring by removing stubborn fat from the entire torso circumference - abdomen, flanks, back, and sides. This advanced technique creates dramatic waist definition, improved body proportions, and enhanced curves that diet and exercise alone cannot achieve.
        
Results are typically visible immediately with continued improvement over 3-6 months as swelling subsides. Patients experience significant reduction in stubborn fat deposits, improved clothing fit, enhanced confidence, and a more sculpted, proportional silhouette that highlights their natural curves.""",
        'candidates': """Ideal candidates for Liposuction 360 are individuals within 20-30 pounds of their goal weight with stubborn fat deposits around the entire midsection that resist diet and exercise. You should be in good health, have realistic expectations, and be committed to maintaining results through healthy lifestyle choices.
        
During your consultation in Kingston, we'll assess your body composition, skin elasticity, and aesthetic goals to determine if Liposuction 360 can deliver your desired body contouring results."""
    },
    
    'liposuction-360-180': {
        'benefits': """Liposuction 360/180 combines comprehensive torso contouring (360°) with targeted treatment of specific areas (180°) for ultimate body sculpting results. This advanced approach removes stubborn fat while creating enhanced definition, improved proportions, and dramatic transformation that addresses your unique body concerns.
        
Results provide significant fat reduction, improved body contours, enhanced waist-to-hip ratio, and boosted confidence. Most patients achieve their desired silhouette with long-lasting results when combined with healthy lifestyle maintenance.""",
        'candidates': """Candidates for Liposuction 360/180 are individuals seeking comprehensive body transformation with realistic expectations about surgical body contouring. You should be in good health, near your ideal weight, and committed to maintaining results through proper nutrition and exercise.
        
Your Kingston consultation will include detailed body analysis and goal-setting to create a customized surgical plan that addresses your specific contouring needs."""
    },
    
    'prp-breast-lift': {
        'benefits': """PRP Breast Lift (Vampire Breast Lift) provides natural breast enhancement using your body's own platelet-rich plasma to improve skin quality, fullness, and nipple sensitivity. This non-surgical approach offers subtle lifting, improved texture, and enhanced appearance without implants or surgery.
        
Results include improved breast skin tone, enhanced nipple sensitivity, subtle volume improvement, and better overall breast appearance. Effects typically develop over 2-3 months and can last 12-18 months with maintenance treatments.""",
        'candidates': """Ideal candidates for PRP Breast Lift are women seeking natural breast enhancement without surgery, experiencing decreased sensitivity, or wanting to improve breast skin quality. You should be in good health, have realistic expectations about non-surgical results, and be seeking subtle improvements.
        
During your consultation in Kingston, we'll assess your breast anatomy, discuss your enhancement goals, and determine if PRP treatment can achieve your desired improvements."""
    },
    
    # Hair procedures
    'prp-hair-restoration': {
        'benefits': """PRP Hair Restoration stimulates natural hair growth using your body's own platelet-rich plasma to reactivate dormant hair follicles. This non-surgical treatment increases hair density, thickness, and overall scalp health while slowing further hair loss progression.
        
Results typically show initial improvement within 3-4 months with optimal results at 6-12 months. Patients experience increased hair density, thicker existing hair, improved scalp health, and slowed hair loss progression with regular maintenance treatments.""",
        'candidates': """Ideal candidates for PRP Hair Restoration are individuals experiencing early to moderate hair thinning, pattern baldness, or diffuse hair loss with viable hair follicles. You should be in good health, have realistic expectations about hair regrowth timelines, and be committed to a treatment series.
        
Your Kingston consultation will include scalp analysis and hair loss assessment to determine if PRP can effectively address your specific hair restoration needs."""
    },
    
    'laser-hair-removal': {
        'benefits': """Laser Hair Removal provides permanent hair reduction using advanced laser technology that targets hair follicles while protecting surrounding skin. This treatment eliminates the need for shaving, waxing, or plucking while providing smooth, hair-free skin with lasting results.
        
Results show progressive hair reduction over 6-8 treatments with most patients achieving 85-95% permanent hair reduction. Benefits include smooth skin, eliminated ingrown hairs, time savings from daily shaving, and increased confidence in any situation.""",
        'candidates': """Ideal candidates for Laser Hair Removal are individuals with unwanted body or facial hair seeking permanent reduction. Treatment works best on darker hair with lighter skin, though advanced lasers can treat various skin tones. You should avoid sun exposure and have realistic expectations about treatment timelines.
        
During your consultation in Kingston, we'll assess your hair and skin type, discuss treatment areas, and create a customized laser hair removal plan for optimal results."""
    },
    
    # Wellness procedures
    'ozempic': {
        'benefits': """Ozempic (semaglutide) provides significant weight loss by regulating appetite, slowing gastric emptying, and improving blood sugar control. This FDA-approved medication helps patients lose 12-15% of body weight while reducing cardiovascular risks and improving overall metabolic health.
        
Results include sustained weight loss, reduced appetite, improved blood sugar control, decreased cardiovascular risk, and enhanced quality of life. Most patients see initial results within 4-6 weeks with continued improvement over 68 weeks of treatment.""",
        'candidates': '''Ideal candidates for Ozempic are individuals with BMI ≥30 or BMI ≥27 with weight-related health conditions who have struggled with traditional weight loss methods. You should be committed to lifestyle changes and ongoing medical monitoring for optimal results.
        
During your consultation in Kingston, we'll assess your medical history, current medications, and weight loss goals to determine if Ozempic is appropriate for your situation.'''
    },
    
    'mounjaro': {
        'benefits': """Mounjaro (tirzepatide) offers superior weight loss results by targeting both GLP-1 and GIP receptors for enhanced appetite control and metabolic improvement. Clinical studies show average weight loss of 15-22% with improvements in blood sugar, blood pressure, and cardiovascular health.
        
Results provide significant sustained weight loss, reduced hunger, improved metabolic markers, better energy levels, and enhanced overall health. Most patients experience initial benefits within 2-4 weeks with continued improvement over time.""",
        'candidates': '''Candidates for Mounjaro include individuals with obesity or significant overweight with related health conditions who need comprehensive medical weight management. You should be ready for lifestyle modifications and regular medical monitoring throughout treatment.
        
Your Kingston consultation will include comprehensive health assessment and goal-setting to determine if Mounjaro can help you achieve sustainable weight loss success.'''
    },
    
    'dietetics': {
        'benefits': """Professional dietetics consultation provides personalized nutrition guidance to optimize health, manage medical conditions, and achieve sustainable lifestyle changes. Our registered dietitians create customized meal plans that align with your health goals, medical needs, and personal preferences.
        
Results include improved nutritional status, better management of chronic conditions, sustainable weight management, increased energy levels, and enhanced overall wellness through evidence-based dietary strategies.""",
        'candidates': """Ideal candidates for dietetics consultation include individuals seeking personalized nutrition guidance, managing chronic conditions through diet, or wanting to optimize their health through proper nutrition. This service benefits people of all ages and health statuses.
        
During your consultation in Kingston, our dietitian will assess your current eating patterns, health status, and goals to create a personalized nutrition plan for optimal results."""
    },
    
    'iv-therapy': {
        'benefits': """IV Therapy delivers essential vitamins, minerals, and nutrients directly into your bloodstream for immediate absorption and maximum effectiveness. This treatment provides rapid hydration, immune system support, energy enhancement, and overall wellness optimization.
        
Results include immediate hydration, increased energy levels, enhanced immune function, improved mental clarity, faster recovery from illness or fatigue, and overall wellness enhancement with effects lasting several days to weeks.""",
        'candidates': """Ideal candidates for IV Therapy include individuals seeking rapid rehydration, immune support, energy enhancement, or recovery from illness, travel, or strenuous activity. Most healthy adults can benefit from customized IV nutrient therapy.
        
Your Kingston consultation will include health assessment and goal discussion to select the optimal IV therapy formulation for your specific wellness needs."""
    },
    
    'sauna': {
        'benefits': """Sauna therapy provides numerous health benefits through heat exposure including improved cardiovascular health, enhanced recovery, stress reduction, and detoxification. Regular sauna use supports immune function, promotes relaxation, and can improve skin health and overall wellness.
        
Results include improved circulation, enhanced recovery from exercise, stress reduction, better sleep quality, potential longevity benefits, and overall health optimization through regular heat therapy sessions.""",
        'candidates': """Sauna therapy benefits most healthy individuals seeking natural wellness enhancement, stress reduction, or improved recovery. You should be able to tolerate heat exposure and be free from conditions that contraindicate heat therapy.
        
During consultation in Kingston, we'll assess your health status and goals to determine the optimal sauna protocol for your wellness enhancement needs."""
    },
    
    'wellness-coaching': {
        'benefits': """Wellness Coaching provides personalized guidance and accountability to help you achieve lasting health and lifestyle improvements. Our certified coaches work with you to identify obstacles, set realistic goals, and develop sustainable habits for long-term wellness success.
        
Results include improved health behaviors, increased motivation and accountability, better stress management, enhanced work-life balance, and sustainable lifestyle changes that support long-term health and happiness.""",
        'candidates': """Ideal candidates for Wellness Coaching are individuals ready to make positive lifestyle changes who would benefit from professional guidance, accountability, and support. This service helps anyone wanting to improve their health, habits, or overall well-being.
        
Your Kingston consultation will include wellness assessment and goal-setting to create a personalized coaching plan that addresses your unique needs and aspirations."""
    },
    
    'metabolic-health-testing': {
        'benefits': """Comprehensive Metabolic Health Testing provides detailed analysis of your body's metabolic function, nutrient status, hormone levels, and overall health markers. This testing identifies potential health risks, nutritional deficiencies, and opportunities for optimization before symptoms appear.
        
Results include personalized health insights, early detection of potential issues, customized treatment recommendations, and baseline measurements for tracking health improvements over time.""",
        'candidates': """Metabolic Health Testing benefits individuals seeking comprehensive health assessment, those with family history of metabolic conditions, or anyone wanting to optimize their health proactively. This testing is valuable for preventive care and health optimization.
        
During your consultation in Kingston, we'll discuss your health history and goals to determine the most appropriate testing panel for your individual needs."""
    },
    
    # Facial procedures  
    'botox': {
        'benefits': """Botox Anti-Wrinkle Injections effectively reduce dynamic wrinkles caused by repeated facial expressions, including forehead lines, crow's feet, and frown lines. This FDA-approved treatment provides natural-looking results that smooth skin while maintaining your ability to express emotions naturally.
        
Results typically appear within 3-7 days and last 3-4 months. Patients experience smoother skin, reduced appearance of wrinkles, improved confidence, and a refreshed appearance that looks natural and youthful.""",
        'candidates': """Ideal candidates for Botox are adults with dynamic wrinkles who want to reduce signs of aging while maintaining natural facial expressions. You should be in good health, not pregnant or breastfeeding, and have realistic expectations about anti-aging results.
        
During your consultation in Kingston, we'll assess your facial anatomy and discuss your aesthetic goals to create a customized Botox treatment plan for optimal, natural-looking results."""
    },
    
    'juvederm': {
        'benefits': """Juvederm Dermal Fillers restore volume, smooth wrinkles, and enhance facial features using hyaluronic acid-based formulations. These treatments provide immediate results that look and feel natural, addressing age-related volume loss and creating enhanced facial harmony.
        
Results are visible immediately and typically last 9-18 months depending on the product used. Patients experience restored facial volume, smoother skin, enhanced lips or cheeks, and a more youthful, refreshed appearance.""",
        'candidates': """Ideal candidates for Juvederm are adults experiencing age-related volume loss, wanting lip enhancement, or seeking to smooth moderate to severe facial wrinkles. You should be in good health and have realistic expectations about dermal filler results.
        
Your Kingston consultation will include facial assessment and goal discussion to select the appropriate Juvederm product and technique for your desired aesthetic enhancement."""
    },
    
    'microneedling': {
        'benefits': """Microneedling with PRP stimulates natural collagen production to improve skin texture, reduce scarring, minimize pore size, and enhance overall skin quality. This treatment combines mechanical stimulation with your body's own growth factors for optimal skin rejuvenation results.
        
Results include improved skin texture, reduced acne scarring, minimized fine lines, smaller pore appearance, and enhanced overall skin tone and quality. Optimal results develop over 2-3 months with continued improvement over time.""",
        'candidates': """Ideal candidates for Microneedling are individuals with acne scarring, uneven skin texture, large pores, or mild signs of aging who want natural skin improvement. Most skin types can benefit from this treatment with proper pre and post-care.
        
During your consultation in Kingston, we'll assess your skin condition and concerns to determine if microneedling with PRP can achieve your desired skin improvement goals."""
    },
    
    'prp-facial': {
        'benefits': """PRP Facial (Vampire Facial) uses your body's own platelet-rich plasma to stimulate natural skin regeneration, improve texture, and enhance overall skin quality. This natural treatment promotes collagen production for lasting skin improvement without synthetic ingredients.
        
Results include improved skin tone and texture, reduced fine lines, enhanced radiance, better skin elasticity, and overall skin rejuvenation. Benefits develop over 2-3 months with peak results lasting 12-18 months.""",
        'candidates': """Ideal candidates for PRP Facial are individuals seeking natural skin rejuvenation, wanting to improve skin texture and tone, or looking for anti-aging treatments without synthetic products. Most skin types benefit from this natural approach.
        
Your Kingston consultation will include skin analysis and goal discussion to determine if PRP facial treatment can achieve your desired natural skin enhancement results."""
    }
}

def add_missing_sections(file_path, procedure_name):
    """Add missing Benefits and Candidates sections to a procedure page"""
    if procedure_name not in MISSING_CONTENT:
        return False
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if sections are missing
        has_benefits = 'Benefits & Results</h2>' in content and len(re.search(r'Benefits & Results</h2>\s*<p>([^<]+)', content, re.DOTALL).group(1)) > 50 if re.search(r'Benefits & Results</h2>\s*<p>([^<]+)', content, re.DOTALL) else False
        has_candidates = 'Ideal Candidates & Considerations</h2>' in content and len(re.search(r'Ideal Candidates & Considerations</h2>\s*<p>([^<]+)', content, re.DOTALL).group(1)) > 50 if re.search(r'Ideal Candidates & Considerations</h2>\s*<p>([^<]+)', content, re.DOTALL) else False
        
        if has_benefits and has_candidates:
            return False  # Already has content
        
        original_content = content
        
        # Add Benefits section if missing or inadequate
        if not has_benefits:
            benefits_pattern = r'(<!-- Benefits Section -->\s*<section class="procedure-section fade-in-element">\s*<h2>Benefits & Results</h2>\s*<p>)[^<]+(</p>\s*</section>)'
            benefits_replacement = f'\\g<1>{MISSING_CONTENT[procedure_name]["benefits"]}\\g<2>'
            content = re.sub(benefits_pattern, benefits_replacement, content, flags=re.DOTALL)
        
        # Add Candidates section if missing or inadequate  
        if not has_candidates:
            candidates_pattern = r'(<!-- Candidates Section -->\s*<section id="ideal-candidates" class="procedure-section section-alt fade-in-element">\s*<h2>Ideal Candidates & Considerations</h2>\s*<p>)[^<]+(</p>\s*<p>During your consultation in Kingston[^<]+</p>\s*</section>)'
            candidates_replacement = f'\\g<1>{MISSING_CONTENT[procedure_name]["candidates"]}\\g<2>'
            content = re.sub(candidates_pattern, candidates_replacement, content, flags=re.DOTALL)
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added missing content to {procedure_name}.html")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to add missing content"""
    base_dir = Path("pages/procedures")
    html_files = list(base_dir.rglob("*.html"))
    
    print(f"🔧 ADDING MISSING BENEFITS & CANDIDATES SECTIONS")
    print(f"=" * 55)
    print(f"Processing {len(html_files)} files...\n")
    
    fixed_count = 0
    
    for file_path in html_files:
        procedure_name = file_path.stem
        if add_missing_sections(str(file_path), procedure_name):
            fixed_count += 1
    
    print(f"\n📊 RESULTS:")
    print(f"Files processed: {len(html_files)}")
    print(f"Files updated: {fixed_count}")
    print(f"Files with missing content definitions: {len(html_files) - len(MISSING_CONTENT)}")
    
    if fixed_count > 0:
        print(f"\n✅ Successfully added missing content to {fixed_count} procedure pages!")
    else:
        print(f"\n⚠️  No files were updated. Either content already exists or procedure definitions are missing.")

if __name__ == "__main__":
    main()