# 🎮 ZX Gaming Hub - Skill Assessment System

A comprehensive skill assessment form that evaluates programming knowledge and sends results to your Discord server.

## ✨ Features

- 🎯 **Complete Skill Assessment** - Tests programming experience, languages, frameworks, and skills
- 📊 **Auto Ranking** - Automatically determines rank based on responses:
  - **Member** (0-40 points) - Entry level
  - **Programmer** (40-65 points) - Intermediate knowledge
  - **Developer** (65-85 points) - Advanced skills
  - **Demon Eye** (85+ points) - Elite/Master level
- 📩 **Discord Integration** - Sends assessment results privately to Discord
- 🎨 **Beautiful UI** - Purple/black gaming theme matching your ZX brand
- 📱 **Responsive Design** - Works on desktop and mobile
- ⚡ **Real-time Validation** - Client-side form validation

## 🚀 Setup Guide

### Step 1: Create a Discord Webhook

1. Go to your Discord server
2. Right-click on the channel → **Edit Channel**
3. Go to **Integrations** → **Webhooks**
4. Click **New Webhook**
5. Name it: `ZX Gaming Assessment`
6. Click **Copy Webhook URL**
7. Save this URL (you'll need it next)

### Step 2: Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and replace:
   ```
   DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN
   ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Backend

```bash
python assessment_backend.py
```

The backend will run on `http://localhost:5000`

### Step 5: Open the Form

Open `skill-assessment.html` in your browser or host it on a web server.

## 📋 Form Sections

### Personal Information
- Name
- Discord Username
- Email

### Programming Experience
- Years of experience (0-1, 1-3, 3-5, 5+ years)

### Programming Languages
Select all proficient languages:
- Python, JavaScript, Java, C++, C#, Go, Rust, TypeScript, Web Dev

### Development Skills
Rate proficiency in:
- Frontend Development
- Backend Development

### Additional Skills
Select additional expertise:
- DevOps/Deployment
- Database Management
- Cloud Services
- Testing/QA
- Machine Learning/AI
- Security/Cybersecurity
- Mobile Development

### Frameworks & Tools
Text area for listing frameworks and tools

### Portfolio
Links and descriptions of projects/portfolio

## 📊 Scoring System

Points are calculated based on:
- **Experience (0-20 pts)**: Years of programming experience
- **Languages (0-20 pts)**: Number of languages known
- **Proficiency (0-30 pts)**: Frontend and Backend skill levels
- **Skills (0-20 pts)**: Additional technical skills
- **Portfolio (0-10 pts)**: Quality of portfolio/projects

**Total: 0-100 points**

### Ranks
- **Demon Eye**: 85-100 (Elite developers with extensive experience)
- **Developer**: 65-84 (Advanced developers with solid experience)
- **Programmer**: 40-64 (Intermediate developers with good foundation)
- **Member**: 0-39 (Entry-level or beginning developers)

## 📬 Discord Notification

When a form is submitted, you'll receive a Discord message with:
- Applicant's name and Discord username
- Assigned rank with score
- Experience level
- Programming languages
- Skill levels
- Additional skills
- Frameworks and tools knowledge
- Portfolio information
- Submission timestamp

## 🔧 File Structure

```
/workspaces/ZX-Gamer-Hub/
├── skill-assessment.html      # Frontend form
├── assessment_backend.py       # Flask backend server
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
├── README.md                  # This file
```

## 💾 Requirements.txt

```
Flask==2.3.0
requests==2.31.0
python-dotenv==1.0.0
```

## 🔐 Security Notes

- Never commit `.env` file to git (it contains your Discord webhook)
- Webhook URLs should be kept private
- Consider rate limiting if deploying publicly
- Validate all user inputs on backend

## 🎮 Customization

### Modify Ranks Thresholds

Edit `assessment_backend.py`:
```python
RANK_THRESHOLDS = {
    'Demon Eye': 85,
    'Developer': 65,
    'Programmer': 40,
    'Member': 0
}
```

### Change Colors

In `skill-assessment.html`, modify the CSS variables:
```css
border: 2px solid #b300ff;      /* Purple */
color: #d400ff;                  /* Bright purple */
```

### Add More Questions

Edit both HTML form and scoring logic in `assessment_backend.py`

## 🐛 Troubleshooting

### "Failed to send to Discord"
- Check if DISCORD_WEBHOOK_URL is correctly set in `.env`
- Verify webhook URL is still valid
- Check Discord rate limits (max 10 requests/sec)

### Form not showing
- Make sure `skill-assessment.html` is in the correct directory
- Check browser console for errors
- Verify Flask backend is running on localhost:5000

### Backend not starting
- Install requirements: `pip install -r requirements.txt`
- Check if port 5000 is already in use
- Run: `python assessment_backend.py` in the correct directory

## 📞 Support

For issues or questions, check:
1. Flask console output for errors
2. Browser developer console (F12)
3. Discord webhook validation
4. Environment variables are set correctly

---

**Made with 💜 for ZX Gaming Hub**
