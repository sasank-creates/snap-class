import streamlit as st

def header_home():
    logo_url = "https://thumbs.dreamstime.com/b/graduation-hat-icon-design-illustration-academic-cap-icon-apps-websites-yellow-shadow-button-design-graduation-hat-icon-339378358.jpg"

    st.markdown(
        f"""
        <div style="display: flex;flex-direction: column;align-items: center;justify-content: center;margin-bottom:30px;">
            <img src="{logo_url}" alt="Logo" style="
            width: 100px;
            height: 100px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(255, 180, 0, 0.5);">
            <h1 style='text-align:center;color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


def header_dashboard():
    logo_url = "https://thumbs.dreamstime.com/b/graduation-hat-icon-design-illustration-academic-cap-icon-apps-websites-yellow-shadow-button-design-graduation-hat-icon-339378358.jpg"

    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; gap:10px;">
            <img src="{logo_url}" alt="Logo" style="
            width: 85px;
            height: 85px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(255, 180, 0, 0.5);">
            <h2 style='text-align:left; color: #58652F !important;'>SNAP<br/>CLASS</h2>
        </div>
        """,
        unsafe_allow_html=True
    )