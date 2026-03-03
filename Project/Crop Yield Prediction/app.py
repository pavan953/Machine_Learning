import streamlit as st
import time
import random

st.set_page_config(page_title="Crop Yield Prediction System", layout="wide")

def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        body {
            background: linear-gradient(270deg, #0f2027, #203a43, #2c5364);
            background-size: 600% 600%;
            animation: gradientBG 12s ease infinite;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .glass {
            background: rgba(255, 255, 255, 0.12);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .glass:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.55);
        }

        .hero-title {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 10px;
        }

        .hero-sub {
            font-size: 18px;
            color: #dcdcdc;
            text-align: center;
            margin-bottom: 40px;
        }

        .footer {
            text-align: center;
            color: #cccccc;
            font-size: 14px;
            margin-top: 60px;
            opacity: 0.8;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def sidebar_nav():
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", ["Home", "Predict", "About"])

def hero_section():
    st.markdown(
        """
        <div class="glass">
            <div class="hero-title">Crop Yield Prediction System</div>
            <div class="hero-sub">
                AI-powered agricultural yield estimation using climatic and regional factors
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def input_section():
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.text_input("Area", "India")
        item = st.text_input("Crop Item", "Rice")

    with col2:
        year = st.number_input("Year", min_value=1960, max_value=2030, value=2020)
        rainfall = st.number_input("Average Rainfall (mm/year)", value=800.0)

    with col3:
        pesticides = st.number_input("Pesticides Used (tonnes)", value=150.0)
        temperature = st.number_input("Average Temperature (°C)", value=26.0)

    st.markdown("</div>", unsafe_allow_html=True)
    return area, item, year, rainfall, pesticides, temperature

def dummy_model_prediction(year, rainfall, pesticides, temperature):
    base = (rainfall * 0.4) + (temperature * 12) - (pesticides * 0.2)
    trend = (year - 2000) * 5
    noise = random.uniform(-200, 200)
    return max(0, base + trend + noise)

def result_section(prediction):
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("Predicted Crop Yield")
    st.metric(
        label="Yield (hg/ha)",
        value=f"{prediction:.2f}"
    )
    st.markdown("</div>", unsafe_allow_html=True)

def loading_animation():
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

def footer():
    st.markdown(
        """
        <div class="footer">
            © 2026 Crop Yield Prediction System | Streamlit ML Interface
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    inject_css()
    page = sidebar_nav()

    if page == "Home":
        hero_section()

    elif page == "Predict":
        hero_section()
        area, item, year, rainfall, pesticides, temperature = input_section()
        if st.button("Predict Yield"):
            loading_animation()
            prediction = dummy_model_prediction(year, rainfall, pesticides, temperature)
            result_section(prediction)

    elif page == "About":
        st.markdown(
            """
            <div class="glass">
                This application demonstrates a professional ML frontend for crop yield prediction.
                It uses climatic, agricultural, and regional inputs to estimate yield output.
            </div>
            """,
            unsafe_allow_html=True
        )

    footer()

if __name__ == "__main__":
    main()
