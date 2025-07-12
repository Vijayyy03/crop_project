#!/usr/bin/env python3
"""
Crop Recommendation System Launcher
This script starts both the Flask authentication server and Streamlit app
"""

import subprocess
import threading
import time
import requests
import sys
import os

def check_port(port):
    """Check if a port is available"""
    try:
        response = requests.get(f'http://localhost:{port}', timeout=1)
        return True
    except:
        return False

def start_streamlit():
    """Start Streamlit app"""
    print("Starting Streamlit app...")
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port', '8501',
            '--server.address', 'localhost'
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting Streamlit: {e}")
    except KeyboardInterrupt:
        print("Streamlit stopped by user")

def start_flask():
    """Start Flask app"""
    print("Starting Flask authentication server...")
    try:
        subprocess.run([
            sys.executable, 'flask_app.py'
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting Flask: {e}")
    except KeyboardInterrupt:
        print("Flask stopped by user")

def main():
    print("🌾 Crop Recommendation System")
    print("=" * 40)
    
    # Check if required files exist
    if not os.path.exists('app.py'):
        print("Error: app.py not found!")
        return
    
    if not os.path.exists('flask_app.py'):
        print("Error: flask_app.py not found!")
        return
    
    print("Starting services...")
    print("- Flask (Authentication): http://localhost:5000")
    print("- Streamlit (Crop Recommendation): http://localhost:8501")
    print()
    
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Wait a moment for Flask to start
    time.sleep(2)
    
    # Start Streamlit in main thread
    start_streamlit()

if __name__ == '__main__':
    main() 