import re

# Read the file
filepath = 'pages/procedures/pelvic-reproductive/endometrial-ablation.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Overview section - find the first procedure-section after hero
overview_old = '''            <section class="procedure-section fade-in-element">
                <h2>Overview</h2>
                <p>Endometrial Ablation at OSHUNJA provides comprehensive gynecological care in Kingston, Jamaica. Our experienced physicians offer advanced diagnostic and treatment procedures in a comfortable, modern facility.</p>
                <p>Women's health is our specialty. We combine clinical excellence with personalized care to address your gynecological concerns with the latest evidence-based techniques.</p>
                <p>From routine screenings to advanced procedures, we provide the full spectrum of gynecological care. Our Kingston team ensures you receive thorough, compassionate treatment at every visit.</p>
            </section>'''

overview_new = '''            <section class="procedure-section fade-in-element">
                <h2>Overview</h2>
                <p>Endometrial Ablation at OSHUNJA provides a minimally invasive solution for women suffering from heavy menstrual bleeding. Our Kingston gynecologists use advanced thermal and radiofrequency techniques to permanently destroy the uterine lining (endometrium), eliminating or significantly reducing monthly bleeding while preserving your uterus and avoiding hysterectomy.</p>
                <p>Many women with menorrhagia (excessive menstrual bleeding) experience anemia, fatigue, and lifestyle disruption from prolonged heavy periods. Endometrial ablation offers rapid relief, with most women experiencing dramatically lighter periods or complete cessation of menstruation. The procedure takes less than 30 minutes and requires minimal downtime compared to hysterectomy.</p>
                <p>Our experienced gynecological surgeons perform this outpatient procedure using state-of-the-art equipment in our modern Kingston facility. We combine clinical expertise with compassionate care, ensuring you understand every step and feel supported throughout your journey to freedom from heavy bleeding.</p>
            </section>'''

content = content.replace(overview_old, overview_new)

# Replace How It Works section
how_old = '''            <section id="how-it-works" class="procedure-section section-alt fade-in-element">
                <h2>How It Works & What To Expect</h2>
                <p>Endometrial Ablation at OSHUNJA begins with consultation to review your medical history, symptoms, and diagnostic needs. Our experienced Kingston gynecologists use advanced techniques and equipment to ensure accurate results and patient comfort throughout the procedure.</p>
                <p>Depending on the specific procedure, you may receive local anesthesia, conscious sedation, or general anesthesia. We provide detailed pre- and post-procedure instructions and schedule appropriate follow-up care to address results and any ongoing treatment needs.</p>
            </section>'''

how_new = '''            <section id="how-it-works" class="procedure-section section-alt fade-in-element">
                <h2>How It Works & What To Expect</h2>

                <div class="process-steps">
                    <div class="process-step fade-in-element">
                        <div class="step-number">1</div>
                        <h3>Comprehensive Evaluation</h3>
                        <p>Initial consultation includes medical history review, pelvic examination, and ultrasound to rule out other causes of heavy bleeding. We confirm you've completed childbearing and discuss alternatives before proceeding with ablation.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">2</div>
                        <h3>Pre-Procedure Preparation</h3>
                        <p>You may receive medication to thin the uterine lining before surgery. On procedure day, you arrive at our Kingston clinic having fasted as instructed. Conscious sedation or general anesthesia is administered based on technique and your comfort.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">3</div>
                        <h3>Ablation Procedure</h3>
                        <p>Using radiofrequency, heated balloon, or cryotherapy, we destroy the endometrial lining through your cervix—no incisions required. The entire process takes 15-30 minutes. Advanced technology ensures thorough treatment while protecting surrounding structures.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">4</div>
                        <h3>Recovery & Discharge</h3>
                        <p>You rest in recovery for 1-2 hours before going home the same day. Mild cramping and watery discharge are normal for several weeks. Most women return to work within 1-2 days and resume normal activities within a week.</p>
                    </div>
                </div>

                <div class="timeline-section">
                    <h3>Expected Results Timeline</h3>
                    <ul class="timeline-list">
                        <li><strong>Immediate:</strong> Procedure complete, mild cramping begins</li>
                        <li><strong>1-3 weeks:</strong> Watery or bloody discharge as lining sheds</li>
                        <li><strong>First cycle:</strong> Significantly lighter or absent period</li>
                        <li><strong>3-6 months:</strong> Final bleeding pattern established</li>
                        <li><strong>Long-term:</strong> 85-90% of women experience dramatically reduced bleeding; 30-40% stop menstruating completely</li>
                    </ul>
                </div>
            </section>'''

content = content.replace(how_old, how_new)

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Fixed endometrial ablation page!')
