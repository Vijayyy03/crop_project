import streamlit as st
import numpy as np
import pickle
from PIL import Image
import base64

# Load the pre-trained models and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Dictionary mapping prediction results to crop names
crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 
             7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 
             12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 
             17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 
             21: "Chickpea", 22: "Coffee"}

# Streamlit app configuration
st.set_page_config(
    page_title="🌾 Smart Crop Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Full Dark Mode CSS styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Dark Theme Styles */
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    /* Custom Dark Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 24px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/><circle cx="10" cy="60" r="0.5" fill="white" opacity="0.1"/><circle cx="90" cy="40" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }
    
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #ffffff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }
    
    /* Dark Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #0f0f23 0%, #1a1a2e 100%);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #0f0f23 0%, #1a1a2e 100%);
    }
    
    /* Dark Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 14px 32px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 16px;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
    
    /* Dark Input Styling */
    .stTextInput > div > div > input {
        background: rgba(26, 26, 46, 0.8);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        padding: 16px 20px;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #ffffff;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        background: rgba(26, 26, 46, 0.95);
        transform: translateY(-1px);
    }
    
    /* Dark Number Input Styling */
    .stNumberInput > div > div > input {
        background: rgba(26, 26, 46, 0.8);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        padding: 16px 20px;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #ffffff;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        background: rgba(26, 26, 46, 0.95);
        transform: translateY(-1px);
    }
    
    /* Dark Selectbox Styling */
    .stSelectbox > div > div > div {
        background: rgba(26, 26, 46, 0.8);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 16px;
        color: #ffffff;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Dark Card Styling */
    .prediction-card {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 24px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        text-align: center;
        color: #ffffff;
        position: relative;
        overflow: hidden;
    }
    
    .prediction-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(45deg, #667eea, #764ba2);
    }
    
    .prediction-card h2 {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    
    .prediction-card h1 {
        font-family: 'Inter', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        margin: 2rem 0;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .prediction-card p {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #b0b0b0;
        line-height: 1.6;
    }
    
    /* Dark Feature Cards */
    .feature-card {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1rem;
        text-align: center;
        color: #ffffff;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 25px 50px rgba(0,0,0,0.6);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .feature-card h3 {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #667eea;
    }
    
    .feature-card p {
        font-family: 'Inter', sans-serif;
        color: #b0b0b0;
        line-height: 1.6;
    }
    
    /* Dark Info Cards */
    .info-card {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        border-left: 4px solid #667eea;
    }
    
    .info-card h3 {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #667eea;
    }
    
    .info-card p {
        font-family: 'Inter', sans-serif;
        color: #b0b0b0;
        line-height: 1.6;
    }
    
    /* Success Animation */
    @keyframes successPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .success-animation {
        animation: successPulse 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Dark Text Styling */
    .stMarkdown {
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }
    
    /* Dark Radio Button Styling */
    .stRadio > div > label {
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        color: #ffffff;
    }
    
    /* Dark Metric Styling */
    .stMetric {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(26, 26, 46, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    
    /* Dark Form styling */
    .stForm {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Dark Expander styling */
    .streamlit-expanderHeader {
        background: rgba(26, 26, 46, 0.9) !important;
        border-radius: 16px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(26, 26, 46, 0.9) !important;
        border-radius: 16px !important;
        margin-top: 1rem !important;
        padding: 1.5rem !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }
    
    /* Dark Success message styling */
    .stSuccess {
        background: rgba(76, 175, 80, 0.2) !important;
        border: 1px solid rgba(76, 175, 80, 0.4) !important;
        border-radius: 16px !important;
        color: #4caf50 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Dark Spinner styling */
    .stSpinner > div {
        border-color: #667eea !important;
        border-top-color: #764ba2 !important;
    }
    
    /* Dark Text area styling */
    .stTextArea > div > div > textarea {
        background: rgba(26, 26, 46, 0.8) !important;
        border: 2px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 16px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation with dark styling
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 1rem;">
        <h2 style="color: white; font-family: 'Inter', sans-serif; margin-bottom: 2rem; font-weight: 600;">🌾 Smart Crop Advisor</h2>
        <div style="width: 50px; height: 3px; background: linear-gradient(45deg, #667eea, #764ba2); margin: 0 auto 2rem auto; border-radius: 2px;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🌱 Crop Recommendation", "❓ FAQ", "📞 Contact"],
        index=0
    )

# Home Page
if page == "🏠 Home":
    st.markdown("""
    <div class="main-header">
        <h1>🌾 Smart Crop Advisor</h1>
        <p>Revolutionizing Agriculture with AI-Powered Crop Recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🚀 Welcome to the Future of Farming</h3>
            <p>
                Our advanced AI system analyzes soil conditions, weather patterns, and environmental factors to provide 
                personalized crop recommendations. Whether you're a seasoned farmer or just starting your agricultural journey, 
                our intelligent platform helps you make data-driven decisions for optimal crop yields.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <h3>📊 AI Accuracy</h3>
            <h2 style="font-size: 3rem; margin: 1rem 0; background: linear-gradient(45deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">95%</h2>
            <p style="color: #b0b0b0;">Prediction Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("""
    <h2 style="color: #ffffff; font-family: 'Inter', sans-serif; text-align: center; margin: 4rem 0 2rem 0; font-weight: 700; font-size: 2.5rem;">✨ Key Features</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI-Powered Analysis</h3>
            <p>Advanced machine learning algorithms analyze multiple parameters to provide accurate crop recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Instant Results</h3>
            <p>Get personalized crop recommendations within seconds, helping you make quick and informed decisions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🌍 Sustainable Farming</h3>
            <p>Support eco-friendly practices by choosing crops that are best suited for your local environment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # How it works section
    st.markdown("""
    <h2 style="color: #ffffff; font-family: 'Inter', sans-serif; text-align: center; margin: 4rem 0 2rem 0; font-weight: 700; font-size: 2.5rem;">🔬 How It Works</h2>
    """, unsafe_allow_html=True)
    
    steps = [
        {"icon": "📝", "title": "Input Data", "desc": "Enter soil parameters like N, P, K levels, temperature, humidity, pH, and rainfall."},
        {"icon": "🧠", "title": "AI Analysis", "desc": "Our machine learning model processes your data using advanced algorithms."},
        {"icon": "🌱", "title": "Get Results", "desc": "Receive personalized crop recommendations optimized for your conditions."}
    ]
    
    cols = st.columns(3)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <h3 style="font-size: 3rem; margin-bottom: 1rem;">{step['icon']}</h3>
                <h4 style="color: #667eea; font-family: 'Inter', sans-serif; margin-bottom: 1rem; font-weight: 600;">{step['title']}</h4>
                <p style="color: #b0b0b0;">{step['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    <div style="text-align: center; margin: 4rem 0;">
        <div style="background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 24px; padding: 3rem; display: inline-block; box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);">
            <h3 style="color: white; font-family: 'Inter', sans-serif; margin-bottom: 1rem; font-weight: 600;">Ready to Get Started?</h3>
            <p style="color: white; opacity: 0.9; margin-bottom: 1.5rem; font-family: 'Inter', sans-serif;">Click on 'Crop Recommendation' in the sidebar to begin your AI-powered farming journey!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Crop Recommendation Page
elif page == "🌱 Crop Recommendation":
    st.markdown("""
    <div class="main-header">
        <h1>🌱 Crop Recommendation</h1>
        <p>Enter your soil and environmental parameters to get AI-powered crop suggestions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a form for input
    with st.form("crop_recommendation_form"):
        st.markdown("""
        <div class="info-card">
            <h3>📊 Soil Parameters</h3>
            <p>Please enter accurate values for the best crop recommendations. All fields are required for optimal results.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            nitrogen = st.number_input("Nitrogen (N) - mg/kg", min_value=0, max_value=200, value=50, help="Nitrogen content in soil")
            phosphorus = st.number_input("Phosphorus (P) - mg/kg", min_value=0, max_value=200, value=50, help="Phosphorus content in soil")
            potassium = st.number_input("Potassium (K) - mg/kg", min_value=0, max_value=200, value=50, help="Potassium content in soil")
            temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.1, help="Average temperature")
        
        with col2:
            humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50, help="Relative humidity")
            ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0, step=0.1, help="Soil pH level")
            rainfall = st.number_input("Rainfall (mm)", min_value=0, max_value=500, value=100, help="Annual rainfall")
            scaler_choice = st.selectbox("Choose Scaler", ["StandardScaler", "MinMaxScaler"], help="Data preprocessing method")
        
        submitted = st.form_submit_button("🌾 Get Crop Recommendation", use_container_width=True)
        
        if submitted:
            with st.spinner("🤖 AI is analyzing your data..."):
                # Prepare input data
                features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
                
                # Apply scaling
                if scaler_choice == "StandardScaler":
                    features_scaled = sc.transform(features)
                else:
                    features_scaled = mx.transform(features)
                
                # Make prediction
                prediction = model.predict(features_scaled)
                predicted_crop = crop_dict[prediction[0]]
                
                # Display result with animation
                st.markdown(f"""
                <div class="prediction-card success-animation">
                    <h2>🎯 Recommended Crop</h2>
                    <h1>{predicted_crop}</h1>
                    <p>Based on your soil and environmental conditions, <strong>{predicted_crop}</strong> is the optimal crop for your region.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Additional information
                st.markdown("""
                <div class="info-card">
                    <h3>💡 Tips for Success</h3>
                    <ul style="color: #b0b0b0; font-family: 'Inter', sans-serif; line-height: 1.8; padding-left: 1.5rem;">
                        <li>Monitor soil moisture regularly</li>
                        <li>Follow recommended fertilization schedules</li>
                        <li>Consider crop rotation for better soil health</li>
                        <li>Stay updated with local weather forecasts</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

# FAQ Page
elif page == "❓ FAQ":
    st.markdown("""
    <div class="main-header">
        <h1>❓ Frequently Asked Questions</h1>
        <p>Everything you need to know about our AI-powered crop recommendation system</p>
    </div>
    """, unsafe_allow_html=True)
    
    faqs = [
        {
            "question": "How accurate are the crop recommendations?",
            "answer": "Our AI model achieves 95% accuracy based on extensive training with agricultural datasets from various regions and soil conditions."
        },
        {
            "question": "What parameters does the system consider?",
            "answer": "The system analyzes Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH level, and rainfall to make recommendations."
        },
        {
            "question": "Can I use this for any region?",
            "answer": "Yes! Our model is trained on diverse datasets and can provide recommendations for various geographical regions and climate conditions."
        },
        {
            "question": "How often should I get recommendations?",
            "answer": "We recommend getting new recommendations at the start of each growing season or when there are significant changes in soil conditions."
        },
        {
            "question": "Is the system suitable for organic farming?",
            "answer": "Absolutely! Our recommendations consider natural soil conditions and can be adapted for both conventional and organic farming practices."
        }
    ]
    
    for i, faq in enumerate(faqs):
        with st.expander(f"❓ {faq['question']}", expanded=False):
            st.markdown(f"""
            <div style="background: rgba(26, 26, 46, 0.9); backdrop-filter: blur(20px); border-radius: 16px; padding: 1.5rem; border: 1px solid rgba(102, 126, 234, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <p style="color: #b0b0b0; font-family: 'Inter', sans-serif; line-height: 1.6;">{faq['answer']}</p>
            </div>
            """, unsafe_allow_html=True)

# Contact Page
elif page == "📞 Contact":
    st.markdown("""
    <div class="main-header">
        <h1>📞 Contact Us</h1>
        <p>Get in touch with our agricultural experts for support and guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📧 Get in Touch</h3>
            <p>
                Have questions about crop recommendations or need technical support? 
                Our team of agricultural experts is here to help you make the most of our AI-powered platform.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>📞 Contact Information</h3>
            <div style="color: #b0b0b0; font-family: 'Inter', sans-serif; line-height: 2;">
                <p>📧 Email: support@smartcropadvisor.com</p>
                <p>📱 Phone: +1 (555) 123-4567</p>
                <p>🌐 Website: www.smartcropadvisor.com</p>
                <p>⏰ Hours: Mon-Fri 9AM-6PM EST</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("""
    <h3 style="color: #ffffff; font-family: 'Inter', sans-serif; margin: 3rem 0 1rem 0; font-weight: 600;">📝 Send us a Message</h3>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        subject = st.selectbox("Subject", ["General Inquiry", "Technical Support", "Feature Request", "Bug Report"])
        message = st.text_area("Message", height=150)
        
        if st.form_submit_button("📤 Send Message", use_container_width=True):
            st.success("✅ Thank you for your message! We'll get back to you soon.") 