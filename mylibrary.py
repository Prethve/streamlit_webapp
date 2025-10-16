import streamlit as st
# import pandas as pd
import datetime as date
import csv

CSV_PATH = '/Users/deevprethve/Documents/School/SUTD/10.025 Computational Thinking for Design/streamlit_app/shOE_DTB.csv'

### Key Functions ####

def calculate_total( oranges, apples):
    return 2*oranges + 3*apples

def plastic_bags_price(bags):
    """one bag 0.1, two bags 0.4, three bags 0.9 """
    return 0.1*bags*bags

def discounts():
    today = date.today()
    print(today)

class Shoe:
    def __init__(self, shoe_name, brand, size_available, price, color, stock, seller_username):
        self.shoe_name = shoe_name
        self.brand = brand
        self.size_available = size_available
        self.price = price
        self.color = color
        self.stock = stock
        self.seller_username = seller_username


def extract_data():
    # shoe_db = pd.read_csv(CSV_PATH)
    shoe_db = {}
    with open(CSV_PATH, mode ='r')as file:
        csv_file = csv.reader(file)
        for lines in csv_file:
            shoe_dict = {
                'shoe_name':lines[0],
                'shoe_id':lines[1],
                'brand':lines[2],
                'size_available':lines[3],
                'price':lines[4],
                'color':lines[5],
                'stock':lines[6],
                'seller_username':lines[7],
            }
            shoe_db[lines[0]] = shoe_dict
    return shoe_db #{st.write(shoe_db)}

            

#### Styling functions ####
# Title 

def title_text(title, caption):
    top_space = '<div style="padding: 50px 10px;"></div>'
    bottom_space = '<div style="padding: 100px 10px;"></div>'
    return {
        st.markdown(top_space, unsafe_allow_html=True),
        st.title(title, anchor=None, help=None, width='content'),
        st.write(caption),
        st.markdown(bottom_space, unsafe_allow_html=True)
    }
    
# Main Page intro columns
def column(feature, text):
    container = st.container(key={feature}, horizontal_alignment='center', vertical_alignment='center', width='stretch')
    return {
        st.header(feature, width='content'),
        st.caption(text, width='content')
    }


print(extract_data())
    