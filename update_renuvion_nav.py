# First, update the renuvion.html page itself to have correct nav
filepath = 'pages/procedures/body/renuvion.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 4 separate renuvion links with one
old_nav = '''                            <li><a href="../../../pages/procedures/body/renuvion-abdomen.html">Renuvion - Abdomen</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-back.html">Renuvion - Back</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-neck.html">Renuvion - Neck</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-arms.html">Renuvion - Arms</a></li>'''

new_nav = '''                            <li><a href="../../../pages/procedures/body/renuvion.html">Renuvion Skin Tightening</a></li>'''

content = content.replace(old_nav, new_nav)

# Update body class
content = content.replace('class="renuvion-abdomen-page"', 'class="renuvion-page"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated renuvion.html navigation!')
