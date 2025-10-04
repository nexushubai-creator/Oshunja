filepath = 'pages/procedures/body/renuvion.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the malformed Overview section closing
content = content.replace(
    '''                <p>Our Kingston clinic combines this cutting-edge technology with expert surgical technique. As one of the few facilities in Jamaica offering Renuvion, we provide patients access to this FDA-cleared treatment that delivers surgical-quality results through tiny incisions, minimal scarring, and significantly faster recovery than traditional body lift procedures.</p>
            
            <!-- Treatment Areas Section -->''',
    '''                <p>Our Kingston clinic combines this cutting-edge technology with expert surgical technique. As one of the few facilities in Jamaica offering Renuvion, we provide patients access to this FDA-cleared treatment that delivers surgical-quality results through tiny incisions, minimal scarring, and significantly faster recovery than traditional body lift procedures.</p>
            </section>

            <!-- Treatment Areas Section -->'''
)

# Remove any literal \n characters that might have gotten inserted
content = content.replace('\\n\\n', '\n')
content = content.replace('\\n', '\n')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Fixed Overview section closing!')
