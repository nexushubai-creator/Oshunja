import re

filepath = 'pages/procedures/body/renuvion.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add background image to How It Works section
content = re.sub(
    r'<section id="how-it-works" class="procedure-section section-alt fade-in-element">',
    '<section id="how-it-works" class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url(\'../../../images/procedures/body/medical-procedure-preparation.jpg\'); background-size: cover; background-position: center; background-attachment: fixed;">',
    content
)

# Replace the How It Works content with Renuvion-specific content
old_how_it_works = '''                <div class="process-steps">
                    <div class="process-step fade-in-element">
                        <div class="step-number">1</div>
                        <h3>Consultation & Mapping</h3>
                        <p>Meet with our fellowship-trained surgeon to discuss your concerns, medical history, and desired outcomes. We'll map your torso individually, considering posture and body shape.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">2</div>
                        <h3>Pre-Operative Preparation</h3>
                        <p>Complete labs, arrange caregiver support, and follow pre-surgery nutrition guidelines. We'll provide detailed instructions about medications and what to bring on surgery day.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">3</div>
                        <h3>The Procedure</h3>
                        <p>Marked zones are numbed with tumescent anaesthetic that also constricts blood vessels. Micro-cannulas remove fat circumferentially around the torso to sculpt an hourglass or V-taper. Fat is feathered into adjacent zones for smooth transitions.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">4</div>
                        <h3>Recovery & Follow-Up</h3>
                        <p>You are placed in a custom compression garment and escorted to a private recovery lounge. Follow-up visits monitor progress at key healing milestones.</p>
                    </div>
                </div>

                <div class="info-box fade-in-element">
                    <h4>During The Procedure</h4>
                    <ul>
                        <li>Twilight sedation or general anaesthesia depending on the extent of contouring</li>
                        <li>Power-assisted cannulas and vibration technology minimise trauma</li>
                        <li>Incisions are closed with absorbable sutures or left to drain depending on treatment plan</li>
                        <li>Procedure takes 2.5 to 4 hours based on the number of zones treated</li>
                    </ul>
                </div>'''

new_how_it_works = '''                <div class="process-steps">
                    <div class="process-step fade-in-element">
                        <div class="step-number">1</div>
                        <h3>Comprehensive Consultation</h3>
                        <p>Meet with our Kingston surgeon to evaluate your skin laxity, discuss treatment areas, and set realistic expectations. We'll assess skin quality, determine if you're a good candidate, and create your personalized Renuvion treatment plan.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">2</div>
                        <h3>Pre-Procedure Preparation</h3>
                        <p>Arrive at our Kingston facility on procedure day. Anesthesia options (local with sedation or general) are reviewed. Treatment areas are marked and photographed for before/after comparison.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">3</div>
                        <h3>Renuvion Treatment</h3>
                        <p>Tiny incisions (3-5mm) are made in discreet locations. The Renuvion handpiece is inserted beneath the skin, delivering controlled helium plasma and RF energy. This heats subdermal tissue to precise temperatures, causing immediate collagen contraction. Multiple passes ensure uniform tightening across treatment zones.</p>
                    </div>

                    <div class="process-step fade-in-element">
                        <div class="step-number">4</div>
                        <h3>Immediate Recovery</h3>
                        <p>Incisions are closed with tiny sutures or skin glue. Compression garments are applied to treated areas. You rest in recovery for 1-2 hours before being discharged home the same day with detailed aftercare instructions.</p>
                    </div>
                </div>

                <div class="timeline-section">
                    <h3>Results Timeline</h3>
                    <ul class="timeline-list">
                        <li><strong>Immediately:</strong> Moderate swelling and bruising in treated areas</li>
                        <li><strong>1-2 weeks:</strong> Return to work and light activities, swelling subsiding</li>
                        <li><strong>4-6 weeks:</strong> Visible skin tightening becomes apparent, continue wearing compression</li>
                        <li><strong>3 months:</strong> Significant improvement visible as collagen remodeling progresses</li>
                        <li><strong>6-12 months:</strong> Final results revealed with maximum skin tightening and contouring</li>
                    </ul>
                </div>'''

content = content.replace(old_how_it_works, new_how_it_works)

# Add background images to Candidates and Complementary sections
content = re.sub(
    r'<section id="ideal-candidates" class="procedure-section section-alt fade-in-element">',
    '<section id="ideal-candidates" class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url(\'../../../images/procedures/body/body-consultation-medical.jpg\'); background-size: cover; background-position: center; background-attachment: fixed;">',
    content
)

# Find and add background to complementary section
content = re.sub(
    r'<!-- Complementary Treatments -->\s*<section class="procedure-section section-alt fade-in-element">',
    '<!-- Complementary Treatments -->\\n            <section class="procedure-section section-alt fade-in-element" style="background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.8)), url(\'../../../images/procedures/body/surgical-consultation.jpg\'); background-size: cover; background-position: center; background-attachment: fixed;">',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated Renuvion page with correct content and background images!')
