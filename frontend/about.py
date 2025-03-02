import streamlit as st

def about():
    # Background Color
    st.markdown(
        """
        <style>
        .stApp {
            background: #854442;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # About Section
    st.markdown(
        """
        <h1 style='text-align: center; color: #fff4e6;'>
            About EHR Summarization
        </h1>
        <p style='text-align: center; color: #fff4e6; font-size: 18px;'>
            EHR Summarization is a tool that helps in generating concise summaries of medical prescriptions.
            It uses advanced NLP techniques to extract essential information, making it easier for healthcare professionals
            and patients to understand their prescriptions.
        </p>
        <div style='
            background-color: #4b3832;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-top: 30px;
        '>
            <h2 style='color: #fff4e6;'>Features:</h2>
            <ul style='color: #fff4e6; font-size: 16px;'>
                <li>Easy PDF Upload</li>
                <li>Accurate Summarization</li>
                <li>Secure and Confidential</li>
                <li>User-friendly Interface</li>
            </ul>
            <p style='color: #fff4e6;'>
                This project is aimed at enhancing patient care by simplifying the understanding of medical prescriptions.
            </p>
        </div>
        """, unsafe_allow_html=True
    )