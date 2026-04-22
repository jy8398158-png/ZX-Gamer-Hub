#!/usr/bin/env python3
"""
ZX Gaming Hub - Skill Assessment Backend
Receives skill assessment forms and sends results to Discord
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Discord Configuration
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')
DISCORD_USER_ID = os.getenv('DISCORD_USER_ID', '')  # Your Discord User ID for DMS

# Rank Calculation Thresholds
RANK_THRESHOLDS = {
    'Demon Eye': 85,
    'Elite Hunter': 65,
    'Bounty Hunter': 40,
    'Applicant': 0
}

def calculate_skill_score(data):
    """
    Calculate a skill score based on form responses (0-100)
    """
    score = 0
    max_score = 0
    
    # Experience scoring (0-20 points)
    experience_scores = {
        '0-1': 5,
        '1-3': 10,
        '3-5': 15,
        '5+': 20
    }
    experience = data.get('experience', '0-1')
    exp_score = experience_scores.get(experience, 0)
    score += exp_score
    max_score += 20
    
    # Languages scoring (0-20 points)
    languages = data.get('languages', [])
    language_count = len(languages)
    lang_score = min(language_count * 2, 20)
    score += lang_score
    max_score += 20
    
    # Frontend/Backend proficiency (0-30 points)
    frontend = data.get('frontend', '')
    backend = data.get('backend', '')
    
    proficiency_scores = {
        'Beginner': 3,
        'Intermediate': 7,
        'Advanced': 12,
        'Expert': 15
    }
    
    score += proficiency_scores.get(frontend, 0)
    score += proficiency_scores.get(backend, 0)
    max_score += 30
    
    # Additional skills (0-20 points)
    skills = data.get('skills', [])
    skills_score = min(len(skills) * 3, 20)
    score += skills_score
    max_score += 20
    
    # Portfolio/Projects (0-10 points)
    portfolio = data.get('portfolio', '').strip()
    if len(portfolio) > 50:
        score += 10
    max_score += 10
    
    # Calculate percentage
    percentage = int((score / max_score) * 100) if max_score > 0 else 0
    return min(percentage, 100)  # Cap at 100

def determine_rank(score):
    """
    Determine rank based on skill score
    """
    for rank, threshold in sorted(RANK_THRESHOLDS.items(), key=lambda x: x[1], reverse=True):
        if score >= threshold:
            return rank
    return 'Member'

def format_discord_message(data, score, rank):
    """
    Format the assessment data into a Discord embed message for ZX-Trickster
    """
    
    languages_str = ', '.join(data.get('languages', [])) or 'None listed'
    skills_str = ', '.join(data.get('skills', [])) or 'None listed'
    tools_str = data.get('tools', 'Not provided').strip() or 'Not provided'
    portfolio_str = data.get('portfolio', 'Not provided').strip() or 'Not provided'
    
    # Determine color based on rank
    rank_colors = {
        'Demon Eye': 0xFF0000,      # Red
        'Elite Hunter': 0xB300FF,   # Purple
        'Bounty Hunter': 0x00FFFF,  # Cyan
        'Applicant': 0x808080       # Gray
    }
    
    embed = {
        "title": f"🎯 NEW BOUNTY APPLICATION - {rank.upper()}",
        "description": f"Skill Score: {score}/100 | Tier: {rank}",
        "color": rank_colors.get(rank, 0xB300FF),
        "fields": [
            {
                "name": "👤 Applicant Info",
                "value": f"**Name:** {data.get('name')}\n**Discord:** {data.get('discord')}\n**Email:** {data.get('email')}",
                "inline": False
            },
            {
                "name": "📊 Experience",
                "value": data.get('experience', 'Not specified'),
                "inline": True
            },
            {
                "name": "⭐ Recommended Tier",
                "value": rank,
                "inline": True
            },
            {
                "name": "💻 Languages",
                "value": languages_str,
                "inline": False
            },
            {
                "name": "🔧 Skills",
                "value": skills_str,
                "inline": False
            },
            {
                "name": "⚙️ Frameworks & Tools",
                "value": f"```{tools_str}```",
                "inline": False
            },
            {
                "name": "📁 Portfolio/Projects",
                "value": f"```{portfolio_str[:500]}{'...' if len(portfolio_str) > 500 else ''}```",
                "inline": False
            },
            {
                "name": "Frontend Level",
                "value": data.get('frontend', 'Not rated'),
                "inline": True
            },
            {
                "name": "Backend Level",
                "value": data.get('backend', 'Not rated'),
                "inline": True
            },
            {
                "name": "📅 Applied",
                "value": data.get('submittedAt', datetime.now().isoformat()),
                "inline": False
            }
        ],
        "footer": {
            "text": "🎯 ZX Bounty Program - Reviewed by ZX-Trickster"
        }
    }
    
    return embed

@app.route('/submit-assessment', methods=['POST'])
def submit_assessment():
    """
    Receive skill assessment form submission
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'discord', 'email']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Calculate score and rank
        score = calculate_skill_score(data)
        rank = determine_rank(score)
        
        # Format discord message
        embed = format_discord_message(data, score, rank)
        
        # Send to Discord webhook
        if DISCORD_WEBHOOK_URL:
            webhook_data = {
                "content": f"🎯 NEW BOUNTY APPLICATION from {data.get('name')} (@{data.get('discord')}) - Tier: {rank}",
                "embeds": [embed]
            }
            
            response = requests.post(
                DISCORD_WEBHOOK_URL,
                json=webhook_data,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code not in [200, 204]:
                print(f"Discord webhook error: {response.status_code}")
                return jsonify({'error': 'Failed to send to Discord'}), 500
        
        return jsonify({
            'success': True,
            'message': f'✅ Application submitted! ZX-Trickster will review your bounty tier ({rank}) shortly.',
            'score': score,
            'rank': rank
        }), 200
    
    except Exception as e:
        print(f"Error processing assessment: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'ZX Gaming Hub Assessment'}), 200

@app.route('/', methods=['GET'])
def home():
    """Home endpoint - serve form or status"""
    try:
        with open('skill-assessment.html', 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html'}
    except:
        return jsonify({
            'status': 'running',
            'service': 'ZX Gaming Hub Skill Assessment',
            'version': '1.0',
            'endpoints': {
                'health': '/health',
                'submit': '/submit-assessment (POST)',
                'form': '/'
            }
        }), 200

if __name__ == '__main__':
    # Get port from environment or use default 5000
    port = int(os.getenv('PORT', 5000))
    print("🎮 ZX Gaming Hub - Skill Assessment Backend")
    print(f"Discord Webhook configured: {'✅' if DISCORD_WEBHOOK_URL else '❌'}")
    print(f"Listening on port {port}...")
    app.run(debug=False, host='0.0.0.0', port=port)
