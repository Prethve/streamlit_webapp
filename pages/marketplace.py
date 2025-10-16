import streamlit as st
import mylibrary

if not st.user.is_logged_in:
    with st.container(horizontal_alignment="center", key="title", width="stretch"):
        mylibrary.title_text(
            "Welcome To Sneako",
            "kafsdfj askjdfa;klsdjf ajsfaskdjfaksd fjas;iejasgl;kjakdsgjklahsdguhdfjkghskdfhga sdfghaouks hasdv",
        )

    col1, col2, col3 = st.columns(3, width="stretch", border=True)
    with st.container(horizontal_alignment="center", key="features", width="stretch"):
        with col1:
            mylibrary.column(
                "Unbeatable Deals", "asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh"
            )

        with col2:
            mylibrary.column(
                "Diverse Collection", "asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh"
            )

        with col3:
            mylibrary.column(
                "Convenient Shopping", "asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh"
            )

else:
    st.markdown(
        """
    <style>
    /* Sidebar container */
    div.block-container {
        max-width:1100px; 
    }
    """,
        unsafe_allow_html=True,
    )
    with st.container(
        horizontal_alignment="center", key="main-container", width="stretch"
    ):
        st.title(f"Welcome, {st.user.name}!", anchor=None, help=None)

        # Original shoes database in a list
        shoe_db = mylibrary.extract_data()
        # Sorted shoes database
        shoe_db = mylibrary.bubble_sort_by_price(shoe_db)
        filtered_db = []

        brands = [
            "ASICS",
            "Adidas",
            "Converse",
            "HOKA",
            "Jordan",
            "New Balance",
            "Nike",
            "On",
            "Puma",
            "Reebok",
            "Saucony",
            "Vans",
        ]
        brands.sort()
        select_brands = st.segmented_control(
            label="Brand", options=brands, selection_mode="multi", width="stretch"
        )
        # Sorting the list of selected shoes based on price
        filtered_db = mylibrary.bubble_sort_by_price(filtered_db)

        # Filtering out shoes according to user input in database
        for value in shoe_db:
            if value["brand"] in set(select_brands):
                filtered_db.append(value)

        num_columns = 3
        columns = st.columns(num_columns, width="stretch")

        # Filtering out shoes according to user input in the website (IMPORTANT)
        for i, value in enumerate(filtered_db if filtered_db else shoe_db):
            with columns[i % num_columns]:  # Distribute tiles across columns
                tile_cont = st.container(
                    height=160,
                    border=True,
                    width="stretch",
                    vertical_alignment="bottom",
                )
                tile_cont.text(value["shoe_name"])
                tile_cont.subheader(
                    f"${value['price']}"
                )  # Use the dictionary key as a tile title
                tile_cont.caption(f"{value['brand']}")
