import streamlit as st
import pandas as pd
from buttons import Shopping, access_bucket  # Importing from buttons.py


def shopping_cart():
    st.title("Shopping Cart Items")

    # Access data from the S3 bucket
    data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    df = pd.read_csv(data)

    # Display the shopping cart

    basket = Shopping(df)

    # Buttons from buttons.py
    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("SCAN ITEM"):
                basket.scan_1()
                st.write("Item scanned.")

        with col2:
            if st.button("REMOVE ITEM"):
                basket.remove()
                st.write("Item removed.")

        with col3:
            if st.button("CLEAR CART"):
                basket.clear()
                st.write("Cart cleared.")

        with col4:
            st.write(f"Shopping Total: ${basket.total()}")

    basket.format()
