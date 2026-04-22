# 🎮 ZX Gaming Hub - Skill Assessment System
## START HERE! ✅

---

## 📋 What You Have

A complete skill assessment platform that:
- ✅ Displays a beautiful form for applicants
- ✅ Auto-calculates skill scores
- ✅ Assigns ranks (Member → Programmer → Developer → Demon Eye)
- ✅ Sends results privately to Discord
- ✅ Fully customizable and ready to deploy

---

## 🚀 QUICK START (3 STEPS)

### **Step 1: Create Discord Webhook (2 minutes)**

1. Open your Discord server
2. Right-click any channel → **Edit Channel**
3. Go to **Integrations** → **Webhooks**
4. Click **New Webhook**
5. Name it: `ZX Gaming Assessment`
6. Click **Copy Webhook URL**
7. **SAVE THIS URL** - you need it next

### **Step 2: Install & Configure (2 minutes)**

**Choose your OS:**

**Linux/Mac:**
```bash
cd /workspaces/ZX-Gamer-Hub
bash setup.sh
```

**Windows:**
```bash
cd /workspaces/ZX-Gamer-Hub
setup.bat
```

These scripts will:
- ✅ Install Python dependencies
- ✅ Create a `.env` file
- ✅ Set everything up for you

**Then edit `.env` and add your Discord webhook:**
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN
```

### **Step 3: Start & Test (1 minute)**

```bash
python assessment_backend.py
```

You should see:
```
🎮 ZX Gaming Hub - Skill Assessment Backend
Discord Webhook configured: ✅
 * Running on http://localhost:5000
```

**Open the form in your browser:**
- Simply open the file: `skill-assessment.html`
- Or navigate to: `file:///workspaces/ZX-Gamer-Hub/skill-assessment.html`

---

## ✅ System Check

Before running, make sure you have:

- [ ] Discord webhook URL (from Step 1)
- [ ] Python 3.8+ installed (`python --version`)
- [ ] `.env` file configured with your webhook
- [ ] Backend running (`python assessment_backend.py`)

---

## 🧪 Test It Out

1. **Open the form** (skill-assessment.html)
2. **Fill it out** with test data
3. **Click Submit**
4. **Check Discord** - You should see the assessment in your configured channel!

Expected Discord message shows:
- ⭐ Skill score (0-100)
- 🎯 Assigned rank
- 📊 All form data
- 🎨 Color-coded by rank

---

## 📊 Ranking System

| Rank | Score | Requirement |
|------|-------|------------|
| 🔴 **Demon Eye** | 85-100 | Elite developers with deep expertise |
| 🟣 **Developer** | 65-84 | Advanced skills, proven projects |
| 🔵 **Programmer** | 40-64 | Solid fundamentals, multiple languages |
| ⚪ **Member** | 0-39 | Entry level or new developers |

---

## 📁 File Breakdown

| File | Purpose |
|------|---------|
| `skill-assessment.html` | 🎨 The form (open in browser) |
| `assessment_backend.py` | 🖥️ Server processing form data |
| `requirements.txt` | 📦 Python dependencies |
| `.env.example` | ⚙️ Config template |
| `.env` | ⚙️ Your actual config (CREATE THIS) |
| `setup.sh` / `setup.bat` | 🔧 Automated setup |
| `README.md` | 📖 Full documentation |
| `QUICKSTART.md` | ⚡ Quick reference |

---

## ⚙️ Configuration

### Discord Webhook
Edit `.env`:
```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN
```

### Customize Ranks
Edit `assessment_backend.py`:
```python
RANK_THRESHOLDS = {
    'Demon Eye': 85,      # Edit these numbers
    'Developer': 65,
    'Programmer': 40,
    'Member': 0
}
```

### Customize Questions
1. Edit form in `skill-assessment.html`
2. Update scoring in `assessment_backend.py` (`calculate_skill_score` function)

### Change Colors/Theme
Edit CSS in `skill-assessment.html`:
```css
#b300ff  /* Purple - change this */
#d400ff  /* Bright purple - change this */
```

---

## 🚨 Troubleshooting

### "Discord Webhook is not configured"
- [ ] Edit `.env` file
- [ ] Add your webhook URL
- [ ] Make sure there's no extra spaces

### "Connection refused" / Backend won't start
- [ ] Run: `python assessment_backend.py`
- [ ] Check if port 5000 is available
- [ ] Try: `pip install -r requirements.txt`

### Form won't submit
- [ ] Backend must be running (`python assessment_backend.py`)
- [ ] Check browser console (F12) for errors
- [ ] Make sure BACKEND_URL in HTML matches your server

### Nothing appearing in Discord
- [ ] Webhook URL is wrong (test in `.env`)
- [ ] Webhook might be deleted (create a new one)
- [ ] Check Discord channel permissions

---

## 🌍 Hosting Online

Want to deploy this publicly?

### Option 1: Deploy Backend (Free)
- **Render** (render.com) - Free tier available
- **Railway** (railway.app) - Free credits
- **Heroku** (heroku.com) - Former free tier
- **Fly.io** (fly.io) - Free tier available

### Option 2: Host Form (Free)
- **GitHub Pages** - Upload HTML file
- **Netlify** - Drag & drop deploy
- **Vercel** - Frontend hosting
- **Firebase** - Google's platform

### Option 3: Everything Together (Low Cost)
- Get a cheap VPS ($3-5/month)
- Run both form and backend
- Use a domain name

**Need help deploying?** See deployment section in `README.md`

---

## 📞 Quick Reference

**Start Backend:**
```bash
python assessment_backend.py
```

**View Backend Health:**
```bash
curl http://localhost:5000/health
```

**Reinstall Dependencies:**
```bash
pip install -r requirements.txt --upgrade
```

**Create Virtual Environment Manually:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🎯 Next Steps

1. ✅ Get Discord webhook
2. ✅ Run setup script (setup.sh or setup.bat)
3. ✅ Add webhook to `.env`
4. ✅ Start backend (`python assessment_backend.py`)
5. ✅ Open `skill-assessment.html`
6. ✅ Test by submitting form
7. ✅ Check Discord for results
8. ✅ (Optional) Customize questions & scoring

---

## 💡 Pro Tips

- 🎨 Customize the theme to match your brand
- 📊 Adjust rank thresholds based on your standards
- 🔒 Keep `.env` secure (never share webhook)
- 📧 Add your email to notifications
- 🚀 Deploy backend online for persistent form
- 💾 Save responses to database (advanced)

---

## 📖 For More Info

- **Quick guide:** `QUICKSTART.md`
- **Full docs:** `README.md`
- **Form:** `skill-assessment.html`
- **Backend:** `assessment_backend.py`

---

## ✨ You're Ready!

Everything is configured and ready to go. Just:
1. Add your Discord webhook to `.env`
2. Run `python assessment_backend.py`
3. Open `skill-assessment.html`

**That's it!** 🎮

---

**Questions?** Check the files above or re-read the setup steps.

**Ready to share?** Deploy it online or share the form link with your community!
