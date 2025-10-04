filepath = 'pages/procedures/pelvic-reproductive/endometrial-ablation.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the FAQ section with relevant questions
old_faq = '''                <div class="faq-container">
                    

                    

                    

                    

                    <details class="faq-item fade-in-element">
                        <summary>Is the procedure safe for dark skin?</summary>
                        <p>Absolutely. Our surgeons have extensive experience treating patients of all skin tones, including melanin-rich Caribbean skin. We use techniques specifically tailored to optimize healing for darker skin types.</p>
                    </details>
                </div>'''

new_faq = '''                <div class="faq-container">
                    <details class="faq-item fade-in-element">
                        <summary>Will I still have periods after endometrial ablation?</summary>
                        <p>Results vary: 30-40% of women stop menstruating completely, 50-60% experience much lighter periods, and about 10% see minimal change. Most women report significant improvement in bleeding that dramatically enhances quality of life.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>Can I get pregnant after endometrial ablation?</summary>
                        <p>Pregnancy is not recommended after ablation. While the procedure is not considered permanent sterilization, the damaged uterine lining makes pregnancy unlikely and potentially dangerous. We recommend reliable contraception or consider tubal ligation if permanent sterilization is desired.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>How long does the procedure take?</summary>
                        <p>The ablation itself takes 15-30 minutes. Including preparation, anesthesia, and recovery time, expect to be at our Kingston facility for 2-4 hours total. You'll go home the same day with no overnight stay required.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>Does endometrial ablation hurt?</summary>
                        <p>The procedure is performed under conscious sedation or general anesthesia, so you won't feel pain during treatment. Afterward, expect cramping similar to period cramps for 1-3 days, easily managed with over-the-counter pain medication and heating pads.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>What if the ablation doesn't work for me?</summary>
                        <p>About 10-15% of women may need a repeat ablation if the endometrium regenerates. If heavy bleeding persists despite ablation, we'll explore other options including hormonal treatments or, as a last resort, hysterectomy. Most women achieve excellent results with the first procedure.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>Do I need to stay on birth control after ablation?</summary>
                        <p>Yes, reliable contraception is essential. While pregnancy is unlikely after ablation, it can occur and carries serious risks including miscarriage, preterm birth, and placental problems. Discuss birth control options with your Kingston gynecologist.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>When can I return to work and exercise?</summary>
                        <p>Most women return to desk work within 1-2 days. Avoid heavy lifting and strenuous exercise for 1-2 weeks. Sexual activity can resume after 2-3 weeks once your doctor confirms healing is complete during your follow-up visit.</p>
                    </details>

                    <details class="faq-item fade-in-element">
                        <summary>Will I go through menopause earlier after ablation?</summary>
                        <p>No, endometrial ablation doesn't affect your ovaries or hormone production. You'll experience menopause at the natural time for your body. However, without periods, you may not notice typical menopause symptoms related to cycle changes.</p>
                    </details>
                </div>'''

content = content.replace(old_faq, new_faq)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Added comprehensive FAQs!')
