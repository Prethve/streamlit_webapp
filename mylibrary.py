import streamlit as st
from datetime import datetime
import random
import csv

CSV_PATH = "/Users/deevprethve/Documents/School/SUTD/10.025 Computational Thinking for Design/streamlit_app/shOE_DTB.csv"

# ------------ Cart System (start) -------------------#
cart = []

def checkout_handler():
    if st.session_state["checked_out"] == True and cart:
        cart.clear()
        st.session_state["checked_out"] = False


@st.dialog(
    "Your Cart",
    width="medium",
    on_dismiss=checkout_handler,
)
def display_cart():
    total = 0
    if not cart:
        st.write("Cart is empty")
        return

    for i, item in enumerate(cart):
        cart_cont = st.container(
            width="stretch",
            horizontal=True,
            horizontal_alignment="distribute",
            vertical_alignment="center",
            gap="large",
        )

        # use sized columns so left/middle/right alignment is predictable
        cols = cart_cont.columns(
            [3, 2, 1], gap="large", width="stretch", vertical_alignment="center"
        )

        # Left: name (flush left)
        with cols[0]:
            left = st.container(horizontal=True, horizontal_alignment="left", width=200)
            left.caption(item.name, width="content")

        # Middle: color (center)
        with cols[1]:
            center = st.container(
                horizontal=True, horizontal_alignment="center", width=50
            )
            center.caption(item.color, width="content")

        # Right: price (flush right)
        with cols[2]:
            right = st.container(
                horizontal=True, horizontal_alignment="right", width=50
            )
            right.caption("{:.2f}".format(item.price), width="content")
        total += item.price
    st.divider()
    total_cont = st.container(
        horizontal=True,
        horizontal_alignment="distribute",
        vertical_alignment="center",
        width="stretch",
        height="content",
    )
    if total_cont.button("Checkout", type="tertiary"):
        st.success("Checked Out!")
        st.balloons()
        st.session_state["checked_out"] = True

    total_cont.header(
        "Total: {:.2f}".format(total),
        width="content",
        divider=True,
    )


# --------------- Cart System (end) ------------------- #


# ------------ Shoe Object System (start) ------------- #
class Shoe:
    def __init__(self, name, price, color, brand):
        self.name = name
        self.price = price
        self.color = color
        self.brand = brand

    # To display the info of each shoe in the tiles
    @st.dialog("Item information")
    def item_info(self):
        st.title(
            self.name
        )  # Later ad a string function to remove the colour from the title
        st.header("{:.2f}".format(self.price))
        st.write(self.color)
        st.write(self.brand)
        if st.button("Add to Cart"):
            cart.append(self)
            st.success(f"Added {self.name} to cart.")


# ------------- Shoe Object System (end) -------------#


# IMPORTANT
def bubble_sort_by_price(shoes):
    n = len(shoes)
    # Loop through all elements in the list
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            if shoes[j]["price"] > shoes[j + 1]["price"]:
                # Swap the dictionaries
                shoes[j], shoes[j + 1] = shoes[j + 1], shoes[j]
    # return shoes


# IMPORTANT
def extract_data():
    shoe_db = []
    # Reads CSV File
    with open(CSV_PATH, mode="r") as file:
        csv_file = csv.reader(file)
        # Stored as a list of lists, hence for loop to iterate thorugh every list and convert them into a dictionary
        for lines in csv_file:
            shoe_dict = {
                "shoe_name": lines[0],
                "shoe_id": lines[1],
                "brand": lines[2],
                "size_available": lines[3],
                "price": float(lines[4]),
                "color": lines[5],
                "stock": lines[6],
                "seller_username": lines[7],
            }
            shoe_db.append(shoe_dict)
    return shoe_db


# IMPORTANT
def seasonal_disc(curr_month, curr_day, db):
    # Dictionary of special discount dates (month: day)
    discount_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    discounted_shoes = []  # Stores the whole shoe dict

    # Check if today's date qualifies for discount
    discount = 0
    for month in discount_days:
        if curr_month == month and curr_day == month:
            discount = 0.2  # 20% seasonal discount
            # For loop to decide which shoes to be discounted
            for j in range(0, len(db), len(db) // month):
                # Applies discount and updates DB
                db[j]["price"] = db[j]["price"] * (1 - discount)
                # Collects all discounted shoes data
                discounted_shoes.append(db[j])
    return discount, discounted_shoes


#### Styling functions ####
def title_text(title, caption):
    top_space = '<div style="padding: 50px 10px;"></div>'
    bottom_space = '<div style="padding: 100px 10px;"></div>'
    return {
        st.markdown(top_space, unsafe_allow_html=True),
        st.title(title, anchor=None, help=None, width="content"),
        st.write(caption),
        st.markdown(bottom_space, unsafe_allow_html=True),
    }


# Main Page intro columns
def column(feature, text):
    container = st.container(
        key={feature},
        horizontal_alignment="center",
        vertical_alignment="center",
        width="stretch",
    )
    return {st.header(feature, width="content"), st.caption(text, width="content")}
