# Image Assets for OSHUNJA Website

## Required Images

Place your optimized images in this directory. Below are the specifications for each required image.

---

## 🖼️ Core Images

### 1. Hero Background (`hero-bg.jpg`)
- **Dimensions:** 1920 x 1080px (minimum)
- **Format:** JPG (optimized for web)
- **File size:** < 300KB
- **Content:** Professional clinic interior, elegant medical setting, or abstract luxury aesthetic
- **Usage:** Homepage hero section background
- **Alternative names:** Can also be used for category backgrounds

### 2. Category Background (`category-bg.jpg`)
- **Dimensions:** 1920 x 600px
- **Format:** JPG
- **File size:** < 200KB
- **Content:** Medical/aesthetic setting, can be slightly blurred or overlayed
- **Usage:** Background for all category page hero sections

### 3. Open Graph Image (`og-image.jpg`)
- **Dimensions:** 1200 x 630px (Facebook/Twitter standard)
- **Format:** JPG
- **File size:** < 150KB
- **Content:** OSHUNJA logo + tagline + contact info (text overlay)
- **Usage:** Social media preview when website is shared

### 4. Clinic Logo (`logo.jpg` or `logo.png`)
- **Dimensions:** 500 x 500px (square) or transparent PNG
- **Format:** PNG (with transparency) or JPG
- **File size:** < 50KB
- **Content:** OSHUNJA clinic logo
- **Usage:** Can be used in various places if text logo is replaced with image

---

## 📸 Optional Procedure Images

For enhanced visual appeal, add procedure-specific images in subdirectories:

```
images/
├── facial/
│   ├── botox-before-after.jpg
│   ├── fillers-treatment.jpg
│   └── chemical-peel.jpg
├── body/
│   ├── coolsculpting.jpg
│   └── body-contouring.jpg
├── pelvic/
│   ├── consultation-room.jpg  (discreet medical setting)
│   └── private-care.jpg
├── wellness/
│   ├── iv-therapy.jpg
│   └── wellness-consultation.jpg
└── hair/
    ├── prp-hair.jpg
    └── hair-consultation.jpg
```

**Specifications for procedure images:**
- Dimensions: 800 x 600px (landscape) or 600 x 800px (portrait)
- Format: JPG
- File size: < 150KB each
- Content: Professional, medical-grade photography (avoid stock photos if possible)

---

## 🎨 Image Optimization Tips

### Before Upload:
1. **Resize** images to exact dimensions listed above
2. **Compress** using tools like TinyPNG, ImageOptim, or Squoosh
3. **Use** appropriate formats (JPG for photos, PNG for logos with transparency)
4. **Test** file sizes - keep them as small as possible without quality loss

### Recommended Tools:
- [TinyPNG](https://tinypng.com) - Online compression
- [Squoosh](https://squoosh.app) - Google's image optimizer
- [ImageOptim](https://imageoptim.com) - Mac app
- Adobe Photoshop - "Save for Web" feature

---

## 🖼️ Stock Photo Resources (if needed)

If you need temporary placeholder images or stock photos:

- **Pexels** - https://pexels.com (free, high-quality)
- **Unsplash** - https://unsplash.com (free, professional)
- **Adobe Stock** - https://stock.adobe.com (paid, medical-specific)
- **iStock** - https://istockphoto.com (paid, diverse medical images)

**Search terms:**
- "luxury medical clinic interior"
- "modern aesthetic clinic"
- "professional doctor consultation"
- "medical spa"
- "wellness center"
- "Jamaica medical facility" (for local context)

---

## ⚠️ Important Notes

### Medical Imagery Guidelines:
- **Always** obtain proper consent for before/after photos
- **Never** use patient photos without written permission
- **Comply** with medical privacy regulations (HIPAA-equivalent in Jamaica)
- **Consider** using illustrations or abstract imagery for sensitive procedures
- **Avoid** overly graphic medical images on public-facing website

### Copyright & Licensing:
- Ensure you have rights to use all images
- Keep records of image licenses
- Credit photographers when required
- Don't use images from competitors' websites

### Diversity & Representation:
- Use images representing diverse skin tones (important for Jamaica demographic)
- Show range of ages and body types
- Avoid stereotypical or unrealistic portrayals
- Reflect actual clientele when possible

---

## 📝 Alt Text Guidelines

When adding images to HTML, always include descriptive alt text:

```html
<!-- Good example -->
<img src="images/hero-bg.jpg" alt="Modern OSHUNJA clinic consultation room in Kingston, Jamaica with luxury furnishings">

<!-- Avoid generic alt text -->
<img src="images/hero-bg.jpg" alt="clinic">
```

**Alt text should:**
- Describe the image content clearly
- Include relevant keywords naturally (e.g., "Kingston Jamaica")
- Be concise (under 125 characters)
- Not start with "image of" or "picture of"

---

## ✅ Image Checklist

Before launching the website:

- [ ] `hero-bg.jpg` uploaded and optimized
- [ ] `category-bg.jpg` uploaded and optimized
- [ ] `og-image.jpg` created with branding
- [ ] Logo image prepared (if replacing text logo)
- [ ] All images compressed for web
- [ ] Alt text added to all `<img>` tags in HTML
- [ ] Before/after photos have patient consent forms
- [ ] Stock photo licenses documented
- [ ] Mobile versions tested (images load quickly)
- [ ] Image quality verified on retina displays

---

## 🔄 Future Enhancements

Consider adding:
- WebP format versions for better compression
- Lazy loading for below-the-fold images
- Responsive image sets (`srcset`) for different screen sizes
- Image CDN for faster global delivery
- Video backgrounds for hero section (if budget allows)

---

For questions about image requirements, contact the web development team.