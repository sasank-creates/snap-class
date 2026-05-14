import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.ui.base_layout import style_base_layout

def main():
    st.set_page_config(
        page_title="SnapClass - Making Attendance faster using AI",
        page_icon="https://thumbs.dreamstime.com/b/graduation-hat-icon-design-illustration-academic-cap-icon-apps-websites-yellow-shadow-button-design-graduation-hat-icon-339378358.jpg"
    
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    join_code = st.query_params.get('join-code', None)

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            if join_code:
                st.session_state['pending_join_code'] = join_code
            home_screen()

main()