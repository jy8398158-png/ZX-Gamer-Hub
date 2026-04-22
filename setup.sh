#!/bin/bash

# ZX Gaming Hub - Quick Setup Script

echo "🎮 ZX Gaming Hub - Skill Assessment Setup"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "✅ Virtual environment created and activated"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Dependencies installed"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file..."
    cp .env.example .env
    echo "⚠️  IMPORTANT: Edit .env and add your Discord Webhook URL"
    echo "   You can get it from: https://discord.com/api/webhooks/..."
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env and add your Discord Webhook URL"
echo "2. Run: python assessment_backend.py"
echo "3. Open skill-assessment.html in your browser"
echo ""
echo "📚 For detailed instructions, see README.md"
