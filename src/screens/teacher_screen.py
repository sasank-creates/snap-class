import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    

    teacher_screen_login()
    
def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="large")  # ✅ fixed indentation
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace")
    
    st.markdown("""
                <h2 style='color:black !important; text-align:center;'>
                    Login using password
                </h2>  
            """, unsafe_allow_html=True)    
    st.write("")                                             # ✅ st.space() doesn't exist
    st.write("")
    
    teacher_username = st.text_input("Enter username", placeholder="Enter your username here")
    teacher_password = st.text_input("Enter password", placeholder="Enter your password here", type="password")
    
    st.divider()
    footer_dashboard()

def teacher_screen_register():                               # ✅ fixed capital S typo
    c1, c2 = st.columns(2, vertical_alignment="center", gap="large")  # ✅ fixed indentation
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home", type="secondary", key="registerbackbtn", shortcut="control+backspace")  # ✅ unique key