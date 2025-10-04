import re

filepath = 'pages/procedures/body/renuvion.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update title and meta tags
content = content.replace(
    '<title>Renuvion Abdomen Kingston Jamaica | Skin Tightening Treatment | OSHUNJA</title>',
    '<title>Renuvion Skin Tightening Kingston Jamaica | Non-Surgical Body Contouring | OSHUNJA</title>'
)

content = content.replace(
    '<meta name="description" content="Advanced Renuvion skin tightening for abdomen in Kingston, Jamaica. Non-surgical body contouring with helium plasma technology at OSHUNJA.">',
    '<meta name="description" content="Advanced Renuvion skin tightening for face, neck, arms, abdomen, and back in Kingston, Jamaica. Revolutionary helium plasma technology for non-surgical body contouring at OSHUNJA.">'
)

content = content.replace(
    '<meta property="og:title" content="Renuvion Abdomen Skin Tightening Kingston Jamaica | OSHUNJA">',
    '<meta property="og:title" content="Renuvion Skin Tightening Kingston Jamaica | OSHUNJA">'
)

content = content.replace(
    '<meta property="og:description" content="Tighten loose abdominal skin without surgery in Kingston, Jamaica using revolutionary plasma technology.">',
    '<meta property="og:description" content="Tighten loose skin on multiple body areas without surgery in Kingston, Jamaica using revolutionary helium plasma technology.">'
)

# Update H1
content = re.sub(
    r'<h1>Renuvion - Abdomen</h1>',
    '<h1>Renuvion Skin Tightening</h1>',
    content
)

content = re.sub(
    r'<p class="hero-subtitle">.*?renuvion.*?abdomen.*?</p>',
    '<p class="hero-subtitle">Revolutionary helium plasma skin tightening for face, neck, arms, abdomen, and back in Kingston, Jamaica</p>',
    content,
    flags=re.IGNORECASE
)

# Update Overview section
overview_old = re.search(
    r'(<section class="procedure-section fade-in-element">\s*<h2>Overview</h2>)(.*?)(</section>)',
    content,
    re.DOTALL
)

if overview_old:
    overview_new = '''\\1
                <p>Renuvion at OSHUNJA delivers revolutionary skin tightening using advanced helium plasma technology combined with radiofrequency energy. This minimally invasive procedure tightens loose, sagging skin on multiple body areas—including abdomen, arms, back, neck, and face—providing dramatic results without the extensive downtime of traditional surgery.</p>
                <p>Whether addressing post-weight loss skin laxity, aging-related sagging, or stubborn areas that don't respond to diet and exercise, Renuvion stimulates immediate collagen contraction and long-term collagen regeneration. The subdermal application of controlled thermal energy creates precise, uniform skin tightening that continues improving for months after your single treatment session.</p>
                <p>Our Kingston clinic combines this cutting-edge technology with expert surgical technique. As one of the few facilities in Jamaica offering Renuvion, we provide patients access to this FDA-cleared treatment that delivers surgical-quality results through tiny incisions, minimal scarring, and significantly faster recovery than traditional body lift procedures.</p>
            \\3'''
    
    content = re.sub(
        r'(<section class="procedure-section fade-in-element">\s*<h2>Overview</h2>)(.*?)(</section>)',
        overview_new,
        content,
        flags=re.DOTALL,
        count=1
    )

# Add Treatment Areas section after Overview
treatment_areas = '''
            <!-- Treatment Areas Section -->
            <section class="procedure-section section-alt fade-in-element">
                <h2>Treatment Areas</h2>
                <p>Renuvion effectively tightens loose skin across multiple body zones. Here are the most popular treatment areas:</p>

                <div class="treatment-areas-grid">
                    <div class="treatment-area-card fade-in-element">
                        <h3>🌟 Abdomen</h3>
                        <p><strong>Best for:</strong> Post-pregnancy skin laxity, weight loss aftermath, stubborn belly pouch</p>
                        <p><strong>Results:</strong> Dramatic tightening of abdominal wall, reduced stretch marks appearance, defined waistline</p>
                        <p><strong>Often combined with:</strong> Liposuction for complete abdominal transformation</p>
                    </div>

                    <div class="treatment-area-card fade-in-element">
                        <h3>💪 Arms (Brachial)</h3>
                        <p><strong>Best for:</strong> "Bat wings," loose upper arm skin, post-weight loss sagging</p>
                        <p><strong>Results:</strong> Firmer, more toned-appearing arms without brachioplasty scars</p>
                        <p><strong>Recovery advantage:</strong> Return to arm movement within days vs. weeks with surgery</p>
                    </div>

                    <div class="treatment-area-card fade-in-element">
                        <h3>🔄 Back & Bra Line</h3>
                        <p><strong>Best for:</strong> Bra bulge, back rolls, loose skin across upper/lower back</p>
                        <p><strong>Results:</strong> Smooth back contour, eliminated bulging, improved posture appearance</p>
                        <p><strong>Popular combination:</strong> 360 liposuction with Renuvion for complete torso transformation</p>
                    </div>

                    <div class="treatment-area-card fade-in-element">
                        <h3>👔 Neck & Jawline</h3>
                        <p><strong>Best for:</strong> Turkey neck, jowls, double chin, aging neck bands</p>
                        <p><strong>Results:</strong> Defined jawline, smooth neck contour, youthful profile restoration</p>
                        <p><strong>Alternative to:</strong> Neck lift surgery with dramatically reduced downtime</p>
                    </div>

                    <div class="treatment-area-card fade-in-element">
                        <h3>🦵 Thighs (Inner/Outer)</h3>
                        <p><strong>Best for:</strong> Inner thigh laxity, outer thigh dimpling, cellulite appearance</p>
                        <p><strong>Results:</strong> Firmer thigh contour, reduced skin crepiness, smoother texture</p>
                        <p><strong>Note:</strong> Best results when combined with targeted liposuction</p>
                    </div>

                    <div class="treatment-area-card fade-in-element">
                        <h3>✨ Multiple Areas</h3>
                        <p><strong>Comprehensive transformation:</strong> Renuvion can treat multiple zones in one surgical session</p>
                        <p><strong>Popular packages:</strong> Mommy makeover enhancement, post-bariatric body contouring, complete body refresh</p>
                        <p><strong>Efficiency:</strong> Treat 3-4 areas in single procedure for maximum impact</p>
                    </div>
                </div>

                <div class="info-box">
                    <h4>💡 Which Areas Should You Treat?</h4>
                    <p>During your Kingston consultation, we'll assess your skin quality, laxity degree, and aesthetic goals to recommend the optimal treatment zones. Many patients achieve their best results by combining Renuvion with liposuction—removing unwanted fat while simultaneously tightening the skin for smooth, contoured results.</p>
                </div>
            </section>
'''

# Insert treatment areas after the first </section> (after Overview)
content = re.sub(
    r'(</section>\s*\n\s*<!-- How It Works)',
    treatment_areas + r'\\n\\n            <!-- How It Works',
    content,
    count=1
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Created combined Renuvion page!')
