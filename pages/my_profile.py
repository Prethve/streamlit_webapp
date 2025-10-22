import streamlit as st
import mylibrary

db = mylibrary.extract_data()
my_shoes = []

for shoe in db:
    if shoe['seller_username'] == 'seller_02':
        my_shoes.append(shoe)

st.header("My Profile")
tab1, tab2 = st.tabs(['Purchase History', 'My Listings'], width="stretch", default=None)

with tab1:
    history_cont = st.container(
            width="stretch",
            horizontal=True,
            horizontal_alignment="distribute",
            vertical_alignment="center",
            gap="large",
        )
    cols = history_cont.columns([3, 2, 2, 1], gap="small", vertical_alignment="center")
    
    for item in mylibrary.purchase_history:
        # Left: name (flush left)
        with cols[0]:
            left = st.container(horizontal=True, horizontal_alignment="left", width=200)
            left.caption(item.name, width="content")

        # Middle: color (center)
        with cols[1]:
            center = st.container(
                horizontal=True, horizontal_alignment="left", width=50
            )
            center.caption(item.color, width="content")

        with cols[2]:
            center = st.container(
                horizontal=True, horizontal_alignment="center", width=50
            )
            center.caption(item.size, width="content") # Add a remove opttion for the shoes

        # Right: price (flush right)
        with cols[3]:
            right = st.container(
                horizontal=True, horizontal_alignment="right", width=50
            )
            right.caption("{:.2f}".format(item.price), width="content")
    st.divider()

with tab2:
    listing_cont = st.container(
            width="stretch",
            horizontal=True,
            horizontal_alignment="distribute",
            vertical_alignment="center",
            gap="large",
            border=True
        )
    
    cols = st.columns([3, 2, 2, 1], gap="small", vertical_alignment="center")
    
    for item in my_shoes:
        # Left: name (flush left)
        with cols[0]:
            left = listing_cont.container(horizontal=True, horizontal_alignment="left", width=200)
            left.caption(item['shoe_name'], width="content")

        # Middle: color (center)
        with cols[1]:
            center = listing_cont.container(
                horizontal=True, horizontal_alignment="left", width=50
            )
            center.caption(item['color'], width="content")

        with cols[2]:
            center = listing_cont.container(
                horizontal=True, horizontal_alignment="center", width=50
            )
            center.caption(item['size_available'], width="content") # Add a remove opttion for the shoes

        # Right: price (flush right)
        with cols[3]:
            right = listing_cont.container(
                horizontal=True, horizontal_alignment="right", width=50
            )
            right.caption("{:.2f}".format(item['price']), width="content")
    
    