"""
call_ai.py - AI Integration for Post This Today
"""

import json
import requests


def get_claude_api_key():
    """Read API key from nocommit.py file"""
    #file_path = '/Users/andrewlaudato/PythonProjects/postthistoday/postthistoday/nocommit.py'
    file_path = './postthistoday/nocommit.py'

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()

            if "CLAUDE_API_KEY = '" in content:
                start = content.find("CLAUDE_API_KEY = '") + len("CLAUDE_API_KEY = '")
                end = content.find("'", start)
                api_key = content[start:end]
                return api_key
            else:
                return None

    except Exception:
        return None


API_KEY = get_claude_api_key()


def generate_linkedin_post(selected_topic=None, content_prompt=None, tone='Professional',
                           length='Medium', custom_topics=None, writing_samples=None):
    """Generate LinkedIn post using Claude AI"""

    if not API_KEY:
        return {
            'success': False,
            'content': 'Error code 125. Please contact support.',
            'error': 'No API key configured'
        }

    prompt = f"""Write a LinkedIn post about: {selected_topic or 'general business topic'}

User's ideas: {content_prompt or 'Share professional insights'}

Tone: {tone}
Length: {length}

Make it engaging and professional with relevant hashtags."""

    try:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': API_KEY,
            'anthropic-version': '2023-06-01'
        }

        payload = {
            'model': 'claude-3-haiku-20240307',
            'max_tokens': 500,
            'messages': [{
                'role': 'user',
                'content': prompt
            }]
        }

        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            content = data['content'][0]['text']
            return {
                'success': True,
                'content': content,
                'error': None
            }
        else:
            return {
                'success': False,
                'content': 'Error code 125. Please contact support.',
                'error': f'API error: {response.status_code}'
            }

    except Exception as e:
        return {
            'success': False,
            'content': 'Error code 125. Please contact support.',
            'error': str(e)
        }