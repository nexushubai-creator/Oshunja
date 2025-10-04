filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update navigation dropdown
old_nav = '''                            <li><a href="pages/procedures/body/renuvion-abdomen.html">Renuvion - Abdomen</a></li>
                            <li><a href="pages/procedures/body/renuvion-back.html">Renuvion - Back</a></li>
                            <li><a href="pages/procedures/body/renuvion-neck.html">Renuvion - Neck</a></li>
                            <li><a href="pages/procedures/body/renuvion-arms.html">Renuvion - Arms</a></li>'''

new_nav = '''                            <li><a href="pages/procedures/body/renuvion.html">Renuvion Skin Tightening</a></li>'''

content = content.replace(old_nav, new_nav)

# Update body procedures section buttons
old_buttons = '''                            <a href="pages/procedures/body/renuvion-abdomen.html" class="btn procedure-btn" data-description="Skin tightening treatment for abdomen using Renuvion technology.">Renuvion - Abdomen</a>
                            <a href="pages/procedures/body/renuvion-back.html" class="btn procedure-btn" data-description="Skin tightening treatment for back.">Renuvion - Back</a>
                            <a href="pages/procedures/body/renuvion-neck.html" class="btn procedure-btn" data-description="Skin tightening treatment for neck and jawline.">Renuvion - Neck</a>
                            <a href="pages/procedures/body/renuvion-arms.html" class="btn procedure-btn" data-description="Skin tightening treatment for arms.">Renuvion - Arms</a>'''

new_buttons = '''                            <a href="pages/procedures/body/renuvion.html" class="btn procedure-btn" data-description="Revolutionary helium plasma skin tightening for multiple body areas.">Renuvion Skin Tightening</a>'''

content = content.replace(old_buttons, new_buttons)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated index.html!')
