import streamlit as st
import pandas as pd
from buttons import Shopping, access_bucket  # Importing from buttons.py


def actions():
    st.title("Customer Actions Page")

    # Access data from the S3 bucket
    #data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    data = 'Grocery_Dataset.csv' # local test
    df = pd.read_csv(data)

    # Initialize the Shopping basket from buttons
    basket = Shopping(df)

    # Buttons from buttons.py (no need for st.rewrite since buttons already has this)
    # buttons follow the columns layout of streamlit so needs to be 5 including pay feature.
    # html/css styling in customer action page does not really matter since it's only used in the background
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        # buttons will be changed once specific items are agreed to be brought to presentation
        
        with col1:
            if st.button("SCAN ITEM"):
                basket.scan_1()

        with col2:
            if st.button("SCAN ITEM+"):
                basket.scan_2()

        with col3:
            if st.button("REMOVE ITEM"):
                basket.remove()

        with col4:
            if st.button("CLEAR CART"):
                basket.clear()

        with col5:
            if st.button("PAY NOW"):
                #basket.pay() function for pay to be made in buttons (direct link to pay_screen)
                pass

    st.write(f"Shopping Total: ${basket.total()}")
    # call table
    basket.format()