import streamlit as st
import mylibrary

if "shoe" not in st.session_state:
    st.session_state["shoe"] = "value"

# Defining the Pages
marketplace = st.Page("pages/marketplace.py", title="Marketplace", default=True)
trending = st.Page("pages/trending.py", title="Trending")
listing = st.Page("pages/my_listing.py", title="My Listings")
profile = st.Page("pages/my_profile.py", title="My Profile")

if not st.user.is_logged_in:
    pages = {"Search": [marketplace, trending]}
else:
    pages = {"Pages": [profile, listing], "Search": [marketplace, trending]}

navbar = st.navigation(pages, position="sidebar")
navbar.run()

with st.sidebar:
    st.divider()
    if not st.user.is_logged_in:
        if st.button("Log in", icon=":material/login:"):
            st.login("google")
        st.stop()

    if st.button("Log out", icon=":material/logout:"):
        st.logout()
