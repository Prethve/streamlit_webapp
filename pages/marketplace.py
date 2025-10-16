import streamlit as st
import mylibrary

if not st.user.is_logged_in:
    with st.container(horizontal_alignment='center', key='title', width='stretch'):
        mylibrary.title_text('Welcome To Sneako', 'kafsdfj askjdfa;klsdjf ajsfaskdjfaksd fjas;iejasgl;kjakdsgjklahsdguhdfjkghskdfhga sdfghaouks hasdv')

    col1, col2, col3 = st.columns(3, width='stretch', border=True)
    with st.container(horizontal_alignment='center', key='features', width='stretch'):
        with col1:
            mylibrary.column('Unbeatable Deals', 'asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh')
        
        with col2:
            mylibrary.column('Diverse Collection', 'asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh')
        
        with col3:
            mylibrary.column('Convenient Shopping', 'asdgfhj fasdfa gdfhsdfghdfhsdf shf sdfsdfg hfh')

else:
    with st.container(horizontal_alignment='center', key='main-container', width='stretch'):
        st.title(f'Welcome, {st.user.name}!', anchor=None, help=None)
        shoe_db = mylibrary.extract_data()


        num_columns = 3
        columns = st.columns(num_columns, width='stretch')

        for i, (key, value) in enumerate(shoe_db.items()):
            with columns[i % num_columns]: # Distribute tiles across columns
                tile_cont = st.container(height='stretch' ,border=True)
                tile_cont.text(key)
                tile_cont.subheader(f"{value['price']}") # Use the dictionary key as a tile title
                tile_cont.caption(f"{value['brand']}")
            
        
        
        
        # st.text_input("Enter the quantity of African Oranges $2 each", key="oranges")
        # st.number_input("Enter the quantity of Fuji Apples $3 each", min_value=0, max_value=10, step=1, key="apples")
        # st.slider("How many plastic bags do you want", min_value=0, max_value=3, step=1, key="bags")
        # bags_cost = mylibrary.plastic_bags_price(st.session_state.bags)
        # st.write("Your plastic bags will cost $" + str(bags_cost))

        # if st.button('Get Total'):
        #     st.write('Calculating Your Total ...')
        #     oranges = int(st.session_state.oranges)
        #     apples = int(st.session_state.apples)
        #     result = mylibrary.calculate_total(oranges, apples)
        #     total = bags_cost + result
        #     st.write('Please pay {:.2f}'.format(total))
        # else:
        #     st.write('Please Key In The Quantity')




