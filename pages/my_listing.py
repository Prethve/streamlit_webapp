import streamlit as st
import mylibrary

if not st.user.is_logged_in:
    # Make logic to prompt login to acces this page(optional: redirect to marketpage)
    pass

else:
    with st.container(horizontal_alignment='center', key='main-container', width='stretch'):
        shoe_db = mylibrary.extract_data()
        st.write(shoe_db)