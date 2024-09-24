import streamlit as st
import pandas as pd
import boto3

with st.container():

    def shopping_cart():
        st.title("Shopping cart items")
        # Change to s3 bucket link
        s3_csv = "Grocery_Dataset.csv"

        # S3 bucket remove comments
        # bucket_name = "itpm-products"
        # file_key = "Grocery_Dataset.csv"
        # make function to read csv from bucket

        if s3_csv is not None:
            df = pd.read_csv(s3_csv)
            st.dataframe(df)

            if "Price" in df.columns:
                total_price = df["Price"].sum()
                st.write(f"Total Price: ${total_price:.2f}")
            else:
                st.write("No price column found in the dataset.")
