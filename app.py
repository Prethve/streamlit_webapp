import streamlit as st
import mylibrary

if "shoe" not in st.session_state:
    st.session_state["shoe"] = "value"
if "checked_out" not in st.session_state:
    st.session_state["checked_out"] = False


# Defining the Pages
marketplace = st.Page("pages/marketplace.py", title="Marketplace", default=True)
profile = st.Page("pages/my_profile.py", title="My Profile")


pages = {
    "Search": [marketplace],
    "Pages": [profile],
}

navbar = st.navigation(pages, position="sidebar")
navbar.run()
