import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):

    st.write("Enter the details of your subject")

    sub_id = st.text_input(
        "Subject Code",
        placeholder="CS101"
    )

    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science"
    )

    sub_section = st.text_input(
        "Section",
        placeholder="A"
    )

    if st.button(
        "Create Subject Now",
        type="primary",
        use_container_width=True 
    ):

        if sub_id and sub_name and sub_section:

            try:

                response = create_subject(
                    sub_id.strip(),
                    sub_name.strip(),
                    sub_section.strip(),
                    teacher_id
                )

                if response:

                    st.toast(
                        "Subject Created Successfully!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Failed to create subject"
                    )

            except Exception as e:

                st.error(f"Error: {str(e)}")

        else:

            st.warning(
                "Please fill all the fields"
            )