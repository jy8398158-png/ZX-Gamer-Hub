# 🎮 ZX GAMING HUB - QUICK REFERENCE

## 🚀 TL;DR - 3 STEPS

### Step 1: Get Discord Webhook
```
Discord → Channel Settings → Integrations → Webhooks → New Webhook
Copy the URL
```

### Step 2: Configure
```bash
# Copy example config
cp .env.example .env

# Edit .env and paste webhook URL
# DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN
```

### Step 3: Run
```bash
python assessment_backend.py    # Start server
# Open: skill-assessment.html   # In browser
```

---

## 📁 FILES YOU NEED

| File | What It Does |
|------|------------|
| `skill-assessment.html` | 👁️ What users see (open in browser) |
| `assessment_backend.py` | 🧠 Processes forms, calculates ranks, sends Discord |
| `.env` | 🔑 Your Discord webhook (KEEP SECRET!) |

---

## ⚙️ ONE-TIME SETUP

```bash
# Linux/Mac:
bash setup.sh

# Windows:
setup.bat

# Manual:
python -m venv venv
source venv/bin/activate            # Or on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🏃 EVERY TIME YOU WANT TO USE IT

```bash
# Start the backend
python assessment_backend.py

# Then open in browser:
# file:///workspaces/ZX-Gamer-Hub/skill-assessment.html
# or copy the path and open it manually
```

---

## 🧮 RANKS & SCORES

```
Score   Rank          Color
0-39    Member        ⚪ Gray
40-64   Programmer    🔵 Cyan
65-84   Developer     🟣 Purple
85-100  Demon Eye     🔴 Red
```

Points from:
- 20: Years of experience
- 20: Languages known
- 30: Frontend + Backend proficiency
- 20: Additional skills (DevOps, Cloud, ML, etc.)
- 10: Portfolio quality

---

## 🔧 CUSTOMIZE

### Change Ranks
Edit `assessment_backend.py`:
```python
RANK_THRESHOLDS = {
    'Demon Eye': 85,    # Change these numbers
    'Developer': 65,
    'Programmer': 40,
    'Member': 0
}
```

### Change Colors
Edit `skill-assessment.html` CSS:
```css
#b300ff  → Your purple value
#d400ff  → Your bright purple value
```

### Add/Remove Questions
1. Edit form in `skill-assessment.html`
2. Update `calculate_skill_score()` in `assessment_backend.py`

---

## 🐛 QUICK FIXES

| Problem | Solution |
|---------|----------|
| Backend won't start | `pip install -r requirements.txt` |
| Form won't submit | Check backend is running + BACKEND_URL in HTML |
| No Discord message | Edit `.env`, verify webhook URL |
| Wrong scores | Check scoring logic in backend |

---

## 📚 DOCUMENTS

- `START-HERE.md` → Read this first!
- `QUICKSTART.md` → 5-minute guide
- `README.md` → Full documentation
- `CHECKLIST.md` → Verify everything works
- `verify.py` → Auto-check setup: `python verify.py`

---

## 💾 IMPORTANT

```
🔒 NEVER commit .env to git
🔑 Keep webhook URL secret
📝 Back up webhook URL somewhere
✅ Test before sharing with others
```

---

## 🌐 TO SHARE ONLINE

1. Keep backend running 24/7 (or use free hosting)
2. Upload HTML form to web hosting
3. Update BACKEND_URL in HTML to your server
4. Share form link with community

**Free options:**
- Backend: Railway, Render, Fly.io
- Frontend: GitHub Pages, Netlify, Vercel

---

## 🆘 VERIFY EVERYTHING WORKS

```bash
python verify.py
```

Should show: `✅ EVERYTHING IS READY!`

---

## 📞 QUICK COMMANDS

```bash
# Check backend health
curl http://localhost:5000/health

# View form
open skill-assessment.html    # Mac
xdg-open skill-assessment.html  # Linux
start skill-assessment.html   # Windows

# View Discord webhook in terminal
cat .env | grep DISCORD_WEBHOOK_URL

# Reinstall dependencies
pip install -r requirements.txt -U
```

---

## ✨ ONCE IT'S WORKING

You'll have:
- ✅ People filling forms
- ✅ Auto-calculated scores
- ✅ Assigned ranks
- ✅ Discord notifications
- ✅ All data in one place

---

**EVERYTHING IS READY. GO! 🚀**

For details → Read `START-HERE.md`
