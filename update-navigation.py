#!/usr/bin/env python3
"""
Script to update navigation on all HTML pages to match the index.html navigation structure.
"""

import os
import re
from pathlib import Path

# Navigation HTML template (will be adjusted for path depth)
NAV_TEMPLATE = '''                <a href="{root}index.html" class="logo" aria-label="OSHUNJA Home">OSHUN<span style="color: var(--secondary-color);">JA</span></a>
                <ul class="nav-links" id="navLinks">
                    <li><a href="{root}index.html"{home_active} aria-label="Home">Home</a></li>

                    <li class="dropdown">
                        <span class="nav-category">Gynecology</span>
                        <ul class="dropdown-menu">
                            <li><a href="{root}pages/procedures/pelvic-intimate/labiaplasty.html">Labiaplasty</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/clitoral-hood-reduction.html">Clitoral Hood Reduction</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/perineoplasty.html">Perineoplasty</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/hymenoplasty.html">Hymenoplasty</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/vaginoplasty.html">Vaginoplasty</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/anal-skin-removal.html">Anal Skin Removal</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/labial-puff.html">Labial Puff</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/annual-exam.html">Annual Exam</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/endometrial-ablation.html">Endometrial Ablation</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/hysteroscopy.html">Hysteroscopy</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/laparoscopy.html">Laparoscopy</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/myomectomy.html">Myomectomy</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/hysterectomy.html">Hysterectomy</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/thinprep-pap.html">ThinPrep Pap</a></li>
                            <li><a href="{root}pages/procedures/pelvic-reproductive/colposcopy.html">Colposcopy</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/vulvar-vaginal-cysts-warts.html">Vulvar/Vaginal Cysts & Warts</a></li>
                            <li><a href="{root}pages/procedures/pelvic-intimate/lichen-sclerosus-treatment.html">Lichen Sclerosus Treatment</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Aesthetics</span>
                        <ul class="dropdown-menu">
                            <li><a href="{root}pages/procedures/facial/botox.html">Botox</a></li>
                            <li><a href="{root}pages/procedures/facial/juvederm.html">Juvederm</a></li>
                            <li><a href="{root}pages/procedures/facial/prp-facial.html">PRP Facial</a></li>
                            <li><a href="{root}pages/procedures/facial/microneedling.html">Microneedling</a></li>
                            <li><a href="{root}pages/procedures/hair/laser-hair-removal.html">Laser Hair Removal</a></li>
                            <li><a href="{root}pages/procedures/body/prp-breast-lift.html">PRP Breast Lift</a></li>
                            <li><a href="{root}pages/procedures/body/liposuction-360-180.html">Liposuction 360/180</a></li>
                            <li><a href="{root}pages/procedures/body/renuvion-abdomen.html">Renuvion - Abdomen</a></li>
                            <li><a href="{root}pages/procedures/body/renuvion-back.html">Renuvion - Back</a></li>
                            <li><a href="{root}pages/procedures/body/renuvion-neck.html">Renuvion - Neck</a></li>
                            <li><a href="{root}pages/procedures/body/renuvion-arms.html">Renuvion - Arms</a></li>
                            <li><a href="{root}pages/procedures/hair/prp-hair-restoration.html">Hair Restoration</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Wellness</span>
                        <ul class="dropdown-menu">
                            <li><a href="{root}pages/procedures/wellness/ozempic.html">Ozempic</a></li>
                            <li><a href="{root}pages/procedures/wellness/mounjaro.html">Mounjaro</a></li>
                            <li><a href="{root}pages/procedures/wellness/dietetics.html">Dietetics</a></li>
                            <li><a href="{root}pages/procedures/wellness/metabolic-health-testing.html">Metabolic Health Testing</a></li>
                            <li><a href="{root}pages/procedures/wellness/iv-therapy.html">IV Therapy</a></li>
                            <li><a href="{root}pages/procedures/wellness/wellness-coaching.html">Wellness Coaching</a></li>
                            <li><a href="{root}pages/procedures/wellness/sauna.html">Sauna</a></li>
                            <li><a href="{root}pages/procedures/wellness/cold-plunge.html">Cold Plunge</a></li>
                            <li><a href="{root}pages/procedures/wellness/salt-blocks.html">Salt Blocks</a></li>
                        </ul>
                    </li>

                    <li class="dropdown">
                        <span class="nav-category">Sexual Health</span>
                        <ul class="dropdown-menu">
                            <li><a href="{root}pages/procedures/sexual-health/o-shot.html">O-Shot</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/clit-shot.html">Clit Shot</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/p-shot.html">P-Shot</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/shockwave-therapy.html">Shockwave Therapy</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/bioidentical-hormones-women.html">Bioidentical Hormones (Women)</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/bioidentical-hormones-men.html">Bioidentical Hormones (Men)</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/menopause-management.html">Menopause Management</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/testosterone-optimization.html">Testosterone Optimization</a></li>
                            <li><a href="{root}pages/procedures/sexual-health/emsella-chair.html">Emsella Chair</a></li>
                        </ul>
                    </li>

                    <li><a href="{root}pages/contact.html" class="btn btn-primary" aria-label="Book Consultation">Book Consultation</a></li>
                </ul>
                <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle mobile menu" aria-expanded="false">
                    ☰
                </button>'''

def get_path_depth(file_path, base_dir):
    """Calculate how many levels deep the file is from base directory."""
    rel_path = os.path.relpath(file_path, base_dir)
    depth = len(Path(rel_path).parts) - 1
    return depth

def get_root_path(depth):
    """Get the relative path to root based on depth."""
    if depth == 0:
        return ""
    return "../" * depth

def update_html_file(file_path, base_dir):
    """Update a single HTML file with new navigation."""
    print(f"Updating: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Calculate path depth
        depth = get_path_depth(file_path, base_dir)
        root_path = get_root_path(depth)
        
        # Determine if this is the home page
        is_home = file_path.endswith('index.html') and depth == 0
        home_active = ' class="active"' if is_home else ''
        
        # Format navigation with correct paths
        new_nav = NAV_TEMPLATE.format(root=root_path, home_active=home_active)
        
        # Find and replace navigation section
        # Pattern to match from <nav> opening to </nav> closing
        nav_pattern = r'<nav>.*?</nav>'
        nav_replacement = f'<nav>\n{new_nav}\n            </nav>'
        
        updated_content = re.sub(nav_pattern, nav_replacement, content, flags=re.DOTALL)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"  Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files."""
    base_dir = '/home/jmatthewlee/claude-test'
    
    # Find all HTML files (excluding index.html as it's already correct)
    html_files = []
    
    # Add pages directory files
    pages_dir = os.path.join(base_dir, 'pages')
    if os.path.exists(pages_dir):
        for root, dirs, files in os.walk(pages_dir):
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to update")
    print("=" * 60)
    
    success_count = 0
    for html_file in html_files:
        if update_html_file(html_file, base_dir):
            success_count += 1
    
    print("=" * 60)
    print(f"Successfully updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()
