# ⚡ Quick Start Guide

## 5-Minute Setup

### 1️⃣ Get Discord Webhook URL

1. Open your Discord server
2. Right-click a channel → **Edit Channel**
3. Go to **Integrations** → **Webhooks** → **New Webhook**
4. Name it: `ZX Gaming Assessment`
5. Copy the **Webhook URL**

### 2️⃣ Configure Your System

**On Linux/Mac:**
```bash
bash setup.sh
```

**On Windows:**
```bash
setup.bat
```

The scripts will:
- ✅ Check Python installation
- ✅ Create a virtual environment
- ✅ Install dependencies
- ✅ Create a `.env` file

### 3️⃣ Add Discord Webhook

Edit the `.env` file and paste your webhook URL:
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN
```

### 4️⃣ Start the Backend

```bash
python assessment_backend.py
```

You'll see:
```
🎮 ZX Gaming Hub - Skill Assessment Backend
Discord Webhook configured: ✅
 * Running on http://localhost:5000
```

### 5️⃣ Open the Form

Simply open `skill-assessment.html` in your web browser!

---

## 🎯 What Happens Next

1. Someone fills out the form
2. ✅ Form validates in real-time
3. 📤 Submits to your backend
4. 🧮 Backend calculates skill score (0-100)
5. 📊 Determines their rank:
   - **Member** (0-40)
   - **Programmer** (40-65)
   - **Developer** (65-85)
   - **Demon Eye** (85+)
6. 📬 Sends beautiful Discord embed to your webhook
7. ✅ Shows success message to user

---

## 📊 Example Discord Message

When someone submits, you'll receive a Discord message showing:
- Their name and Discord username
- Their calculated skill score and rank
- Years of experience
- Programming languages
- Frontend/Backend proficiency
- Additional skills
- Frameworks knowledge
- Portfolio links
- Submission time

---

## ❓ Common Questions

**Q: Where do the form responses go?**
A: To your Discord through the webhook (private channel)

**Q: Can I customize the ranks?**
A: Yes! Edit `assessment_backend.py` and modify `RANK_THRESHOLDS`

**Q: What if I don't want to run Python locally?**
A: You can deploy this to a free service like Heroku, Render, or Railway

**Q: Can I host the form online?**
A: Yes! Upload `skill-assessment.html` to any web server/hosting

**Q: How do I update the form questions?**
A: Edit `skill-assessment.html` AND update the scoring logic in `assessment_backend.py`

---

## 🚀 For Production Deployment

If deploying online:

1. Host the HTML on your web server
2. Deploy the Python backend to a service like Render/Railway
3. Update the form's fetch URL to point to your backend
4. Use environment variables for your Discord webhook

---

## 📞 Need Help?

Check the detailed [README.md](README.md) for:
- Full installation instructions
- Customization options
- Troubleshooting tips
- Security best practices

---

**You're all set! 🎮**
