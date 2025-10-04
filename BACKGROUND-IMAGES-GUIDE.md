# Background Images for Procedure Pages

## Current Implementation
I've added elegant gradient and pattern backgrounds to all procedure page sections using CSS. These create visual interest without requiring external image files.

## Sections with Backgrounds

### 1. **Hero Section (Top of page)**
- Gradient background with subtle geometric patterns
- Brand colors: Primary gold → Dark gold gradient
- Overlay pattern for texture

### 2. **"How It Works & What To Expect" Section**
- Light beige background with subtle dot pattern
- Radial gradients for depth
- White cards for process steps stand out

### 3. **"Ideal Candidates & Considerations" Section**  
- Distinctive wavy pattern overlay
- Multiple gradient layers for sophistication
- Maintains readability with light colors

### 4. **"Complementary Treatments" Section**
- Diamond/checkered subtle pattern
- Inviting gradient overlays
- Encourages exploration of related services

## Adding Custom Background Images (Optional)

If you want to use actual photos instead of patterns, follow these steps:

### Step 1: Get Stock Images
**Recommended Sources:**
- **Unsplash** (https://unsplash.com) - Free, high-quality medical/spa images
- **Pexels** (https://pexels.com) - Free stock photos
- **Pixabay** (https://pixabay.com) - Free images and videos

**Search Terms:**
- "medical spa interior"
- "luxury wellness clinic"
- "aesthetic treatment room"
- "medical consultation"
- "spa treatment background"
- "clean medical aesthetic"

### Step 2: Download and Prepare Images
```bash
# Create background images directory
mkdir -p /home/jmatthewlee/claude-test/images/backgrounds

# Download images (use appropriate URLs)
cd /home/jmatthewlee/claude-test/images/backgrounds
wget https://images.unsplash.com/[photo-id] -O hero-bg.jpg
wget https://images.unsplash.com/[photo-id] -O process-bg.jpg
wget https://images.unsplash.com/[photo-id] -O candidates-bg.jpg
wget https://images.unsplash.com/[photo-id] -O complementary-bg.jpg
```

### Step 3: Optimize Images
```bash
# Install image optimization tool (if not already installed)
# sudo apt install imagemagick

# Resize and optimize (example for 1920px width)
convert hero-bg.jpg -resize 1920x -quality 85 hero-bg-optimized.jpg
```

### Step 4: Update CSS
Edit `css/styles.css` and modify the background sections:

**For Hero Section:**
```css
.procedure-hero {
  background: linear-gradient(135deg, rgba(164, 125, 82, 0.9) 0%, rgba(196, 154, 108, 0.85) 100%),
              url('../images/backgrounds/hero-bg.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* Parallax effect */
}
```

**For How It Works Section:**
```css
.procedure-section.section-alt::before {
  background: linear-gradient(rgba(250, 248, 245, 0.95), rgba(250, 248, 245, 0.95)),
              url('../images/backgrounds/process-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

**For Ideal Candidates Section:**
```css
.procedure-section.section-alt:has(.candidates-grid)::before {
  background: linear-gradient(rgba(250, 248, 245, 0.92), rgba(250, 248, 245, 0.92)),
              url('../images/backgrounds/candidates-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

**For Complementary Treatments Section:**
```css
.procedure-section.section-alt:has(.complementary-grid)::before {
  background: linear-gradient(rgba(250, 248, 245, 0.9), rgba(250, 248, 245, 0.9)),
              url('../images/backgrounds/complementary-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

## Image Specifications

**Recommended Sizes:**
- Hero: 1920x800px (landscape)
- Section backgrounds: 1920x1080px (landscape)

**Format:** JPG (best compression) or WebP (modern browsers)

**File Size:** Keep under 200KB per image (use compression)

**Style Guidelines:**
- Soft focus/blurred backgrounds work best
- Light, airy images (not too dark)
- Medical/spa aesthetic
- Professional but warm feeling
- Avoid busy images (text needs to be readable)

## Free Image Suggestions

### For Medical/Aesthetic Procedures:
1. **Hero**: Clean, modern clinic interior with natural light
2. **How It Works**: Consultation room or medical professional
3. **Ideal Candidates**: Peaceful spa/wellness setting
4. **Complementary**: Related treatment or wellness products

### Example Unsplash Searches:
```
site:unsplash.com medical spa
site:unsplash.com aesthetic clinic
site:unsplash.com wellness center
site:unsplash.com clean medical
```

## Current Status
✅ All sections have elegant CSS pattern backgrounds
✅ No external images required
✅ Fast page load times
✅ Fully responsive
⚠️ Optional: Can add photos later for more visual impact

## Notes
- Current CSS patterns are professional and don't require image downloads
- Patterns are scalable and work on all screen sizes
- No performance impact from loading images
- Can easily switch to photos later if desired
