import re

filepath = 'pages/procedures/pelvic-reproductive/endometrial-ablation.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add background images to sections
content = re.sub(
    r'<section id="how-it-works" class="procedure-section section-alt fade-in-element">',
    '<section id="how-it-works" class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url(\'../../../images/procedures/face-neck-skin/medical-spa-facial-treatment.jpg\'); background-size: cover; background-position: center; background-attachment: fixed;">',
    content
)

content = re.sub(
    r'<section id="ideal-candidates" class="procedure-section section-alt fade-in-element">',
    '<section id="ideal-candidates" class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url(\'../../../images/procedures/face-neck-skin/aesthetic-procedure-consultation.jpg\'); background-size: cover; background-position: center; background-attachment: fixed;">',
    content
)

# Replace sparse Benefits section
old_benefits = '''            <section class="procedure-section fade-in-element">
                <h2>Benefits & Results</h2>
                <p>Endometrial ablation significantly reduces or eliminates heavy menstrual bleeding by destroying the uterine lining. This minimally invasive procedure provides relief from excessive bleeding, reduces need for hysterectomy, and improves quality of life.</p>
            </section>'''

new_benefits = '''            <section class="procedure-section fade-in-element">
                <h2>Benefits & Results</h2>
                
                <div class="benefits-grid">
                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">🩸</span>
                        <h3>Dramatically Reduced Bleeding</h3>
                        <p>85-90% of women experience significantly lighter periods or complete cessation of menstruation after endometrial ablation.</p>
                    </div>

                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">🏠</span>
                        <h3>Quick Outpatient Procedure</h3>
                        <p>Same-day discharge with most women returning to work within 1-2 days—no lengthy hospital stays required.</p>
                    </div>

                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">🚫</span>
                        <h3>Avoid Hysterectomy</h3>
                        <p>Preserve your uterus while eliminating heavy bleeding—a minimally invasive alternative to major surgery.</p>
                    </div>

                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">⚡</span>
                        <h3>No Incisions</h3>
                        <p>Procedure performed through your cervix with no external cuts—minimal scarring and faster healing.</p>
                    </div>

                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">💊</span>
                        <h3>Reduced Anemia</h3>
                        <p>Less bleeding means improved iron levels, energy, and overall health—no more chronic fatigue from blood loss.</p>
                    </div>

                    <div class="benefit-card fade-in-element">
                        <span class="benefit-icon">✨</span>
                        <h3>Improved Quality of Life</h3>
                        <p>Freedom from planning life around heavy periods—travel, exercise, and live without constant bleeding concerns.</p>
                    </div>
                </div>

                <div class="results-info">
                    <h3>What Results Can I Expect?</h3>
                    <ul>
                        <li><strong>30-40% of women</strong> stop having periods completely (amenorrhea)</li>
                        <li><strong>50-60% of women</strong> experience dramatically lighter periods</li>
                        <li><strong>90% satisfaction rate</strong> with significant improvement in quality of life</li>
                        <li><strong>Results are permanent</strong> for most women who've completed childbearing</li>
                        <li><strong>5-10% may need repeat procedure</strong> if endometrium regenerates over time</li>
                    </ul>
                </div>
            </section>'''

content = content.replace(old_benefits, new_benefits)

# Enhance Candidates section
old_candidates = '''            <section id="ideal-candidates" class="procedure-section section-alt fade-in-element">
                <h2>Ideal Candidates & Considerations</h2>
                <p>Ideal candidates for endometrial ablation are women with heavy menstrual bleeding who have completed childbearing. You should be in good health and have tried other treatments for heavy bleeding without success.</p>
                <p>During your consultation in Kingston, we'll evaluate your medical history, discuss your specific goals, and determine if this procedure is right for your individual situation.</p>
            </section>'''

new_candidates = '''            <section id="ideal-candidates" class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url('../../../images/procedures/face-neck-skin/aesthetic-procedure-consultation.jpg'); background-size: cover; background-position: center; background-attachment: fixed;">
                <h2>Ideal Candidates & Considerations</h2>
                
                <div class="candidates-section">
                    <h3>You're an Ideal Candidate If:</h3>
                    <ul class="ideal-list">
                        <li><strong>Heavy menstrual bleeding</strong> that interferes with daily activities and quality of life</li>
                        <li><strong>Completed childbearing</strong> and do not plan future pregnancies (pregnancy not recommended post-ablation)</li>
                        <li><strong>Failed medical management</strong> including hormonal treatments, IUDs, or other non-surgical options</li>
                        <li><strong>Want to avoid hysterectomy</strong> and prefer a less invasive alternative</li>
                        <li><strong>Normal uterine anatomy</strong> without fibroids larger than 3cm or significant abnormalities</li>
                        <li><strong>No desire to preserve fertility</strong> as pregnancy after ablation carries risks</li>
                    </ul>

                    <h3>⚠️ This Procedure May Not Be Right If:</h3>
                    <ul class="contraindications-list">
                        <li><strong>Planning future pregnancies:</strong> Ablation permanently affects the uterine lining needed for pregnancy</li>
                        <li><strong>Active pelvic infection:</strong> Must be treated before procedure</li>
                        <li><strong>Uterine or endometrial cancer:</strong> Requires different treatment approach</li>
                        <li><strong>Large fibroids:</strong> May need myomectomy or other treatment first</li>
                        <li><strong>Severe uterine abnormalities:</strong> Structural issues may prevent effective treatment</li>
                    </ul>

                    <div class="consultation-note">
                        <strong>During Your Kingston Consultation:</strong> We'll perform ultrasound, review your menstrual history, discuss alternative treatments, and determine if endometrial ablation is the best solution for your heavy bleeding.
                    </div>
                </div>
            </section>'''

content = content.replace(old_candidates, new_candidates)

# Enhance Recovery section  
old_recovery = '''            <section class="procedure-section fade-in-element">
                <h2>Recovery & Aftercare</h2>
                <p>Recovery varies by procedure and individual. Our Kingston team provides detailed aftercare instructions and is available for any questions or concerns during your recovery period.</p>
                <p>We schedule follow-up appointments to monitor your progress and ensure optimal results.</p>
            </section>'''

new_recovery = '''            <section class="procedure-section fade-in-element">
                <h2>Recovery & Aftercare</h2>
                
                <div class="recovery-timeline">
                    <div class="recovery-phase fade-in-element">
                        <h3>📅 First 24 Hours</h3>
                        <ul>
                            <li>Mild to moderate cramping (similar to period cramps)</li>
                            <li>Rest at home with prescribed pain medication</li>
                            <li>Light watery or bloody discharge begins</li>
                            <li>Apply heating pad for comfort</li>
                            <li>No tampons, douching, or sexual activity</li>
                        </ul>
                    </div>

                    <div class="recovery-phase fade-in-element">
                        <h3>📅 Days 2-7</h3>
                        <ul>
                            <li>Most women return to work within 1-2 days</li>
                            <li>Cramping diminishes significantly</li>
                            <li>Continued watery discharge (normal healing process)</li>
                            <li>Resume light activities and walking</li>
                            <li>Avoid heavy lifting or strenuous exercise</li>
                        </ul>
                    </div>

                    <div class="recovery-phase fade-in-element">
                        <h3>📅 Weeks 2-4</h3>
                        <ul>
                            <li>Discharge may continue for 2-4 weeks (this is normal)</li>
                            <li>Gradually resume normal exercise</li>
                            <li>Sexual activity can resume after 2-3 weeks (with doctor approval)</li>
                            <li>Follow-up appointment to assess healing</li>
                        </ul>
                    </div>

                    <div class="recovery-phase fade-in-element">
                        <h3>📅 Long-Term Care</h3>
                        <ul>
                            <li>First period may still be heavy as remaining tissue sheds</li>
                            <li>Significant improvement typically seen by second or third cycle</li>
                            <li>Continue routine gynecological exams and Pap smears</li>
                            <li>Report any unusual bleeding or pain to your Kingston doctor</li>
                        </ul>
                    </div>
                </div>

                <div class="warning-box">
                    <h4>⚠️ Contact Us Immediately If You Experience:</h4>
                    <ul>
                        <li>Severe abdominal pain not relieved by medication</li>
                        <li>Fever over 100.4°F (38°C)</li>
                        <li>Heavy bright red bleeding soaking through pads</li>
                        <li>Foul-smelling discharge (possible infection)</li>
                        <li>Difficulty urinating or severe pelvic pressure</li>
                    </ul>
                </div>
            </section>'''

content = content.replace(old_recovery, new_recovery)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Enhanced endometrial ablation page with detailed content and images!')
