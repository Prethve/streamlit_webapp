import streamlit as st

def calculate_total( oranges, apples):
    return 2*oranges + 3*apples

def plastic_bags_price(bags):
    """one bag 0.1, two bags 0.4, three bags 0.9 """
    return 0.1*bags*bags

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


    