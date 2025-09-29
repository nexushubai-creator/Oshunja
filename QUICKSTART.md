# 🚀 OSHUNJA Website - Quick Start Guide

## Get Your Website Live in 5 Steps

---

## Step 1: Update Contact Information (5 minutes)

Search and replace these placeholders throughout all files:

### Phone Number
- **Find:** `+1876XXXXXXX` or `1876XXXXXXX`
- **Replace with:** Your actual phone number (format: `18765551234`)

### Address
- **Find:** `Your Street Address`
- **Replace with:** Your actual clinic address

### Email (if different)
- **Find:** `info@oshunja.com`
- **Replace with:** Your actual email address

### Social Media
- **Find:** `https://instagram.com/oshunja`
- **Replace with:** Your actual Instagram URL
- **Find:** WhatsApp number in all `https://wa.me/` links

**Quick Tip:** Use Find & Replace in your code editor (Ctrl+Shift+F or Cmd+Shift+F)

---

## Step 2: Add Images (10 minutes)

Place these images in the `/images` folder:

1. **hero-bg.jpg** - Homepage hero background (1920x1080px)
2. **category-bg.jpg** - Category page background (1920x600px)
3. **og-image.jpg** - Social sharing preview (1200x630px)

**Optional:** Add procedure-specific images to enhance visual appeal

📖 See `/images/README.md` for detailed specifications

---

## Step 3: Test Locally (2 minutes)

### Option A: Simple Python Server
```bash
cd /path/to/claude-test
python3 -m http.server 8000
```
Then open: http://localhost:8000

### Option B: VS Code Live Server
1. Install "Live Server" extension in VS Code
2. Right-click `index.html`
3. Select "Open with Live Server"

### What to Test:
- ✅ Navigation menu (mobile & desktop)
- ✅ All internal links work
- ✅ Contact form validation
- ✅ Testimonials slider auto-plays
- ✅ FAQ accordions expand/collapse
- ✅ Mobile responsiveness

---

## Step 4: Backend Integration (15-30 minutes)

### Contact Form Setup

**Option A: Simple EmailJS Integration (No backend needed)**

1. Sign up at [EmailJS](https://www.emailjs.com)
2. Get your Service ID, Template ID, and Public Key
3. Add to bottom of `contact.html` before `</body>`:
```html
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script>
    emailjs.init("YOUR_PUBLIC_KEY");
</script>
```

4. Replace the `handleFormSubmission()` function in `js/main.js` (line ~145) with:
```javascript
function handleFormSubmission(formData) {
    const submitButton = document.querySelector('#contactForm button[type="submit"]');
    submitButton.textContent = 'Submitting...';
    submitButton.disabled = true;

    emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {
        from_name: formData.name,
        from_email: formData.email,
        phone: formData.phone,
        procedure: formData.procedure,
        date: formData.appointmentDate,
        message: formData.message
    })
    .then(() => {
        showFormMessage('Thank you! We\'ll contact you within 24 hours.', 'success');
        document.getElementById('contactForm').reset();
    })
    .catch(() => {
        showFormMessage('Error sending message. Please call us directly.', 'error');
    })
    .finally(() => {
        submitButton.textContent = 'Submit Consultation Request';
        submitButton.disabled = false;
    });
}
```

**Option B: Custom Backend**

If you have a backend API, update line ~165 in `js/main.js`:
```javascript
fetch('https://your-api.com/consultations', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
})
```

---

## Step 5: Deploy to Web (10 minutes)

### Option A: Netlify (Free & Easy)

1. Create account at [Netlify](https://www.netlify.com)
2. Drag and drop your `claude-test` folder
3. Your site is live! (You'll get a `yoursite.netlify.app` URL)
4. Add custom domain in settings if you own `oshunja.com`

### Option B: Traditional Web Hosting

1. Connect via FTP (FileZilla, Cyberduck, or cPanel File Manager)
2. Upload all files to `public_html` or `www` directory
3. Ensure `index.html` is in the root
4. Set file permissions (typically 644 for files, 755 for directories)

### Option C: GitHub Pages (Free)

1. Create GitHub repository
2. Upload files
3. Enable GitHub Pages in repository settings
4. Site will be at `username.github.io/repository-name`

---

## ✅ Post-Launch Checklist

### Immediate Actions:
- [ ] Test contact form submission and verify emails arrive
- [ ] Check all pages on mobile phone (real device, not just browser)
- [ ] Test WhatsApp button - does it open correctly?
- [ ] Verify phone number links work (call from mobile)
- [ ] Ensure all images load properly
- [ ] Check website on different browsers (Chrome, Safari, Firefox)

### First Week:
- [ ] Set up Google Analytics (track visitors)
- [ ] Submit sitemap to Google Search Console
- [ ] Create Google My Business listing
- [ ] Test page load speed (use PageSpeed Insights)
- [ ] Set up social media profiles (Instagram)
- [ ] Add SSL certificate (HTTPS) if not automatic

### First Month:
- [ ] Monitor form submissions - are inquiries coming in?
- [ ] Gather and add real client testimonials (replace placeholders)
- [ ] Take professional photos of clinic to replace stock images
- [ ] Add more procedure detail pages (currently has 2 examples)
- [ ] Create blog section for SEO (optional but recommended)
- [ ] Set up automated appointment reminders

---

## 🆘 Troubleshooting

### Images Not Showing?
- Check file paths are correct (case-sensitive)
- Ensure images are in `/images` folder
- Verify image file extensions match HTML (`.jpg` vs `.jpeg`)

### Form Not Working?
- Open browser console (F12) to see errors
- Check that EmailJS or backend API is configured
- Verify all form field `id` attributes match JavaScript

### Mobile Menu Not Opening?
- Ensure `js/main.js` is loading (check Network tab in DevTools)
- Clear browser cache
- Check for JavaScript errors in console

### Links to Procedure Pages Broken?
- Most procedure detail pages are placeholders (use botox.html as template)
- Create additional procedure pages by copying existing examples
- Update links in category pages to match actual file paths

---

## 📈 Next Steps (Optional Enhancements)

### Week 2-4:
1. **Add More Procedure Pages** - Create detail pages for all procedures listed
2. **Professional Photography** - Replace emoji icons with real images
3. **Patient Portal** - Add login for existing patients
4. **Online Booking** - Integrate Calendly or Acuity Scheduling
5. **Live Chat** - Add Tawk.to or Intercom widget

### Month 2-3:
1. **Content Marketing** - Start blog with skincare tips, procedure FAQs
2. **Video Content** - Add YouTube videos of facility tours, testimonials
3. **Before/After Gallery** - Create password-protected gallery (with consent)
4. **Email Newsletter** - Collect emails, send monthly wellness tips
5. **Paid Advertising** - Google Ads, Instagram Ads for local reach

---

## 📞 Need Help?

### Developer Resources:
- **HTML/CSS Help:** [MDN Web Docs](https://developer.mozilla.org)
- **JavaScript Issues:** [Stack Overflow](https://stackoverflow.com)
- **Responsive Design:** [CSS-Tricks](https://css-tricks.com)

### Hire Help:
- **Freelance Developers:** Upwork, Fiverr, Toptal
- **Local Agencies:** Kingston, Jamaica web design firms
- **Maintenance:** Consider monthly retainer for updates

---

## 🎉 Congratulations!

Your OSHUNJA website is ready to attract clients and grow your practice. Remember:

✨ **Update content regularly** - Fresh content improves SEO
🔒 **Keep forms secure** - Protect patient information
📱 **Mobile-first** - Most visitors will be on phones
⚡ **Speed matters** - Optimize images and code
💬 **Respond quickly** - Answer consultation requests within 24 hours

**Good luck with your launch!** 🚀

---

*Built with care for OSHUNJA - Where Medicine Meets Aesthetics*