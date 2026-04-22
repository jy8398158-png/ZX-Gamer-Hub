#!/usr/bin/env python3
"""
ZX Gaming Hub - System Verification Script
Checks if everything is properly configured and ready to go
"""

import os
import sys
from pathlib import Path

def check_mark(passed):
    return "✅" if passed else "❌"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def verify_files():
    """Check if all required files exist"""
    print_section("📁 CHECKING FILES")
    
    required_files = [
        'skill-assessment.html',
        'assessment_backend.py',
        'requirements.txt',
        '.env.example',
        'setup.sh',
        'setup.bat',
        'README.md',
        'QUICKSTART.md',
        'START-HERE.md'
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        all_exist = all_exist and exists
        print(f"{check_mark(exists)} {file}")
    
    return all_exist

def verify_python():
    """Check Python version"""
    print_section("🐍 CHECKING PYTHON")
    
    version = sys.version_info
    supports_python = version.major == 3 and version.minor >= 8
    
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    print(f"{check_mark(supports_python)} Python 3.8+ required")
    
    return supports_python

def verify_dependencies():
    """Check if dependencies can be imported"""
    print_section("📦 CHECKING DEPENDENCIES")
    
    dependencies = {
        'flask': 'Flask',
        'requests': 'requests',
        'dotenv': 'python-dotenv'
    }
    
    all_installed = True
    for module, name in dependencies.items():
        try:
            __import__(module)
            print(f"{check_mark(True)} {name}")
        except ImportError:
            print(f"{check_mark(False)} {name} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def verify_env():
    """Check .env configuration"""
    print_section("⚙️  CHECKING CONFIGURATION")
    
    env_exists = os.path.exists('.env')
    print(f"{check_mark(env_exists)} .env file exists")
    
    if env_exists:
        with open('.env', 'r') as f:
            content = f.read()
            has_webhook = 'DISCORD_WEBHOOK_URL=' in content
            webhook_configured = 'https://discord.com/api/webhooks/' in content
            
            print(f"{check_mark(has_webhook)} DISCORD_WEBHOOK_URL defined")
            print(f"{check_mark(webhook_configured)} Webhook URL properly configured")
            
            return webhook_configured
    else:
        print(f"{check_mark(False)} .env file not found (create from .env.example)")
        return False

def verify_backend():
    """Check backend code"""
    print_section("🖥️  CHECKING BACKEND")
    
    with open('assessment_backend.py', 'r') as f:
        backend = f.read()
        
    checks = {
        'Flask app': 'Flask(__name__)' in backend,
        'Discord webhook': 'DISCORD_WEBHOOK_URL' in backend,
        'Rank system': 'RANK_THRESHOLDS' in backend,
        'Submit endpoint': '/submit-assessment' in backend,
        'CORS enabled': 'CORS' in backend or 'cors' in backend.lower()
    }
    
    all_good = True
    for check, passed in checks.items():
        all_good = all_good and passed
        print(f"{check_mark(passed)} {check}")
    
    return all_good

def verify_frontend():
    """Check frontend form"""
    print_section("🎨 CHECKING FRONTEND")
    
    with open('skill-assessment.html', 'r') as f:
        form = f.read()
    
    checks = {
        'Form element': '<form' in form,
        'Assessment fields': 'name' in form and 'discord' in form and 'email' in form,
        'Rating questions': 'experience' in form and 'frontend' in form and 'backend' in form,
        'Language selection': 'languages' in form and 'Python' in form,
        'Skills checkboxes': 'skills' in form,
        'Portfolio field': 'portfolio' in form,
        'Submit button': 'submit' in form.lower(),
        'JavaScript handler': 'fetch' in form and 'BACKEND_URL' in form
    }
    
    all_good = True
    for check, passed in checks.items():
        all_good = all_good and passed
        print(f"{check_mark(passed)} {check}")
    
    return all_good

def print_summary(checks):
    """Print summary and recommendations"""
    print_section("📊 VERIFICATION SUMMARY")
    
    total = len(checks)
    passed = sum(checks.values())
    percentage = int((passed / total) * 100)
    
    print(f"Status: {passed}/{total} checks passed ({percentage}%)\n")
    
    if percentage == 100:
        print("🎉 EVERYTHING IS READY!")
        print("\nNext steps:")
        print("1. Run: python assessment_backend.py")
        print("2. Open: skill-assessment.html in your browser")
        print("3. Test the form")
        print("4. Check your Discord for results!")
    else:
        print("⚠️  SOME ISSUES NEED ATTENTION:")
        
        if not checks.get('files', True):
            print("  → Missing files - check START-HERE.md for setup")
        
        if not checks.get('python', True):
            print("  → Python 3.8+ required - upgrade or update")
        
        if not checks.get('dependencies', True):
            print("  → Missing dependencies - run: pip install -r requirements.txt")
        
        if not checks.get('env', True):
            print("  → Configuration incomplete - copy .env.example to .env and add Discord webhook")
        
        print("\nFor help, read: START-HERE.md")

def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " " * 10 + "ZX GAMING HUB - SYSTEM VERIFICATION" + " " * 14 + "║")
    print("╚" + "="*58 + "╝")
    
    checks = {
        'files': verify_files(),
        'python': verify_python(),
        'dependencies': verify_dependencies(),
        'env': verify_env(),
        'backend': verify_backend(),
        'frontend': verify_frontend()
    }
    
    print_summary(checks)
    
    print("\n")
    
    # Exit with appropriate code
    if all(checks.values()):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
