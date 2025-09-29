# 🔑 GitHub Token - Complete Guide

## 📍 Where You'll Paste the Token

The token gets pasted **in the terminal** when Git asks for your password during `git push`.

---

## 🎬 **Complete Walkthrough**

### **BEFORE You Run Commands:**

#### 1️⃣ **Get Your Token First**

Go to: **https://github.com/settings/tokens**

Click: **"Generate new token"** → **"Generate new token (classic)"**

Fill in:
- **Note:** `OSHUNJA Website`
- **Expiration:** 90 days (or No expiration)
- **Select scopes:** ☑ **`repo`** (check this box!)

Click: **"Generate token"**

**IMPORTANT:** Copy the token NOW! It looks like:
```
ghp_abcd1234efgh5678ijkl9012mnop3456qrst
```

You won't be able to see it again!

---

### **NOW Run These Commands:**

#### 2️⃣ **Create GitHub Repository**

1. Open browser: https://github.com/new
2. Repository name: `oshunja-website`
3. Make it: **Public**
4. Click: **"Create repository"**

---

#### 3️⃣ **Connect Your Code (Run in Terminal)**

**Command 1:** (Replace YOUR-USERNAME with your actual GitHub username)
```bash
git remote add origin https://github.com/YOUR-USERNAME/oshunja-website.git
```

Example:
```bash
git remote add origin https://github.com/jmatthewlee/oshunja-website.git
```

---

#### 4️⃣ **Push to GitHub**

**Command 2:**
```bash
git push -u origin main
```

---

## 🎯 **THIS IS WHERE YOU PASTE THE TOKEN:**

After running `git push`, you'll see:

```
Username for 'https://github.com': ▊
```

**Type your GitHub username**, press Enter.

Then you'll see:

```
Password for 'https://YOUR-USERNAME@github.com': ▊
```

**👉 RIGHT HERE - PASTE YOUR TOKEN** (Ctrl+V or Right-click → Paste)

⚠️ **Note:** The token won't show when you paste it (for security). Just paste and press Enter!

---

## ✅ **Success Looks Like:**

```
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
Delta compression using up to 8 threads
Compressing objects: 100% (22/22), done.
Writing objects: 100% (25/25), 45.78 KiB | 2.86 MiB/s, done.
Total 25 (delta 2), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR-USERNAME/oshunja-website.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

🎉 **Your code is now on GitHub!**

---

## 🔄 **Alternative: Save Token (No Need to Paste Again)**

After first successful push, Git can remember your token:

```bash
# Run this once
git config credential.helper store
```

Next time you push, it won't ask for the token again!

---

## 🆘 **Troubleshooting**

### **"Authentication failed"**
- Make sure you copied the **entire token** (starts with `ghp_`)
- Check you selected **`repo`** scope when creating token
- Token might have expired - create a new one

### **"Repository not found"**
- Check your username is spelled correctly in the URL
- Make sure repository exists on GitHub
- Verify repository is public (not private)

### **"Permission denied"**
- Use token, not your GitHub password
- Token needs `repo` scope checked

### **Token Already Closed the Browser?**
- Create a new token: https://github.com/settings/tokens
- Delete old token if you want
- Use the new token when pushing

---

## 📝 **Quick Command Reference**

```bash
# 1. Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/oshunja-website.git

# 2. Push (this will ask for username & token)
git push -u origin main

# 3. Type username, press Enter
# 4. Paste token, press Enter
# 5. Done! ✅
```

---

## 🎥 **Visual Flow**

```
Terminal:
┌─────────────────────────────────────────────┐
│ $ git push -u origin main                   │
│                                             │
│ Username for 'https://github.com':          │
│ > your-github-username ← TYPE THIS          │
│                                             │
│ Password for 'https://...':                 │
│ > ************************ ← PASTE TOKEN   │
│                            (invisible)      │
│                                             │
│ ✅ Pushing to GitHub...                     │
│ ✅ Success!                                 │
└─────────────────────────────────────────────┘
```

---

## 🔒 **Security Tips**

✅ **DO:**
- Save token in password manager
- Use token instead of password
- Set expiration dates on tokens
- Create new tokens for different projects

❌ **DON'T:**
- Share your token with anyone
- Commit token to code
- Use your GitHub password instead of token
- Post token in public forums/screenshots

---

## 💡 **Remember:**

The token acts as your **password** when pushing code to GitHub from the command line.

**When Git asks for "Password"** → **Paste your token**

That's it! Simple as that. 🎉

---

Need help? The token goes in the terminal, not on the GitHub website!