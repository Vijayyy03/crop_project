import streamlit as st
import numpy as np
import pickle

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

# Streamlit app layout and styling
st.set_page_config(page_title="AgroCulture", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Helvetica', sans-serif;
        }
        .stButton>button {
            background-color: #3a9bdc;
            color: #ffffff;
            border-radius: 25px;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 20px rgba(58, 155, 220, 0.5);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2a7eb7;
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(58, 155, 220, 0.8);
        }
        .stTextInput>div>input {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #3a9bdc;
            border-radius: 8px;
            padding: 12px 20px;
            font-size: 16px;
            transition: 0.3s;
        }
        .stTextInput>div>input:focus {
            border: 1px solid #ff9100;
            box-shadow: 0 0 8px rgba(255, 145, 0, 0.8);
        }
        .home-header {
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #3a9bdc, #2a7eb7);
            color: white;
            border-radius: 15px;
            box-shadow: 0 6px 15px rgba(58, 155, 220, 0.3);
        }
        .home-header h1 {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .home-header p {
            font-size: 1.2rem;
            margin-bottom: 40px;
        }
        .cta-button {
            background-color: #ff9100;
            color: #fff;
            padding: 20px 40px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 25px;
            transition: 0.3s;
            box-shadow: 0 4px 20px rgba(255, 145, 0, 0.6);
        }
        .cta-button:hover {
            background-color: #ff5722;
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(255, 87, 34, 0.8);
        }
        .section {
            margin-top: 40px;
        }
        .section h2 {
            font-size: 2rem;
            text-align: center;
            color: #ff9100;
        }
        .section p {
            font-size: 1.1rem;
            text-align: center;
            color: #ddd;
            margin-top: 10px;
        }
        .feature-list {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        .feature-item {
            background-color: #333;
            margin: 10px;
            padding: 20px;
            border-radius: 10px;
            width: 250px;
            text-align: center;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }
        .feature-item h3 {
            font-size: 1.5rem;
            color: #ff9100;
        }
        .feature-item p {
            color: #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Home", "Crop Recommendation", "FAQ", "Contact"])

#HOME PAGE
def redirect_to_recommendation():
    st.session_state.page = "Crop Recommendation"

    
if page == "Home":
    st.markdown("""
    <div class="home-header">
        <h1>🌾Crop Recommendation System</h1>
        <p>Harness the power of AI to predict the best crops for your region and soil conditions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    ### Introduction
    Our system provides personalized crop recommendations based on the soil and weather conditions you provide. 
    Using advanced machine learning techniques, the app processes key data points and suggests the most optimal crop that would thrive in your region. 
    Whether you're a farmer or an agricultural researcher, this tool can help boost crop yield and support sustainable farming practices.
    """)
    
    st.write("""
    ### How It Works:
    The app takes user inputs like Nitrogen, Phosphorus, Potassium content, temperature, humidity, rainfall, and soil pH. These inputs are processed by our machine learning models to recommend the best-suited crop based on historical agricultural data. The system ensures recommendations are scientifically accurate and timely.
    """)
    
    st.write("""
    ### Key Features:
    - **AI-Driven Predictions**: Predict the most suitable crops using state-of-the-art machine learning models.
    - **Real-Time Results**: Get crop recommendations in just a few seconds.
    - **User-Friendly Interface**: A simple, clean design makes it easy for anyone to use, regardless of technical expertise.
    - **Sustainability Focused**: Support sustainable farming practices by recommending crops that are suited for the local environment and climate.
    - **Wide Range of Crops**: From grains like Rice to fruits like Mango, our system supports a variety of crops.
    """)

   

    # Styling and Feature Showcase
    st.write("### Features of Our Crop Recommendation System:")

    st.markdown("""
    <div class="feature-list">
        <div class="feature-item">
            <h3>AI Predictions</h3>
            <p>Our system uses powerful machine learning models to predict the most suitable crops based on input data.</p>
        </div>
        <div class="feature-item">
            <h3>Quick Results</h3>
            <p>Get accurate crop recommendations within seconds, helping farmers make better decisions faster.</p>
        </div>
        <div class="feature-item">
            <h3>User-Friendly</h3>
            <p>The interface is simple, intuitive, and accessible to anyone, even with minimal tech experience.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # # Adding the Call to Action button with CSS for better look
    # st.markdown("""
    # <div style="text-align: center;">
    #     <button class="cta-button" onclick="window.location.href='/Crop Recommendation'">Start Crop Recommendation</button>
    # </div>
    # """, unsafe_allow_html=True)

    # Enhanced CSS for Styling
    st.markdown("""
    <style>
        /* Styling for the page */
        body {
            font-family: 'Helvetica', sans-serif;
            background-color: #fafafa;
            color: #333;
        }

        .home-header {
            background: linear-gradient(135deg, #ff9100, #3a9bdc);
            color: #fff;
            text-align: center;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .home-header h1 {
            font-size: 2.5rem;
            font-weight: bold;
        }

        .home-header p {
            font-size: 1.3rem;
            margin-top: 10px;
        }

        /* Key Features Styling */
        .feature-list {
            display: flex;
            justify-content: space-around;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        .feature-item {
            background-color: #f2f2f2;
            padding: 20px;
            width: 250px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            text-align: center;
        }

        .feature-item:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        }

        .feature-item h3 {
            color: #ff9100;
            font-size: 1.5rem;
        }

        .feature-item p {
            color: #555;
        }

        /* Call to action button styling */
        .cta-button {
            background-color: #ff9100;
            color: white;
            padding: 15px 30px;
            font-size: 1.2rem;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            transition: 0.3s ease;
            box-shadow: 0 5px 15px rgba(255, 145, 0, 0.3);
        }

        .cta-button:hover {
            background-color: #ff5722;
            box-shadow: 0 8px 25px rgba(255, 87, 34, 0.5);
            transform: scale(1.05);
        }
    </style>
    """, unsafe_allow_html=True)


# FAQ page content with collapsible answers
elif page == "FAQ":
    st.markdown("<h2 class='faq-header'>Frequently Asked Questions (FAQ)</h2>", unsafe_allow_html=True)

    faq_data = [
        {"question": "What is the purpose of this system?", "answer": "This system recommends the best crop for cultivation based on your soil and weather data using machine learning."},
        {"question": "How do I use this crop recommendation system?", "answer": "You can input your soil's nitrogen, phosphorus, potassium levels, temperature, humidity, and rainfall to get the best crop recommendation."},
        {"question": "Is the recommendation always accurate?", "answer": "While the system uses accurate machine learning models, the recommendations are based on the input data. Variations in actual conditions may affect outcomes."},
        {"question": "How is the system trained?", "answer": "The system is trained on historical agricultural data to predict the most suitable crops for various conditions."},
        {"question": "Can I use this system for different regions?", "answer": "Yes! This system is designed to work with global regions as long as the correct environmental data is provided."},
        {"question": "What kind of crops can be recommended?", "answer": "The system supports a wide variety of crops, including grains like rice and maize, fruits like mango, banana, and coconut, and pulses like lentil and chickpea."},
        {"question": "Do I need technical knowledge to use this system?", "answer": "No, the system is designed to be user-friendly, and no technical expertise is needed. Just input your soil and weather data, and get the recommendations instantly."},
        {"question": "How is the data processed?", "answer": "Your input data is processed using machine learning algorithms, which analyze historical data and provide a prediction based on conditions similar to yours."},
        {"question": "Can I use this system for small-scale farming?", "answer": "Yes! The system can be used by both large and small-scale farmers. It helps make data-driven decisions for crop selection."},
        {"question": "Is the system free to use?", "answer": "Yes, the system is free for use as part of our goal to support sustainable farming practices globally."},
        {"question": "Can the system predict multiple crops for the same region?", "answer": "Currently, the system recommends one crop at a time based on the provided data. However, in the future, we aim to offer suggestions for multiple crops."},
        {"question": "How often should I update the input data?", "answer": "We recommend updating the input data whenever there are significant changes in soil composition or weather conditions for more accurate results."},
        {"question": "What should I do if I see an error or issue with the system?", "answer": "If you encounter an error, please contact us through the Contact page, and we will work to resolve the issue promptly."}
    ]

    for faq in faq_data:
        with st.expander(faq['question']):
            st.write(faq['answer'])

    st.markdown("<hr/>", unsafe_allow_html=True)

    #contact page

    # Contact page content with a clean 3D layout and interactive form
elif page == "Contact":
    st.markdown("""
    <style>
        .contact-header {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #fff;
            background: linear-gradient(135deg, #3a9bdc, #2a7eb7);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(58, 155, 220, 0.3);
        }

        .contact-form {
            background-color: #222;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.3);
            margin-top: 30px;
        }

        .contact-form input, .contact-form textarea {
            background-color: #333;
            border: 1px solid #3a9bdc;
            border-radius: 10px;
            color: #fff;
            font-size: 1rem;
            padding: 12px;
            width: 100%;
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
        }

        .contact-form input:focus, .contact-form textarea:focus {
            border: 1px solid #ff9100;
            box-shadow: 0 0 8px rgba(255, 145, 0, 0.6);
            transform: scale(1.05);
        }

        .contact-form button {
            background-color: #ff9100;
            color: #fff;
            font-size: 1.1rem;
            padding: 15px 30px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 15px rgba(255, 145, 0, 0.4);
        }

        .contact-form button:hover {
            background-color: #ff5722;
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(255, 87, 34, 0.6);
        }

        .contact-details {
            margin-top: 30px;
            text-align: center;
            font-size: 1.2rem;
            color: #ddd;
        }

        .contact-details p {
            margin-top: 15px;
        }

        .contact-location {
            text-align: center;
            margin-top: 30px;
            color: #ddd;
        }

        .contact-location h4 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #ff9100;
        }

        .contact-location p {
            font-size: 1.1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header section with clean 3D design
    st.markdown("<div class='contact-header'>Contact Us</div>", unsafe_allow_html=True)
    
    st.write("""
    We're here to help! If you have any questions, suggestions, or feedback, feel free to reach out to us. We're always happy to assist.
    """)
    
    st.write("### Contact Form")

    # Contact form
    contact_form = """
    <div class="contact-form">
        <form action="https://formsubmit.co/thatquotes92@gmail.com" method="POST">
            <div>
                <label for="name" style="color: #fff; font-size: 1.1rem;">Full Name:</label>
                <input type="text" name="name" required placeholder="Enter your full name">
            </div>
            <div>
                <label for="email" style="color: #fff; font-size: 1.1rem;">Email:</label>
                <input type="email" name="email" required placeholder="Enter your email address">
            </div>
            <div>
                <label for="message" style="color: #fff; font-size: 1.1rem;">Message:</label>
                <textarea name="message" required placeholder="Write your message here" rows="5"></textarea>
            </div>
            <div style="text-align: center;">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)

    # Alternative contact information section with clean design
    st.markdown("<div class='contact-details'>", unsafe_allow_html=True)
    st.write("""
    ### Alternative Ways to Reach Us:
    If you'd prefer, you can reach out to us via the following channels:
    - **Email**: thatquotes92@gmail.com
    - **Phone**: +123 456 7890
    - **Social Media**: @AgroCulture (Twitter, Facebook, LinkedIn)

    We’re excited to hear from you and will get back to you as soon as possible!
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Location section (Optional for a more detailed contact page)
    st.markdown("<div class='contact-location'>", unsafe_allow_html=True)
    st.write("""
    ### Our Office Location:
    You can also visit us at our office located at:

    📍 **Farming Solutions HQ**
    123 Greenfield Avenue, Suite 400
    Tech Park, AgriCity, Country

    We’re open from Monday to Friday, 9 AM to 5 PM (GMT).
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<hr/>", unsafe_allow_html=True)




# Crop recommendation page content (No change)
elif page == "Crop Recommendation":
    st.title("🌱 Crop Recommendation System")
    st.write("Enter the soil and weather conditions below to get the recommended crop for optimal yield.")

    # Input fields in a two-column structured layout
    col1, col2 = st.columns(2)
    with col1:
        N = float(st.text_input("Nitrogen Content (N)", value="50", key="nitrogen"))
        P = float(st.text_input("Phosphorus Content (P)", value="50", key="phosphorus"))
        K = float(st.text_input("Potassium Content (K)", value="50", key="potassium"))
        ph = float(st.text_input("Soil pH Level", value="7.0", key="ph"))

    with col2:
        temp = float(st.text_input("Temperature (°C)", value="25.0", key="temperature"))
        humidity = float(st.text_input("Humidity (%)", value="50.0", key="humidity"))
        rainfall = float(st.text_input("Rainfall (mm)", value="100.0", key="rainfall"))

    # Prediction button
    if st.button("🔍 Predict Crop"):
        # Prepare features for prediction
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale the input features
        try:
            mx_features = mx.transform(single_pred)
            sc_mx_features = sc.transform(mx_features)
            prediction = model.predict(sc_mx_features)

            # Determine crop based on prediction
            if prediction[0] in crop_dict:
                crop = crop_dict[prediction[0]]
                st.markdown("""
    <style>
        /* Styling for the prediction result */
        .result {
            background: linear-gradient(135deg, #FFBC99, #FF9E80);  /* Peach gradient */
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            transition: all 0.3s ease;
            opacity: 0;
            animation: fadeInUp 1s forwards, bounce 1s ease infinite;
        }

        .result h3 {
            font-size: 2rem;
            font-weight: bold;
        }

        .result p {
            font-size: 1.1rem;
            margin-top: 10px;
        }

        /* Keyframe for fade-in effect */
        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Keyframe for bounce effect */
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        /* Button Styling */
        .stButton>button {
            background-color: #FF7043; /* Peachy coral */
            color: white;
            font-size: 1.2rem;
            padding: 12px 25px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(255, 112, 67, 0.3);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #FF5722; /* Deeper peach */
            box-shadow: 0 8px 25px rgba(255, 87, 34, 0.5);
            transform: scale(1.05);
        }

        /* Spinner for loading */
        .stSpinner {
            color: #FF7043; /* Peachy coral */
        }
    </style>
""", unsafe_allow_html=True)

                st.markdown(f"<div class='result'>{crop} is the best crop to be cultivated with the given conditions. 🌱</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Sorry, we could not determine the best crop with the provided data.")
        except Exception as e:
            st.error(f"❌ An error occurred during prediction: {e}")
        