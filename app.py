import streamlit as st
import mylibrary

# Defining the Pages
marketplace = st.Page('pages/marketplace.py', title='Marketplace')
trending = st.Page('pages/trending.py', title='Trending')

navbar = st.navigation([marketplace, trending], position='sidebar')
navbar.run()

print(st.user.to_dict())

with st.sidebar:
    if not st.user.is_logged_in:
        if st.button("Log in", icon=':material/login:'):
            st.login('google')
        st.stop()

    if st.button("Log out", icon=':material/logout:'):
        st.logout()
            
        
