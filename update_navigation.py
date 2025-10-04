#!/usr/bin/env python3
"""
Updates navigation bars across all HTML pages to match the homepage navigation structure.
"""

import os
import re
from pathlib import Path

# Define the new navigation HTML template (from homepage)
NEW_NAV_TEMPLATE = '''                <a href="{home_path}index.html" class="logo" aria-label="OSHUNJA Home">OSHUN<span style="color: var(--secondary-color);">JA</span></a>
                <ul class="nav-links" id="navLinks">
                    <li><a href="{home_path}index.html" aria-label="Home">Home</a></li>

                    <li class="dropdown">
                        <span class="nav-category">Facial Procedures</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/facial/botox.html">Botox</a></li>
                            <li><a href="{home_path}pages/procedures/facial/juvederm.html">Juvederm</a></li>
                            <li><a href="{home_path}pages/procedures/facial/prp-facial.html">PRP Facial</a></li>
                            <li><a href="{home_path}pages/procedures/facial/microneedling.html">Microneedling</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Hair & Scalp</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/hair/laser-hair-removal.html">Laser Hair Removal</a></li>
                            <li><a href="{home_path}pages/procedures/hair/prp-hair-restoration.html">Hair Restoration (PRP)</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Body Procedures</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/body/prp-breast-lift.html">PRP Breast Lift</a></li>
                            <li><a href="{home_path}pages/procedures/body/liposuction-360-180.html">Liposuction 360/180</a></li>
                            <li><a href="{home_path}pages/procedures/body/renuvion-abdomen.html">Renuvion - Abdomen</a></li>
                            <li><a href="{home_path}pages/procedures/body/renuvion-back.html">Renuvion - Back</a></li>
                            <li><a href="{home_path}pages/procedures/body/renuvion-neck.html">Renuvion - Neck</a></li>
                            <li><a href="{home_path}pages/procedures/body/renuvion-arms.html">Renuvion - Arms</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Pelvic & Intimate</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/labiaplasty.html">Labiaplasty</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/clitoral-hood-reduction.html">Clitoral Hood Reduction</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/perineoplasty.html">Perineoplasty</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/hymenoplasty.html">Hymenoplasty</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/vaginoplasty.html">Vaginoplasty</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/anal-skin-removal.html">Anal Skin Removal</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/labial-puff.html">Labial Puff</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Pelvic & Reproductive</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/annual-exam.html">Annual Exam</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/endometrial-ablation.html">Endometrial Ablation</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/hysteroscopy.html">Hysteroscopy</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/laparoscopy.html">Laparoscopy</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/myomectomy.html">Myomectomy</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/hysterectomy.html">Hysterectomy</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/thinprep-pap.html">ThinPrep Pap</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-reproductive/colposcopy.html">Colposcopy</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/vulvar-vaginal-cysts-warts.html">Vulvar/Vaginal Cysts & Warts</a></li>
                            <li><a href="{home_path}pages/procedures/pelvic-intimate/lichen-sclerosus-treatment.html">Lichen Sclerosus Treatment</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Sexual Health</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/sexual-health/o-shot.html">O-Shot</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/clit-shot.html">Clit Shot</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/p-shot.html">P-Shot</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/shockwave-therapy.html">Shockwave Therapy</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/bioidentical-hormones-women.html">Bioidentical Hormones (Women)</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/bioidentical-hormones-men.html">Bioidentical Hormones (Men)</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/menopause-management.html">Menopause Management</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/testosterone-optimization.html">Testosterone Optimization</a></li>
                            <li><a href="{home_path}pages/procedures/sexual-health/emsella-chair.html">Emsella Chair</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Wellness</span>
                        <ul class="dropdown-menu">
                            <li><a href="{home_path}pages/procedures/wellness/ozempic.html">Ozempic</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/mounjaro.html">Mounjaro</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/dietetics.html">Dietetics</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/metabolic-health-testing.html">Metabolic Health Testing</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/iv-therapy.html">IV Therapy</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/wellness-coaching.html">Wellness Coaching</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/sauna.html">Sauna</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/cold-plunge.html">Cold Plunge</a></li>
                            <li><a href="{home_path}pages/procedures/wellness/salt-blocks.html">Salt Blocks</a></li>
                        </ul>
                    </li>

                    <li><a href="https://wa.me/18764422327" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">💬</a></li>
                    <li><a href="#" class="btn btn-virtual-consult virtual-consult-trigger" aria-label="Virtual Consultation">Virtual Consultation</a></li>
                    <li><a href="{home_path}pages/contact.html" class="btn btn-primary" aria-label="Book Consultation">Book Consultation</a></li>
                </ul>
                <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle mobile menu" aria-expanded="false">
                    ☰
                </button>'''


def calculate_relative_path(file_path, base_dir):
    """Calculate relative path from file to base directory."""
    file_dir = os.path.dirname(file_path)
    rel_path = os.path.relpath(base_dir, file_dir)
    if rel_path == '.':
        return ''
    return rel_path + '/'


def update_navigation_in_file(file_path, base_dir):
    """Update navigation bar in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Calculate relative path for this file
        home_path = calculate_relative_path(file_path, base_dir)
        
        # Insert the home_path into the template
        new_nav = NEW_NAV_TEMPLATE.format(home_path=home_path)
        
        # Pattern to match the entire <nav> content
        # Match from <nav> opening tag to its closing </nav> tag
        pattern = r'(<nav>\s*).*?(\s*</nav>)'
        
        # Replace with new navigation
        updated_content = re.sub(
            pattern,
            r'\1' + new_nav + r'\2',
            content,
            flags=re.DOTALL
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def main():
    base_dir = '/home/jmatthewlee/claude-test'
    
    # Find all HTML files except index.html
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to update")
    
    success_count = 0
    for file_path in html_files:
        rel_path = os.path.relpath(file_path, base_dir)
        if update_navigation_in_file(file_path, base_dir):
            success_count += 1
            print(f"✓ Updated: {rel_path}")
        else:
            print(f"✗ Failed: {rel_path}")
    
    print(f"\n{'='*60}")
    print(f"Successfully updated {success_count}/{len(html_files)} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
