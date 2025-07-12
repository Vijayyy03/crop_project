from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import subprocess
import threading
import time
import requests

# Initialize Flask app and configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Use env variable for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Global variable to track Streamlit status
streamlit_running = False
streamlit_process = None

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Load user for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def start_streamlit():
    """Start Streamlit in a separate thread"""
    global streamlit_process, streamlit_running
    try:
        # Start Streamlit as a subprocess
        streamlit_process = subprocess.Popen([
            'python', '-m', 'streamlit', 'run', 'app.py',
            '--server.port', '8501',
            '--server.address', 'localhost',
            '--server.headless', 'true'
        ])
        streamlit_running = True
        print("Streamlit started successfully on port 8501")
    except Exception as e:
        print(f"Error starting Streamlit: {e}")
        streamlit_running = False

def check_streamlit_status():
    """Check if Streamlit is running"""
    try:
        response = requests.get('http://localhost:8501', timeout=2)
        return response.status_code == 200
    except:
        return False

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not password:
            flash('Username and password are required.', 'error')
            return redirect(url_for('register'))

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.', 'error')
            return redirect(url_for('register'))

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            
            # Ensure Streamlit is running before redirecting
            if not streamlit_running:
                # Start Streamlit if not running
                streamlit_thread = threading.Thread(target=start_streamlit)
                streamlit_thread.daemon = True
                streamlit_thread.start()
                
                # Wait a moment for Streamlit to start
                time.sleep(3)
            
            # Redirect to the Streamlit app
            return redirect("http://localhost:8501")
        else:
            flash('Login failed. Check your username and password.', 'error')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Streamlit status route
@app.route('/streamlit-status')
def streamlit_status():
    """Check if Streamlit is running"""
    if check_streamlit_status():
        return {'status': 'running', 'url': 'http://localhost:8501'}
    else:
        return {'status': 'not_running'}

# Start Streamlit route
@app.route('/start-streamlit')
def run_streamlit():
    """Manually start Streamlit"""
    global streamlit_running
    if not streamlit_running:
        streamlit_thread = threading.Thread(target=start_streamlit)
        streamlit_thread.daemon = True
        streamlit_thread.start()
        return 'Starting Streamlit... Please wait a moment and then visit http://localhost:8501'
    else:
        return 'Streamlit is already running on http://localhost:8501'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if not already created
    
    # Start Streamlit automatically when Flask starts
    print("Starting Streamlit in background...")
    streamlit_thread = threading.Thread(target=start_streamlit)
    streamlit_thread.daemon = True
    streamlit_thread.start()
    
    print("Flask app starting on http://localhost:5000")
    print("Streamlit will be available on http://localhost:8501")
    app.run(debug=True, host='localhost', port=5000)
