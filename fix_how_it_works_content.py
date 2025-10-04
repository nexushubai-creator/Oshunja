#!/usr/bin/env python3
"""
Replaces generic 'How It Works' content with procedure-specific information.
"""

import os
import re

# Procedure-specific "How It Works" content
HOW_IT_WORKS_CONTENT = {
    # WELLNESS
    'ozempic.html': '''
                <p>Ozempic (semaglutide) is a GLP-1 receptor agonist administered as a once-weekly injection. During your initial consultation at OSHUNJA in Kingston, we'll review your medical history, discuss your weight loss goals, and determine if Ozempic is appropriate for you.</p>
                <p>Treatment begins with a low starter dose that gradually increases over 4-8 weeks to minimize side effects. We'll teach you proper injection technique and provide ongoing monitoring to track your progress, adjust dosing as needed, and ensure optimal results while maintaining your safety.</p>
            ''',
    
    'mounjaro.html': '''
                <p>Mounjaro (tirzepatide) is a dual GIP/GLP-1 receptor agonist delivered via once-weekly injection. Your Kingston consultation includes comprehensive metabolic assessment, goal setting, and medical clearance to ensure this advanced treatment is right for your needs.</p>
                <p>We start with the lowest effective dose and titrate upward based on your response and tolerance. Our team provides injection training, nutritional guidance, and regular follow-ups to optimize your weight loss journey and overall metabolic health.</p>
            ''',
    
    'iv-therapy.html': '''
                <p>IV therapy at OSHUNJA delivers vitamins, minerals, and hydration directly into your bloodstream for 100% absorption. Your session begins with selecting the appropriate IV cocktail based on your wellness goals—whether that's energy enhancement, immune support, athletic recovery, or beauty-focused nutrients.</p>
                <p>You'll relax comfortably in our Kingston facility while the IV infusion runs for 30-60 minutes. Most clients feel energized and refreshed immediately, with benefits lasting days to weeks depending on the formula chosen.</p>
            ''',
    
    'dietetics.html': '''
                <p>Our registered dietitian provides personalized nutrition counseling tailored to your specific health goals and dietary needs. Initial consultations include comprehensive assessment of your current diet, medical conditions, lifestyle factors, and nutritional status.</p>
                <p>You'll receive customized meal plans, practical strategies for sustainable eating habits, and ongoing support through follow-up sessions. Whether managing chronic conditions, optimizing athletic performance, or pursuing weight goals, our Kingston-based nutritionist guides you every step of the way.</p>
            ''',
    
    'wellness-coaching.html': '''
                <p>Wellness coaching at OSHUNJA provides accountability and support for achieving your health goals. Sessions combine goal-setting, behavior modification techniques, and practical strategies for sustainable lifestyle changes across nutrition, movement, stress management, and sleep optimization.</p>
                <p>Your coach meets with you regularly—in person in Kingston or virtually—to track progress, adjust strategies, and provide motivation. This holistic approach addresses mind and body for comprehensive wellness transformation.</p>
            ''',
    
    'metabolic-health-testing.html': '''
                <p>Metabolic health testing includes comprehensive bloodwork to assess glucose control, insulin sensitivity, thyroid function, hormone levels, and other key metabolic markers. Testing is performed at our Kingston facility or partnered labs for convenience.</p>
                <p>Results are thoroughly reviewed during your follow-up consultation, where our medical team interprets findings, identifies areas for improvement, and creates targeted interventions to optimize your metabolic health and longevity.</p>
            ''',
    
    'sauna.html': '''
                <p>Infrared sauna sessions at OSHUNJA provide therapeutic heat therapy in a comfortable, private setting. Sessions typically last 30-45 minutes at temperatures between 120-140°F, promoting deep detoxification through sweat while remaining comfortable enough to relax.</p>
                <p>The infrared heat penetrates deeply to enhance circulation, reduce inflammation, support detoxification, and promote relaxation. Many Kingston clients incorporate regular sauna sessions into their wellness routines for ongoing benefits.</p>
            ''',
    
    'cold-plunge.html': '''
                <p>Cold plunge therapy involves brief immersion (2-5 minutes) in cold water (45-55°F) to trigger beneficial physiological responses. Our Kingston facility provides guided cold exposure in a controlled, safe environment with proper supervision for first-timers.</p>
                <p>Cold therapy reduces inflammation, enhances recovery, boosts mood through endorphin release, and may improve metabolic function. Regular practice builds cold tolerance and amplifies benefits over time.</p>
            ''',
    
    'salt-blocks.html': '''
                <p>Himalayan salt therapy (halotherapy) involves breathing air saturated with microscopic salt particles in our dedicated salt room. Sessions last 45-60 minutes while you relax in a tranquil environment as salt particles are dispersed throughout the space.</p>
                <p>The salt-enriched air supports respiratory health, may help with skin conditions, and promotes relaxation. Many Kingston clients find regular salt therapy sessions beneficial for seasonal allergies, asthma, or general wellness.</p>
            ''',
    
    # SEXUAL HEALTH  
    'o-shot.html': '''
                <p>The O-Shot uses platelet-rich plasma (PRP) from your own blood to rejuvenate vaginal tissue and enhance sexual function. Your blood is drawn and processed to concentrate healing growth factors, then strategically injected into areas around the clitoris and upper vaginal wall using precise, proven protocols.</p>
                <p>The procedure is performed in our private Kingston facility with topical numbing for comfort. Most patients experience minimal discomfort and can return to normal activities immediately, with sexual activity resumed after 24-48 hours.</p>
            ''',
    
    'p-shot.html': '''
                <p>The P-Shot (Priapus Shot) uses PRP injected into specific areas of the penis to enhance function, sensitivity, and size. After blood draw and PRP preparation, targeted injections deliver concentrated growth factors to stimulate tissue regeneration and improve blood flow.</p>
                <p>The procedure takes about 30 minutes at our Kingston clinic with topical anesthesia for comfort. Results develop gradually over 2-3 months as tissue remodeling occurs, with benefits lasting 12-18 months or longer.</p>
            ''',
    
    'clit-shot.html': '''
                <p>The Clitoral Shot delivers PRP precisely to clitoral tissue to enhance sensitivity and sexual response. Similar to the O-Shot, this focused treatment uses your body's natural healing factors concentrated from your own blood and injected with precision using proven techniques.</p>
                <p>Treatment is performed in complete privacy at our Kingston facility with topical numbing. The quick procedure causes minimal discomfort with no downtime, allowing immediate return to daily activities.</p>
            ''',
    
    'emsella-chair.html': '''
                <p>The Emsella Chair provides non-invasive pelvic floor strengthening using High-Intensity Focused Electromagnetic (HIFEM) technology. You remain fully clothed while seated on the specialized chair, which delivers thousands of supramaximal pelvic floor contractions during each 28-minute session.</p>
                <p>Most patients complete a series of 6 treatments over 3 weeks at our Kingston clinic. You'll feel intense but painless muscle contractions during treatment, with improvement in urinary control and sexual function developing progressively over the treatment course and beyond.</p>
            ''',
    
    'shockwave-therapy.html': '''
                <p>Low-intensity shockwave therapy delivers acoustic waves to penile tissue to improve blood flow and stimulate tissue regeneration. Treatment involves applying a specialized wand to different areas of the penis for 15-20 minutes, creating micro-trauma that triggers healing and new blood vessel formation.</p>
                <p>Most patients complete 6-12 sessions over several weeks at our Kingston facility. The treatment is painless with no anesthesia needed, and you can immediately resume all normal activities including sexual activity.</p>
            ''',
    
    'bioidentical-hormones-women.html': '''
                <p>Bioidentical hormone therapy begins with comprehensive testing to assess your current hormone levels including estrogen, progesterone, testosterone, and thyroid hormones. Based on results and symptoms, we create a customized hormone prescription delivered via cream, pellets, or other methods.</p>
                <p>Regular follow-ups at our Kingston clinic monitor your response, adjust dosing as needed, and ensure optimal hormone balance. Most women notice improvement in energy, mood, sleep, and other symptoms within weeks of starting treatment.</p>
            ''',
    
    'bioidentical-hormones-men.html': '''
                <p>Male hormone optimization starts with detailed lab work assessing testosterone, estrogen, thyroid, and other key hormones. If deficiency is confirmed, we develop a personalized treatment plan using bioidentical hormones delivered through injections, creams, or pellets based on your preference and needs.</p>
                <p>Our Kingston team monitors your progress closely, adjusting dosing to achieve optimal levels while avoiding side effects. Most men experience improvements in energy, strength, mood, and sexual function within 4-6 weeks.</p>
            ''',
    
    'testosterone-optimization.html': '''
                <p>Testosterone replacement therapy begins with comprehensive blood work to confirm deficiency and rule out contraindications. Once cleared, treatment is initiated using your preferred delivery method—injections (weekly or bi-weekly), topical cream, or subcutaneous pellets (every 3-4 months).</p>
                <p>Regular monitoring through follow-up labs and visits at our Kingston clinic ensures therapeutic testosterone levels are achieved and maintained safely. Most patients notice significant improvements in energy, body composition, and quality of life within the first few months.</p>
            ''',
    
    'menopause-management.html': '''
                <p>Comprehensive menopause management begins with symptom assessment and hormone testing to understand your specific needs. Treatment may include hormone replacement therapy, non-hormonal medications, lifestyle modifications, and nutritional support tailored to your symptoms and medical history.</p>
                <p>Our Kingston team provides ongoing care to manage hot flashes, sleep disturbances, mood changes, and other menopausal symptoms while monitoring for long-term health considerations. Treatment is adjusted based on your response and evolving needs.</p>
            ''',
}

def get_procedure_name(filename):
    """Get readable procedure name from filename."""
    name = filename.replace('.html', '').replace('-', ' ').title()
    replacements = {'Prp': 'PRP', 'Iv': 'IV', 'O Shot': 'O-Shot', 'P Shot': 'P-Shot'}
    for old, new in replacements.items():
        name = name.replace(old, new)
    return name

def fix_how_it_works(filepath):
    """Replace generic How It Works content with procedure-specific info."""
    try:
        filename = os.path.basename(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to find the generic How It Works section
        pattern = r'(<section id="how-it-works" class="procedure-section section-alt fade-in-element">.*?<h2>How It Works & What To Expect</h2>)\s*<p>During your consultation at OSHUNJA in Kingston.*?</p>\s*<p>The treatment process is designed for your comfort.*?</p>\s*(</section>)'
        
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            # Check if we have specific content for this procedure
            if filename in HOW_IT_WORKS_CONTENT:
                new_content = match.group(1) + HOW_IT_WORKS_CONTENT[filename] + match.group(2)
            else:
                # Generate category-specific content
                procedure_name = get_procedure_name(filename)
                
                if 'pelvic-intimate' in filepath:
                    new_text = f'''
                <p>{procedure_name} at OSHUNJA is performed by our board-certified gynecological surgeon in a private, comfortable surgical suite in Kingston. The procedure begins with detailed consultation to understand your concerns and desired outcomes, followed by thorough examination and surgical planning.</p>
                <p>Surgery is typically performed under local anesthesia with sedation or general anesthesia based on procedure complexity. Our team ensures your comfort throughout the process and provides comprehensive post-operative care instructions for optimal healing and results.</p>
            '''
                elif 'pelvic-reproductive' in filepath:
                    new_text = f'''
                <p>{procedure_name} at OSHUNJA begins with consultation to review your medical history, symptoms, and diagnostic needs. Our experienced Kingston gynecologists use advanced techniques and equipment to ensure accurate results and patient comfort throughout the procedure.</p>
                <p>Depending on the specific procedure, you may receive local anesthesia, conscious sedation, or general anesthesia. We provide detailed pre- and post-procedure instructions and schedule appropriate follow-up care to address results and any ongoing treatment needs.</p>
            '''
                elif 'facial' in filepath:
                    new_text = f'''
                <p>{procedure_name} at OSHUNJA in Kingston combines medical expertise with aesthetic artistry. Your treatment begins with consultation to assess your facial structure, discuss goals, and create a customized plan. The procedure itself is performed with precision using advanced techniques for natural-looking results.</p>
                <p>Most treatments are quick with minimal discomfort and no downtime, allowing you to return to normal activities immediately. We provide detailed aftercare instructions and schedule follow-up appointments to ensure optimal results and your complete satisfaction.</p>
            '''
                else:
                    new_text = f'''
                <p>{procedure_name} at OSHUNJA in Kingston begins with comprehensive consultation to assess your needs and create a personalized treatment plan. Our medical team explains each step of the process, ensuring you feel informed and comfortable before proceeding.</p>
                <p>Treatment is performed using advanced techniques and equipment in our modern facility. We prioritize your comfort and safety throughout, providing detailed aftercare instructions and scheduling follow-up appointments to monitor your progress and results.</p>
            '''
                
                new_content = match.group(1) + new_text + match.group(2)
            
            content = content.replace(match.group(0), new_content)
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    base_dir = '/home/jmatthewlee/claude-test/pages/procedures'
    
    fixed_count = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                if fix_how_it_works(filepath):
                    rel_path = os.path.relpath(filepath, '/home/jmatthewlee/claude-test')
                    print(f'✓ {rel_path}')
                    fixed_count += 1
    
    print(f'\n✅ Fixed {fixed_count} pages with procedure-specific content')

if __name__ == '__main__':
    main()
