# Procedure Page Conversion Instructions

## 📊 STATUS

- ✅ **Completed:** 4 files
- 📋 **Remaining:** 46 files (organized into 7 batches)
- ⚙️ **Automation:** Batch conversion script created!

---

## 🚀 QUICK START

### Option 1: Automated Batch Conversion (Recommended)

**File Location:** `BATCH-CONVERSION-PROMPTS.md`

1. Open `BATCH-CONVERSION-PROMPTS.md`
2. Copy the **BATCH 1** prompt
3. Start a **new Claude Code session**
4. Paste the prompt
5. Claude converts those 3 files automatically
6. Repeat for BATCH 2-7

**Time:** ~15 minutes per batch, ~2 hours total for all 7 batches

---

### Option 2: Manual Conversion Script

**File Location:** `batch-convert-procedures.sh`

```bash
./batch-convert-procedures.sh
```

This shows you all files that need conversion organized by category.

---

## 📁 FILES CREATED

1. **`BATCH-CONVERSION-PROMPTS.md`** - Copy-paste prompts for each batch
2. **`batch-convert-procedures.sh`** - Shell script to list all files
3. **`conversion.log`** - Log file tracking conversion status
4. **`CONVERSION-STATUS.md`** - Current status tracker

---

## 📝 BATCH OVERVIEW

| Batch | Category | Files | Est. Time |
|-------|----------|-------|-----------|
| 1 | Facial | 3 | 15 min |
| 2 | Body | 7 | 20 min |
| 3 | Hair | 2 | 10 min |
| 4 | Pelvic-Intimate | 8 | 20 min |
| 5 | Pelvic-Reproductive | 8 | 20 min |
| 6 | Sexual-Health | 9 | 25 min |
| 7 | Wellness | 9 | 25 min |
| **TOTAL** | | **46** | **~2 hours** |

---

## ✅ WHAT'S ALREADY DONE

1. ✅ Homepage enhanced with larger buttons
2. ✅ Font sizes increased site-wide
3. ✅ Botox page converted to labiaplasty layout
4. ✅ Juvederm page converted
5. ✅ Microneedling page converted
6. ✅ Netlify deployment configured
7. ✅ Batch conversion system created

---

## 🎯 NEXT STEPS

### Immediate (Do Now):

1. **Open** `BATCH-CONVERSION-PROMPTS.md`
2. **Copy** BATCH 1 section
3. **Start new Claude Code session**
4. **Paste** and let Claude convert

### After Each Batch:

1. ✅ Check converted files look good
2. 🔄 Upload to Netlify (drag & drop)
3. 🧪 Test on live site
4. ➡️ Move to next batch

### Final Steps:

1. Test all 50 procedure pages
2. Verify navigation works
3. Check mobile responsiveness
4. Add AI-generated images (see `images/AI-IMAGE-GENERATION-GUIDE.md`)
5. Set up custom domain (if applicable)

---

## 📋 TEMPLATE USED

**Source:** `/pages/procedures/pelvic-intimate/labiaplasty.html`

This template includes:
- Professional header with dropdowns
- Hero section with breadcrumbs
- Quick info bar (Duration, Anesthesia, Recovery, Results)
- Complete procedure sections
- FAQ accordion
- CTA with contact info
- Footer with all links
- Structured data for SEO

---

## 🆘 TROUBLESHOOTING

**Q: Claude times out during conversion?**
A: Convert fewer files per batch (3-5 instead of 7-9)

**Q: Paths are broken after conversion?**
A: All files in `procedures/*` use `../../../` for root

**Q: How do I verify conversions worked?**
A: Open converted HTML file in browser, check structure matches labiaplasty.html

**Q: Should I convert files manually or use batches?**
A: Use batches! Much faster and ensures consistency.

---

## 📞 CONTACT INFO TO USE

**Phone:** +1 (876) 611-5100
**Address:** 10-12 Oxford Road, Kingston 5, Jamaica
**Hours:** Mon-Fri 9AM-7PM | Sat 10AM-3PM

---

## 🎨 AFTER CONVERSION

1. **Generate AI Images** (optional but recommended)
   - See `images/AI-IMAGE-GENERATION-GUIDE.md`
   - Use Midjourney, DALL-E, or Stable Diffusion
   - Add luxury aesthetic images to each procedure

2. **Test Everything**
   - All navigation links
   - Mobile responsive design
   - Contact forms
   - WhatsApp button

3. **SEO Optimization**
   - Verify structured data
   - Check meta descriptions
   - Update sitemap.xml

4. **Deploy to Netlify**
   - Drag updated files to Netlify
   - Test live site: https://willowy-crostata-60e7ea.netlify.app
   - Change site name to something better

---

## 💡 TIPS

- **Work in batches** - Don't try to convert all 46 at once
- **Test frequently** - Check each batch before moving to next
- **Keep backups** - Files are in git, you can always revert
- **Stay organized** - Mark completed batches in BATCH-CONVERSION-PROMPTS.md

---

**Ready to start?** Open `BATCH-CONVERSION-PROMPTS.md` now! 🚀
