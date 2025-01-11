# Home.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Insurance Page Predictor",
    page_icon="✈",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #F0F8FF;
    }
    .main-header {
        font-size: 3rem;
        color: #4CAF50;
        text-align: center;
        margin: 2rem 0;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 2rem;
    }
    .description {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #FFFFFF;
        text-align: justify;
        margin: 1rem auto;
        width: 80%;
    }
    .feature-box {
        background-color: #000000;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem auto;
        width: 80%;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .cta-button {
        display: block;
        width: fit-content;
        margin: 2rem auto;
        padding: 1rem 2rem;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        font-size: 1.2rem;
        border-radius: 25px;
        text-decoration: none;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }
    .cta-button:hover {
        background-color: #45A049;
    }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<h1 class="main-header">✈Selamat Datang di Homepage SAF Prediktor Insurance✈</h1>', unsafe_allow_html=True)

# Sub Header
st.markdown('<h2 class="sub-header">Prediksi data Klaim Polis dengan menggunakan Machine Learning</h2>', unsafe_allow_html=True)

# Description
st.markdown("""
    <div class="description">
        SAF Prediktor Insurance meruapakan sebuah aplikasi dengan memanfaatkan Model Machine Learning
        yang telah dibuat dan dilakukan training, sehingga dapat membantu memprediksi pemegang polis
        berdasarkan data historis untuk menentukan status pemegang polis Klaim/Not Klaim.
    </div>
""", unsafe_allow_html=True)

# Updated "How It Works" section with better contrast
st.markdown("""
    <div class="feature-box" style="background-color: #F0F4F8; color: #000000; border: 1px solid #B0BEC5;">
        <h3>🔍 Bagaimana Cara kerjanya:</h3>
        <ol style="line-height: 1.8;">
            <li><strong>Input Your Data:</strong> Provide petal and sepal measurements through sliders or upload a dataset.</li>
            <li><strong>Predict the Species:</strong> Use our pre-trained machine learning model to classify the Iris flower.</li>
            <li><strong>Analyze Results:</strong> Visualize the predictions with easy-to-understand charts and tables.</li>
        </ol>
    </div>
""", unsafe_allow_html=True)



# Call to Action Button
st.markdown("""
    <a href="3_Input&predict" class="cta-button">🚀 Mulai Prediksi</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer style="text-align:center; margin-top:3rem; font-size:0.9rem;">
        Machine Learning V.1, hubungi Operator jika terjadi kendala ☎
        
    </footer>
""", unsafe_allow_html=True)
