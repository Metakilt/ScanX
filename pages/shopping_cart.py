import streamlit as st
import pandas as pd
from buttons import Shopping, access_bucket  # Importing from buttons.py


def shopping_cart():
    st.title("Shopping Cart Items")

    # Access data from the S3 bucket
    data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    df = pd.read_csv(data)

    # Initialize the Shopping basket from buttons
    basket = Shopping(df)

    # Buttons from buttons.py
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("SCAN ITEM"):
                basket.scan_1()
                st.write("Item scanned.")

        with col2:
            if st.button("SCAN ITEM+"):
                basket.scan_2()
                st.write("Multiple quantities scanned.")

        with col3:
            if st.button("REMOVE ITEM"):
                basket.remove()
                st.write("Item removed.")

        # Added separately because 4 columns destroys the css might fix later
        if st.button("Clear Cart"):
            basket.clear()
    # call table
    basket.format()

    # Pay now button not working with navbar package, link straight with switchpage instead
    # Use markdown to center div with flex html. Check if button onclick can work in streamlit
    with st.container():
        if st.button("PAY NOW"):
            st.session_state["current_page"] = "Pay Now"
