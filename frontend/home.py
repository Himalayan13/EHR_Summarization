import streamlit as st
import requests

def home():
    st.markdown(
        """
        <style>
        .stApp { background: linear-gradient(to right, #6b4f4f, #854442); }
        div[data-testid="stFileUploader"] {
            width: 80% !important;
            margin: auto !important;
            border: 3px dashed #fff4e6 !important;
            border-radius: 20px !important;
            background-color: rgba(255, 244, 230, 0.2) !important;
            padding: 40px !important;
            text-align: center !important;
            transition: 0.3s ease-in-out;
        }
        div[data-testid="stFileUploader"]:hover {
            background-color: rgba(255, 244, 230, 0.3) !important;
            border: 3px solid #fff4e6 !important;
        }
        div[data-testid="stFileUploader"] label {
            font-size: 20px !important;
            color: #fff4e6 !important;
            font-weight: bold !important;
            text-align: center !important;
        }
        div[data-testid="stFileUploaderDropzone"] {
            color: #fff4e6 !important;
            font-weight: bold !important;
            font-size: 18px !important;
        }
        .summary-box {
            background: rgba(255, 244, 230, 0.2);
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            color: #fff4e6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style='text-align: center; color: #fff4e6;'>EHR Summarization 📄</h1>
        <p style='text-align: center; color: #fff4e6; font-size: 18px;'>
            Upload a prescription PDF to get a concise summary of its contents.
        </p>
        """, unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload Prescription PDF", type=["pdf"])

    if uploaded_file:
        files = {"file": uploaded_file.getvalue()}
        
        with st.spinner('Summarizing... Please wait...'):
            response = requests.post("http://127.0.0.1:5000/summarize", files=files)

        if response.status_code == 200:
            st.markdown(
                f"""
                <div class='summary-box'>
                    <h2>📝 Summary</h2>
                    <p>{response.text}</p>
                    <button onclick="navigator.clipboard.writeText('{response.text}')">📋 Copy</button>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.error("Failed to summarize the document. Please try again.")

def about():
    st.markdown("<h1 style='text-align: center; color: #fff4e6;'>About This App</h1>", unsafe_allow_html=True)
    st.write("This is an AI-powered EHR summarization tool that extracts key insights from prescription PDFs.")

def contact():
    st.markdown("<h1 style='text-align: center; color: #fff4e6;'>Contact</h1>", unsafe_allow_html=True)
    st.write("For inquiries, please reach out at support@ehrsummarization.com.")

def navigation():
    with st.sidebar:
        show_nav = st.checkbox("☰ Toggle Navigation", value=True)

        if show_nav:
            st.markdown("<h2 style='color:#fff4e6;'>Navigation</h2>", unsafe_allow_html=True)
            page = st.radio("", ["📄 Home", "ℹ️ About", "📩 Contact"])
            return page
        else:
            return "📄 Home"

def main():
    page = navigation()
    
    if page == "📄 Home":
        home()
    elif page == "ℹ️ About":
        about()
    elif page == "📩 Contact":
        contact()

if __name__ == "__main__":
    main()