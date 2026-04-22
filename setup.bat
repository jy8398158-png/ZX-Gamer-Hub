@echo off
REM ZX Gaming Hub - Quick Setup Script for Windows

echo.
echo 🎮 ZX Gaming Hub - Skill Assessment Setup
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python found: %PYTHON_VERSION%
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo ✅ Virtual environment created and activated
echo.

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

echo ✅ Dependencies installed
echo.

REM Check if .env exists
if not exist .env (
    echo ⚙️  Creating .env file...
    copy .env.example .env
    echo ⚠️  IMPORTANT: Edit .env and add your Discord Webhook URL
    echo    You can get it from: https://discord.com/api/webhooks/...
)

echo.
echo ✅ Setup complete!
echo.
echo 📝 Next steps:
echo 1. Edit .env and add your Discord Webhook URL
echo 2. Run: python assessment_backend.py
echo 3. Open skill-assessment.html in your browser
echo.
echo 📚 For detailed instructions, see README.md
echo.
pause
