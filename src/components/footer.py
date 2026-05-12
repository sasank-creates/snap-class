import streamlit as st

def footer_home():
    logo_url = "https://tse2.mm.bing.net/th/id/OIP.IBsOCRokuQlKbv6yNeNx3wHaB_?pid=Api&P=0&h=180"

    st.markdown(
        f"""
        <div style="margin-top: 2rem; display: flex; justify-content: center; align-items: center; gap: 8px;">
            <p style="margin: 0; padding: 0;">Created with ❤️ by</p>
            <img src="{logo_url}" style="height: 25px; width: auto; vertical-align: middle;"/>
        </div>
        """,
        unsafe_allow_html=True
    )