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
    ### 1. Extrating shoes database in a list from csv
    shoe_db = mylibrary.extract_data()

    ### 2. Applying discount prior to Sorting
    discount, discounted_shoes = mylibrary.seasonal_disc(12, 12, shoe_db)

    ### 3. Sorting shoes database through custom bubble sort
    mylibrary.bubble_sort_by_price(shoe_db)

    st.markdown(
        """
    <style>
    div.block-container {
        max-width:1100px; 
    }
    """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.button("Toggle Cart", on_click=mylibrary.display_cart)

    # Brand Filter

    with st.container(
        horizontal_alignment="center", key="main-container", width="stretch"
    ):

        st.title(f"Welcome, {st.user.name}!", anchor=None, help=None)

        ### 4. Managing the filter function
        # 4a. Brand Filter UI (Add a Flash Sale Filter also to show dicounted shoes first)
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
        select_brands = st.segmented_control(
            label="Brand", options=brands, selection_mode="multi", width="stretch"
        )
        st.divider()

        # 4b. Filtering out shoes in database according to user input
        filtered_db = []
        for value in shoe_db:
            if value["brand"] in set(select_brands):
                filtered_db.append(value)

        ### 5. Logic to determine what shoe dateabase is active
        active_db = filtered_db if filtered_db else shoe_db

        ### 6. Displaying filtered out shoes according to user input on the website (IMPORTANT)
        num_columns = 3
        columns = st.columns(num_columns, width="stretch")
        for i, value in enumerate(active_db):

            # Creating a unique shoe object (in memory) for each tile
            shoe = mylibrary.Shoe(
                value["shoe_name"], value["price"], value["color"], value["brand"]
            )
            with columns[i % num_columns]:  # Distribute tiles across columns
                tile_cont = st.container(
                    height=190,
                    border=True,
                    width="stretch",
                    vertical_alignment="distribute",
                )
                tile_cont.metric(
                    label=shoe.name,
                    value="{:.2f}".format(shoe.price),
                    delta=(
                        "{:.0f}%".format(-discount * 100)
                        if value in discounted_shoes
                        else None
                        # This is to randomise the discount to the number of shoes equivalent to the month
                    ),
                    delta_color="inverse",
                )
                bottom = tile_cont.container(
                    horizontal=True,
                    vertical_alignment="center",
                    horizontal_alignment="distribute",
                    width="stretch",
                )
                bottom.caption(f"{shoe.brand}")
                if bottom.button(label="Info", key=value["shoe_id"]):
                    shoe.item_info()
