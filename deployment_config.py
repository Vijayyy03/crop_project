"""
Deployment Configuration for Crop Recommendation System

This file helps configure the application for different deployment scenarios.
Set the appropriate environment variables based on your deployment platform.

For Local Development:
- No environment variables needed (uses defaults)

For Heroku:
- Set STREAMLIT_URL to your Heroku app URL
- Set STREAMLIT_PORT to 8501
- Set STREAMLIT_HOST to 0.0.0.0

For Railway:
- Set STREAMLIT_URL to your Railway app URL
- Set STREAMLIT_PORT to 8501
- Set STREAMLIT_HOST to 0.0.0.0

For Render:
- Set STREAMLIT_URL to your Render app URL
- Set STREAMLIT_PORT to 8501
- Set STREAMLIT_HOST to 0.0.0.0

For Streamlit Cloud:
- Set STREAMLIT_URL to your Streamlit Cloud app URL
- Set STREAMLIT_PORT to 8501
- Set STREAMLIT_HOST to 0.0.0.0
"""

import os

# Default configuration for local development
DEFAULT_CONFIG = {
    'STREAMLIT_URL': 'http://localhost:8501',
    'STREAMLIT_PORT': '8501',
    'STREAMLIT_HOST': 'localhost',
    'SECRET_KEY': 'your_default_secret_key'
}

def get_config():
    """Get configuration from environment variables or use defaults"""
    config = {}
    for key, default_value in DEFAULT_CONFIG.items():
        config[key] = os.getenv(key, default_value)
    return config

def print_config():
    """Print current configuration for debugging"""
    config = get_config()
    print("Current Configuration:")
    print(f"STREAMLIT_URL: {config['STREAMLIT_URL']}")
    print(f"STREAMLIT_PORT: {config['STREAMLIT_PORT']}")
    print(f"STREAMLIT_HOST: {config['STREAMLIT_HOST']}")
    print(f"SECRET_KEY: {'*' * len(config['SECRET_KEY'])} (hidden)")

if __name__ == "__main__":
    print_config() 