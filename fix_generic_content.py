#!/usr/bin/env python3
"""
Script to fix generic content in procedure pages with procedure-specific content
"""

import os
import re
from pathlib import Path

# Dictionary mapping procedure names to their specific content
PROCEDURE_CONTENT = {
    # Pelvic & Intimate procedures
    'anal-skin-removal': {
        'benefits': "Anal skin removal (anal skin tag removal) eliminates uncomfortable skin tags that can cause irritation, hygiene difficulties, and self-consciousness. This minor procedure provides immediate relief from discomfort during sitting, cleansing, and intimate activities while improving confidence and comfort.",
        'candidates': "Ideal candidates for anal skin removal are adults experiencing discomfort, irritation, or aesthetic concerns from anal skin tags. You should be in good health, have realistic expectations, and be committed to proper post-procedure hygiene and care.",
        'complementary': "Anal skin removal can be combined with other intimate procedures like hemorrhoid treatment or perineoplasty for comprehensive anal and perineal wellness. Many patients benefit from our intimate health packages that address multiple concerns simultaneously."
    },
    'hymenoplasty': {
        'benefits': "Hymenoplasty (hymen reconstruction) is a delicate procedure that reconstructs the hymenal tissue for personal, cultural, or emotional reasons. This confidential procedure provides restored anatomy with natural appearance and function, addressing individual needs with complete privacy and understanding.",
        'candidates': "Ideal candidates for hymenoplasty are women seeking hymen reconstruction for personal reasons. You should be in good health, not currently sexually active or pregnant, and have realistic expectations about the procedure and healing process.",
        'complementary': "Hymenoplasty is often performed as a standalone procedure but can be combined with other intimate treatments like vaginoplasty or labiaplasty if comprehensive intimate restoration is desired."
    },
    'labial-puff': {
        'benefits': "Labial puff (fat transfer to labia) restores volume and youthful appearance to the labia majora using your own body fat. This natural enhancement improves labial fullness, reduces wrinkles and sagging, and enhances intimate confidence with long-lasting, natural-feeling results.",
        'candidates': "Ideal candidates for labial puff are women experiencing volume loss in the labia majora due to aging, childbirth, or genetics. You should be in good health, have realistic expectations, and have sufficient donor fat for the transfer procedure.",
        'complementary': "Labial puff pairs beautifully with labiaplasty for complete intimate rejuvenation. Many patients combine this with O-Shot treatments or other intimate wellness procedures for comprehensive enhancement."
    },
    'lichen-sclerosus-treatment': {
        'benefits': "Lichen sclerosus treatment provides relief from chronic itching, pain, and progressive tissue changes affecting intimate areas. Our comprehensive approach addresses symptoms, prevents progression, and restores comfort and function with both medical and aesthetic considerations.",
        'candidates': "Ideal candidates for lichen sclerosus treatment are women diagnosed with this autoimmune condition experiencing symptoms like itching, pain, or tissue changes. Treatment is appropriate for all stages of the condition with various therapeutic options available.",
        'complementary': "Lichen sclerosus treatment may be combined with intimate rejuvenation procedures once the condition is controlled. Our approach includes both medical management and aesthetic restoration as appropriate."
    },
    'lichen-sclerosus': {
        'benefits': "Lichen sclerosus management provides comprehensive care for this chronic condition affecting intimate tissues. Treatment reduces inflammation, prevents progression, relieves symptoms, and maintains intimate function and comfort through ongoing medical care.",
        'candidates': "Patients with lichen sclerosus benefit from ongoing medical management regardless of disease stage. Early treatment prevents progression while advanced cases can achieve symptom relief and functional improvement.",
        'complementary': "Lichen sclerosus care integrates with overall intimate health management. Once controlled, patients may consider additional treatments for aesthetic concerns or functional enhancement."
    },
    'vulvar-vaginal-cysts-warts': {
        'benefits': "Vulvar and vaginal cyst/wart removal eliminates uncomfortable growths causing pain, irritation, or aesthetic concerns. Treatment provides immediate relief, prevents complications, improves hygiene, and restores confidence in intimate situations.",
        'candidates': "Candidates for vulvar/vaginal cyst and wart treatment include women with symptomatic cysts or warts causing discomfort, aesthetic concerns, or functional issues. Treatment is appropriate for most patients regardless of age or cyst/wart type.",
        'complementary': "Cyst and wart removal can be combined with other intimate treatments for comprehensive care. Many patients benefit from follow-up treatments like intimate rejuvenation or preventive care protocols."
    },
    
    # Pelvic & Reproductive procedures
    'annual-exam': {
        'benefits': "Annual gynecological exams provide essential preventive care including cancer screening, infection detection, reproductive health assessment, and early intervention for potential issues. Regular exams are crucial for maintaining optimal gynecological health throughout your life.",
        'candidates': "All women should have annual gynecological exams starting at age 21 or within 3 years of becoming sexually active. Regular exams benefit women of all ages and health statuses for preventive care and early detection.",
        'complementary': "Annual exams often include additional screenings like STI testing, bone density assessments, or hormone evaluations. We can coordinate comprehensive women's health services during your visit."
    },
    'colposcopy': {
        'benefits': "Colposcopy provides detailed examination of the cervix, vagina, and vulva to investigate abnormal Pap smear results or symptoms. This diagnostic procedure enables early detection of precancerous changes and guides appropriate treatment decisions.",
        'candidates': "Colposcopy candidates include women with abnormal Pap results, unexplained bleeding, or visible cervical changes. Most women with irregular screening results benefit from this detailed examination for accurate diagnosis.",
        'complementary': "Colposcopy may be followed by cervical biopsies, LEEP procedures, or cryotherapy based on findings. We coordinate all necessary follow-up treatments for comprehensive cervical health care."
    },
    'endometrial-ablation': {
        'benefits': "Endometrial ablation significantly reduces or eliminates heavy menstrual bleeding by destroying the uterine lining. This minimally invasive procedure provides relief from excessive bleeding, reduces need for hysterectomy, and improves quality of life.",
        'candidates': "Ideal candidates for endometrial ablation are women with heavy menstrual bleeding who have completed childbearing. You should be in good health and have tried other treatments for heavy bleeding without success.",
        'complementary': "Endometrial ablation may be combined with other minimally invasive procedures like hysteroscopy or laparoscopy to address multiple gynecological concerns simultaneously."
    },
    'hysterectomy': {
        'benefits': "Hysterectomy provides definitive treatment for various gynecological conditions including fibroids, endometriosis, abnormal bleeding, or cancer. This procedure eliminates symptoms, prevents recurrence, and can be life-saving when medically indicated.",
        'candidates': "Hysterectomy candidates include women with severe gynecological conditions unresponsive to conservative treatment. You should have completed childbearing and understand the permanent nature of this procedure.",
        'complementary': "Hysterectomy may be combined with ovary removal, pelvic repair procedures, or other treatments based on individual medical needs. We coordinate comprehensive surgical care."
    },
    'hysteroscopy': {
        'benefits': "Hysteroscopy enables direct visualization and treatment of uterine conditions including polyps, fibroids, or abnormal bleeding. This minimally invasive procedure provides accurate diagnosis and often eliminates the need for more extensive surgery.",
        'candidates': "Hysteroscopy benefits women with abnormal uterine bleeding, suspected polyps or fibroids, infertility issues, or other uterine abnormalities. Most patients are candidates for this diagnostic and therapeutic procedure.",
        'complementary': "Hysteroscopy is often combined with endometrial ablation, polyp removal, or fibroid treatment. We can address multiple uterine issues during a single procedure when appropriate."
    },
    'laparoscopy': {
        'benefits': "Laparoscopy provides minimally invasive diagnosis and treatment of gynecological conditions with smaller incisions, faster recovery, and less pain than traditional surgery. This approach enables precise treatment while minimizing surgical trauma.",
        'candidates': "Laparoscopy candidates include women requiring gynecological surgery for conditions like endometriosis, ovarian cysts, or pelvic pain. Most patients benefit from this minimally invasive surgical approach.",
        'complementary': "Laparoscopic procedures can address multiple conditions simultaneously, including endometriosis treatment, cyst removal, or fertility enhancement procedures during a single surgery."
    },
    'myomectomy': {
        'benefits': "Myomectomy removes uterine fibroids while preserving the uterus, maintaining fertility potential. This procedure relieves symptoms like heavy bleeding, pelvic pressure, and pain while allowing future pregnancy possibilities.",
        'candidates': "Ideal myomectomy candidates are women with symptomatic fibroids who wish to preserve fertility or the uterus. You should be in good health and understand the potential for fibroid recurrence.",
        'complementary': "Myomectomy may be combined with other fertility-preserving procedures or simultaneous treatment of endometriosis or other pelvic conditions for comprehensive care."
    },
    'thinprep-pap': {
        'benefits': "ThinPrep Pap smears provide superior cervical cancer screening with reduced inadequate samples and improved detection of abnormal cells. This advanced technique offers more accurate results than conventional Pap tests.",
        'candidates': "All women requiring cervical cancer screening benefit from ThinPrep Pap tests. This improved technique is especially valuable for women with previous inadequate samples or high-risk factors.",
        'complementary': "ThinPrep Pap testing is often combined with HPV testing, STI screening, or comprehensive annual exams for complete gynecological health assessment."
    },
    
    # Sexual Health procedures
    'bioidentical-hormones-men': {
        'benefits': "Bioidentical hormone therapy for men restores optimal testosterone and hormone levels, improving energy, libido, muscle mass, mood, and overall vitality. This personalized treatment addresses age-related hormone decline with natural, body-identical hormones.",
        'candidates': "Ideal candidates for male bioidentical hormone therapy are men experiencing symptoms of low testosterone including fatigue, decreased libido, mood changes, or reduced muscle mass. You should be in good health and committed to ongoing monitoring.",
        'complementary': "Male hormone therapy pairs well with P-Shot treatments, testosterone optimization protocols, and comprehensive men's wellness programs for complete hormonal and sexual health enhancement."
    },
    'bioidentical-hormones-women': {
        'benefits': "Bioidentical hormone therapy for women alleviates menopausal symptoms, restores hormonal balance, improves mood and energy, and supports overall wellness. This personalized treatment uses natural, body-identical hormones for optimal results.",
        'candidates': "Ideal candidates for female bioidentical hormone therapy are women experiencing menopausal symptoms, hormone imbalances, or age-related hormonal changes. You should be committed to ongoing monitoring and follow-up care.",
        'complementary': "Female hormone therapy integrates beautifully with O-Shot treatments, menopause management protocols, and comprehensive women's wellness programs for complete hormonal health."
    },
    'clit-shot': {
        'benefits': "The Clit Shot (clitoral PRP injection) enhances sensitivity, improves sexual response, and increases pleasure using your body's own growth factors. This innovative treatment can restore intimacy and sexual confidence with natural, long-lasting results.",
        'candidates': "Ideal candidates for the Clit Shot are women experiencing decreased sensitivity, difficulty reaching climax, or reduced sexual satisfaction. You should be in good health and have realistic expectations about intimate enhancement.",
        'complementary': "The Clit Shot pairs perfectly with O-Shot treatments, bioidentical hormone therapy, or other intimate wellness procedures for comprehensive sexual health enhancement."
    },
    'emsella-chair': {
        'benefits': "Emsella Chair treatment strengthens pelvic floor muscles, reduces incontinence, improves sexual function, and enhances intimate wellness using electromagnetic technology. This non-invasive treatment requires no downtime while providing significant improvements.",
        'candidates': "Ideal candidates for Emsella Chair treatment are women experiencing pelvic floor weakness, incontinence, or reduced sexual satisfaction. This treatment benefits women of all ages seeking pelvic floor strengthening.",
        'complementary': "Emsella Chair treatment combines excellently with O-Shot procedures, hormone therapy, or other intimate wellness treatments for comprehensive pelvic health enhancement."
    },
    'menopause-management': {
        'benefits': "Comprehensive menopause management addresses hot flashes, mood changes, sleep disturbances, and other menopausal symptoms through personalized treatment plans. Our approach improves quality of life and supports healthy aging.",
        'candidates': "Women experiencing menopausal symptoms, perimenopause, or post-menopausal concerns benefit from comprehensive management. Treatment options are available for women at all stages of menopause.",
        'complementary': "Menopause management often includes bioidentical hormone therapy, nutritional counseling, and intimate wellness treatments for complete menopausal health support."
    },
    'o-shot': {
        'benefits': "The O-Shot (Orgasm Shot) enhances sexual function, increases sensitivity, improves lubrication, and can help with urinary incontinence using platelet-rich plasma. This natural treatment rejuvenates intimate tissues for improved sexual wellness.",
        'candidates': "Ideal candidates for the O-Shot are women experiencing decreased sexual satisfaction, urinary incontinence, or intimate tissue changes. You should be in good health and seeking natural intimate enhancement.",
        'complementary': "The O-Shot combines beautifully with hormone therapy, Emsella Chair treatments, or intimate surgical procedures for comprehensive sexual wellness enhancement."
    },
    'p-shot': {
        'benefits': "The P-Shot (Priapus Shot) enhances male sexual function, improves erection quality, increases size and sensitivity, and addresses erectile dysfunction using platelet-rich plasma. This natural treatment promotes intimate wellness and confidence.",
        'candidates': "Ideal candidates for the P-Shot are men experiencing erectile dysfunction, reduced sensitivity, or seeking enhancement of sexual function. You should be in good health and have realistic expectations.",
        'complementary': "The P-Shot pairs excellently with hormone therapy, shockwave therapy, or comprehensive men's wellness programs for complete sexual health optimization."
    },
    'shockwave-therapy': {
        'benefits': "Shockwave therapy for sexual health improves blood flow, enhances sensitivity, and can address erectile dysfunction through non-invasive acoustic waves. This treatment promotes natural healing and improved sexual function.",
        'candidates': "Candidates for sexual health shockwave therapy include men with erectile dysfunction, reduced sensitivity, or seeking enhanced sexual performance. This treatment benefits most men seeking non-invasive sexual wellness.",
        'complementary': "Shockwave therapy combines well with P-Shot treatments, hormone optimization, or comprehensive sexual wellness programs for enhanced results."
    },
    'testosterone-optimization': {
        'benefits': "Testosterone optimization restores healthy hormone levels, improves energy, enhances libido, increases muscle mass, and supports overall male vitality through personalized hormone protocols and lifestyle optimization.",
        'candidates': "Men experiencing low testosterone symptoms including fatigue, decreased libido, mood changes, or reduced performance benefit from optimization protocols. Comprehensive evaluation determines the best approach.",
        'complementary': "Testosterone optimization integrates with P-Shot treatments, nutritional counseling, and comprehensive men's health programs for complete vitality enhancement."
    },
    
    # Wellness procedures
    'cold-plunge': {
        'benefits': "Cold plunge therapy enhances recovery, reduces inflammation, boosts metabolism, improves circulation, and supports mental resilience through controlled cold exposure. This wellness treatment provides numerous health and performance benefits.",
        'candidates': "Cold plunge therapy benefits most healthy adults seeking enhanced recovery, improved circulation, or stress resilience. You should be in good cardiovascular health and able to tolerate cold exposure.",
        'complementary': "Cold plunge therapy pairs excellently with sauna treatments, IV therapy, or comprehensive wellness programs for complete recovery and health optimization."
    },
    'salt-blocks': {
        'benefits': "Salt block therapy (halotherapy) improves respiratory function, reduces inflammation, enhances skin health, and promotes relaxation through natural salt exposure. This wellness treatment supports respiratory and overall health.",
        'candidates': "Salt block therapy benefits individuals with respiratory concerns, skin conditions, or those seeking natural wellness enhancement. This gentle treatment is suitable for most ages and health conditions.",
        'complementary': "Salt block therapy combines well with sauna treatments, cold plunge therapy, or comprehensive wellness programs for holistic health enhancement."
    }
}

def fix_generic_content_in_file(file_path):
    """Fix generic content in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract procedure name from file path
        procedure_name = Path(file_path).stem
        
        if procedure_name not in PROCEDURE_CONTENT:
            print(f"No specific content defined for {procedure_name}, skipping...")
            return False
        
        original_content = content
        
        # Fix generic benefits section
        generic_benefits_pattern = r'(<p>This procedure provides (?:meaningful benefits for your health and wellness goals|significant benefits for comfort, confidence, and quality of life)\. Our Kingston team (?:will discuss expected outcomes during your personalized consultation|ensures you understand all potential benefits during your consultation)\.</p>)'
        
        if re.search(generic_benefits_pattern, content):
            content = re.sub(
                generic_benefits_pattern,
                f'<p>{PROCEDURE_CONTENT[procedure_name]["benefits"]}</p>',
                content
            )
        
        # Fix generic candidates section
        generic_candidates_pattern = r'(<p>Good candidates for this procedure are in good overall health, have realistic expectations, and are seeking to address specific concerns related to this treatment area\.</p>\s*<p>During your consultation in Kingston, we\'ll evaluate your medical history, discuss your goals, and determine if this procedure is right for you\.</p>)'
        
        if re.search(generic_candidates_pattern, content):
            replacement = f'''<p>{PROCEDURE_CONTENT[procedure_name]["candidates"]}</p>
                <p>During your consultation in Kingston, we'll evaluate your medical history, discuss your specific goals, and determine if this procedure is right for your individual situation.</p>'''
            content = re.sub(
                generic_candidates_pattern,
                replacement,
                content
            )
        
        # Fix generic complementary treatments section
        generic_complementary_pattern = r'(<p>This procedure can be combined with other treatments for comprehensive results\. During your consultation, we\'ll discuss complementary options that align with your goals\.</p>)'
        
        if re.search(generic_complementary_pattern, content):
            content = re.sub(
                generic_complementary_pattern,
                f'<p>{PROCEDURE_CONTENT[procedure_name]["complementary"]}</p>',
                content
            )
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed generic content in {procedure_name}.html")
            return True
        else:
            print(f"No generic content found in {procedure_name}.html")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all procedure files"""
    base_dir = Path("pages/procedures")
    fixed_count = 0
    
    # Get all HTML files in procedures directory
    html_files = list(base_dir.rglob("*.html"))
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    for file_path in html_files:
        if fix_generic_content_in_file(file_path):
            fixed_count += 1
    
    print(f"\nCompleted! Fixed generic content in {fixed_count} files.")

if __name__ == "__main__":
    main()