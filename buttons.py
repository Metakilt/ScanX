import streamlit as st
import pandas as pd
import random
import boto3
from io import BytesIO


class Shopping:
    def __init__(self, data):
        self.data = data
        if "cart" not in st.session_state:
            st.session_state.cart = {}

    def scan_1(self):
        item_index = random.choice(self.data.index)
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        # self.cart[self.data.iloc[item]['Title']] = [1, self.data.iloc[item]['Price'], self.data.iloc[item]['Price']*1]
        if item_name in st.session_state.cart:
            st.session_state.cart[item_name][0] += 1
            st.session_state.cart[item_name][2] += item_price
        else:
            st.session_state.cart[item_name] = [1, item_price, item_price * 1]

    def scan_2(self):
        item_index = random.choice(self.data.index)
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        randomiser = random.randint(2, 5)
        # self.cart[self.data.iloc[item]['Title']] = [1*randomiser, self.data.iloc[item]['Price'], self.data.iloc[item]['Price']*randomiser]
        if item_name in st.session_state.cart:
            st.session_state.cart[item_name][0] += randomiser
            st.session_state.cart[item_name][2] += item_price * randomiser
        else:
            st.session_state.cart[item_name] = [
                1 * randomiser,
                item_price,
                item_price * randomiser,
            ]

    def remove(self):
        try:
            st.session_state.cart.popitem()
        except:
            pass

    def clear(self):
        try:
            st.session_state.cart.clear()
        except:
            pass

    def total(self):
        return round(sum(price[2] for price in st.session_state.cart.values()), 2)

    def format(self):
        """result = ""
        if len(self.cart) != 0:
            for item, value in self.cart.items():
                quantity = value[0]
                price = value[1]
                item_total = value[2]
                result += f"{item:<10} Quantity: {quantity:<10} Price: {price:<10} Total: {item_total}\n"
            return result
        else:
            result+='Nothing in cart.'
            return result"""

        if st.session_state.cart:
            for item, details in st.session_state.cart.items():
                st.write(
                    f"{item}, Quantity: {details[0]}, Price: {details[1]}, Total: {details[2]}"
                )
        else:
            st.write("Cart is empty.")


def access_bucket(bucket_name, bucket_obj):
    session = boto3.Session()

    s3 = session.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=bucket_obj)
    response_data = response["Body"].read()

    data = BytesIO(response_data)
    return data


if __name__ == "__main__":
    data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    df = pd.read_csv(data)
    basket = Shopping(df)

    st.markdown(
        """
        <style>
        .stButton>button {
            padding: 10px 15px;
            font-size: 28px;
            margin: 1px 1px;
            cursor: pointer;
        }

        .stButton {
            display: inline-block;
            width: 100%;
        }

        .stButton .fullWidth {
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Customer Actions")

    with st.container():
        st.write("What do you want to do?")
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            if st.button("SCAN ITEM"):
                st.session_state["action"] = "Scanned one item..."
                basket.scan_1()
        with col2:
            if st.button("SCAN ITEM++"):
                st.session_state["action"] = (
                    "Scanned an item with multiple quantities..."
                )
                basket.scan_2()
        with col3:
            if st.button("REMOVE ITEM"):
                st.session_state["action"] = "Removed an item..."
                basket.remove()
        with col4:
            if st.button("CLEAR CART"):
                st.session_state["action"] = "Cleared cart..."
                basket.clear()

    # current action
    if "action" in st.session_state:
        st.write(f"Status: {st.session_state['action']}")
    else:
        st.write("No action taken yet.")

    basket.format()
    st.write(f"Shopping Total: ${basket.total()}")
