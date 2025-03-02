import streamlit as st
from home import home
from about import about

# Set page configuration
st.set_page_config(page_title="EHR Summarization", page_icon="📄", layout="centered")

# Custom CSS for Sidebar
st.markdown(
    """
    <style>
    .stSidebar {
        background-color: #4b3832;
        color: #fff4e6;
    }
    .stSidebar .st-radio .st-bj {
        color: #fff4e6;
    }N
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Pane
st.sidebar.markdown(
    """
    <h2 style='color: #fff4e6; text-align: center;'>Navigation</h2>
    """, 
    unsafe_allow_html=True
)
page = st.sidebar.radio("Go to", ["Home", "About"])

# Display selected page
if page == "Home":
    home()
elif page == "About":
    about()