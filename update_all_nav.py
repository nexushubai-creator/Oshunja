import os
import glob

# Find all HTML files in pages directory
html_files = glob.glob('pages/**/*.html', recursive=True)

old_nav_pattern = '''                            <li><a href="../../../pages/procedures/body/renuvion-abdomen.html">Renuvion - Abdomen</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-back.html">Renuvion - Back</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-neck.html">Renuvion - Neck</a></li>
                            <li><a href="../../../pages/procedures/body/renuvion-arms.html">Renuvion - Arms</a></li>'''

new_nav_pattern = '''                            <li><a href="../../../pages/procedures/body/renuvion.html">Renuvion Skin Tightening</a></li>'''

updated_files = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_nav_pattern in content:
            content = content.replace(old_nav_pattern, new_nav_pattern)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'✅ Updated: {filepath}')
            updated_files += 1
    except Exception as e:
        print(f'⚠️  Error with {filepath}: {e}')

print(f'\\n🎉 Updated {updated_files} files!')
