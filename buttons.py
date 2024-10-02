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
        if st.session_state.cart:
            items = []
            for item, details in st.session_state.cart.items():
                items.append(
                    {
                        "Item": item,
                        "Quantity": details[0],
                        "Price": details[1],
                        "Total": details[0] * details[1],
                    }
                )
            cart_display = pd.DataFrame(items)

            # CSS for the table
            css = """
        <style>
            .table {
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1em;
                font-family: Arial, sans-serif;
                min-width: 400px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }
            .table th, .table td {
                padding: 12px 15px;
                text-align: center;
                border-bottom: 1px solid #dddddd;
            }
            .table th {
                background-color: #ffd500;
                color: white;
                text-align: center;
            }
            .table tr:nth-child(even) {
                background-color: #f2f2f2;
                text-align:center;
            }
            .table tr:hover {
                background-color: #f1f1f1;
            }
        </style>
    """.strip()
            st.markdown(css, unsafe_allow_html=True)
            html_table = cart_display.to_html(classes="table", index=False)
            st.markdown(html_table, unsafe_allow_html=True)
            # st.write(
            #     cart_display.to_html(classes="table", index=False),
            #     unsafe_allow_html=True,
            # )
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
    st.write(f"Shmpping Total: ${basket.total()}")
