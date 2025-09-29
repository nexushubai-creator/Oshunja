# 🚀 Deploy OSHUNJA to GitHub Pages

Your website is now ready to push to GitHub! Follow these steps to get it online.

---

## ✅ What's Already Done

- [x] Git repository initialized
- [x] All files committed
- [x] Branch set to `main`

---

## 📋 Next Steps (5 Minutes)

### **Step 1: Create GitHub Repository**

1. Go to **https://github.com/new**
2. Fill in the form:
   - **Repository name:** `oshunja-website` (or any name you want)
   - **Description:** `OSHUNJA - Luxury Gynecology, Aesthetics & Wellness Clinic in Kingston, Jamaica`
   - **Public** or **Private:** Choose Public (required for free GitHub Pages)
   - **❌ DO NOT** check "Initialize with README" (we already have files)
3. Click **"Create repository"**

---

### **Step 2: Connect and Push to GitHub**

After creating the repository, GitHub will show you commands. Run these in your terminal:

```bash
# Connect your local repo to GitHub
git remote add origin https://github.com/YOUR-USERNAME/oshunja-website.git

# Push your code to GitHub
git push -u origin main
```

**Replace `YOUR-USERNAME`** with your actual GitHub username!

**Example:**
```bash
git remote add origin https://github.com/jmatthewlee/oshunja-website.git
git push -u origin main
```

---

### **Step 3: Enable GitHub Pages**

1. Go to your repository on GitHub
2. Click **"Settings"** (top menu)
3. Scroll down and click **"Pages"** (left sidebar)
4. Under "Source":
   - Branch: Select **`main`**
   - Folder: Select **`/ (root)`**
5. Click **"Save"**

**Wait 1-2 minutes...** then your site will be live! 🎉

---

## 🌐 Your Website URL

After enabling GitHub Pages, your site will be available at:

```
https://YOUR-USERNAME.github.io/oshunja-website/
```

**Example:**
```
https://jmatthewlee.github.io/oshunja-website/
```

---

## 🔐 Authentication Options

When you run `git push`, GitHub will ask for authentication. Choose one:

### **Option A: Personal Access Token (Recommended)**

1. Go to **https://github.com/settings/tokens**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Settings:
   - Note: `OSHUNJA Website`
   - Expiration: 90 days (or custom)
   - Scopes: Check **`repo`** (gives full repo access)
4. Click **"Generate token"**
5. **COPY THE TOKEN** (you won't see it again!)
6. When `git push` asks for password, **paste the token**

### **Option B: GitHub CLI**

```bash
# Install GitHub CLI (if needed)
# Then authenticate
gh auth login
```

### **Option C: SSH Key**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "info@oshunja.com"

# Copy the public key
cat ~/.ssh/id_ed25519.pub

# Add it to GitHub: https://github.com/settings/keys
```

---

## 🔄 Future Updates

Whenever you make changes to your website:

```bash
# Stage changes
git add .

# Commit with message
git commit -m "Update: describe your changes"

# Push to GitHub
git push

# Wait 1-2 minutes → Changes appear on live site!
```

---

## 🎯 Quick Reference Commands

```bash
# Check status
git status

# See commit history
git log --oneline

# View remote URL
git remote -v

# Pull latest changes
git pull

# Create new branch
git checkout -b new-feature

# Switch branches
git checkout main
```

---

## 📱 Custom Domain (Optional)

Want to use `oshunja.com` instead of GitHub's URL?

1. Buy domain from registrar (Namecheap, GoDaddy, etc.)
2. In repository Settings → Pages → Custom domain
3. Enter `oshunja.com`
4. Update DNS records at your registrar:
   ```
   Type: A
   Host: @
   Value: 185.199.108.153
   ```
5. Wait 24-48 hours for DNS propagation

**Full guide:** https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

---

## ✅ Post-Deployment Checklist

After your site is live:

- [ ] Visit your GitHub Pages URL
- [ ] Test all navigation links
- [ ] Verify mobile responsiveness
- [ ] Test contact form (check console)
- [ ] Check all category pages load
- [ ] Test on different browsers
- [ ] Share link with colleagues for feedback
- [ ] Add images if you haven't already
- [ ] Update contact information (phone/address)
- [ ] Set up Google Analytics (optional)

---

## 🆘 Troubleshooting

### **"Permission denied" when pushing**
- Use Personal Access Token instead of password
- Or set up SSH key authentication

### **"Repository not found"**
- Check the remote URL: `git remote -v`
- Make sure you created the repository on GitHub
- Verify repository name matches

### **GitHub Pages not working**
- Make sure repository is **Public**
- Check Settings → Pages is enabled
- Wait 2-3 minutes after enabling
- Clear browser cache and try again

### **Images not showing**
- Add images to `/images` folder
- Make sure filenames match: `hero-bg.jpg`, `category-bg.jpg`
- Push changes: `git add images/ && git commit -m "Add images" && git push`

---

## 📊 GitHub Repository Features

Your repository includes:

- **README.md** - Technical documentation
- **QUICKSTART.md** - Launch guide
- **PROJECT-SUMMARY.md** - Feature overview
- **Code organization** - Clean folder structure
- **Comments** - Well-documented code
- **Responsive** - Mobile-friendly design
- **SEO-ready** - Meta tags included

---

## 🎉 You're Almost Live!

Just run these commands:

```bash
git remote add origin https://github.com/YOUR-USERNAME/oshunja-website.git
git push -u origin main
```

Then enable GitHub Pages in repository settings.

**Your website will be online in minutes!** 🚀

---

## 📞 Need Help?

- **GitHub Docs:** https://docs.github.com/en/pages
- **Git Tutorial:** https://www.atlassian.com/git/tutorials
- **GitHub Support:** https://support.github.com

---

*Made with ❤️ for OSHUNJA - Where Medicine Meets Aesthetics*