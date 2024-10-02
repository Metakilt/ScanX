import streamlit as st
import pandas as pd
from buttons import Shopping, access_bucket


def cart():

    st.title("Cart")
    #data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    data = 'Grocery_Dataset.csv' # local test
    df = pd.read_csv(data)

    basket = Shopping(df)
    basket.format_2()