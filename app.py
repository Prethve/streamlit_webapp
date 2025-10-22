import streamlit as st
import mylibrary

if "shoe" not in st.session_state:
    st.session_state["shoe"] = "value"
if "checked_out" not in st.session_state:
    st.session_state["checked_out"] = False


# Defining the Pages
marketplace = st.Page("pages/marketplace.py", title="Marketplace", default=True)
# trending = st.Page("pages/trending.py", title="Flash Sale")
# listing = st.Page("pages/my_listing.py", title="My Listings")
profile = st.Page("pages/my_profile.py", title="My Profile")


pages = {
    "Search": [marketplace],
    "Pages": [profile],
}

navbar = st.navigation(pages, position="sidebar")
navbar.run()

# with st.sidebar:
#     st.divider()
#     if not st.user.is_logged_in:
#         if st.button("Log in", icon=":material/login:"):
#             st.login("google")
#         st.stop()

#     if st.button("Log out", icon=":material/logout:"):
#         st.logout()
