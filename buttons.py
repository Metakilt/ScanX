import streamlit as st
import pandas as pd
import random
import boto3
from io import BytesIO
import streamlit.components.v1 as components


class Shopping:
    def __init__(self, data):
        self.data = data
        if "cart" not in st.session_state:
            st.session_state.cart = {}

    def scan_1(self):
        item_index = random.choice(self.data.index)
        item_name = self.data.iloc[item_index]['Title']
        item_price = self.data.iloc[item_index]['Price']

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += 1
            st.session_state.cart[item_index][3] += item_price
        else:
            st.session_state.cart[item_index] = [item_name, 1, item_price, item_price*1]

    def scan_2(self):
        item_index = random.choice(self.data.index)
        item_name = self.data.iloc[item_index]['Title']
        item_price = self.data.iloc[item_index]['Price']
        randomiser = random.randint(2, 5)

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += randomiser
            st.session_state.cart[item_index][3] += item_price*randomiser
        else:
            st.session_state.cart[item_index] = [
                item_name, 
                1*randomiser, 
                item_price, 
                item_price*randomiser
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
        return round(sum(price[3] for price in st.session_state.cart.values()), 2)

    def format(self):
        if st.session_state.cart:
            items = []
            for item, details in st.session_state.cart.items():
                items.append(
                    {
                        "Item": details[0],
                        "Quantity": details[1],
                        "Price": details[2],
                        "Total": details[3],
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
                    background-color: #0F2698;
                    color: white;
                    text-align: center;
                }
                .table tr:nth-child(even) {
                    text-align:center;
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

    def format_2(self):
        if st.session_state.cart:
            cart_html = ""      # dynamic html placeholder
            running_total = 0
            # for each item create div elements to show in cart
            for item, details in st.session_state.cart.items():
                name = item
                quantity = details[0]
                price = details[1]
                total = quantity*price
                running_total += price

                cart_html += f"""<div class="cart-item">
                <div class="item-details">
                    <div class="item-name">{name}</div>
                    <div class="item-quantity">Quantity: {quantity}</div>
                </div>
                <div class="item-total">${total}</div>
                </div>"""
            
            # mobile screen checkout
            components.html(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Checkout Page</title>
                <style>
                    title {{
                        font-size: 20px;
                        align-items: left;
                    }}
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f5f5f5;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        overflow: scroll;
                    }}
                    .mobile-container {{
                        width: 100%;
                        max-width: 375px;
                        background-color: white;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        padding: 20px;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    }}
                    .mobile-container h3 {{
                        text-align: center;
                        font-size: 1.2rem;
                        margin-bottom: 20px;
                    }}
                    .cart-item {{
                        display: flex;
                        justify-content: space-between;
                        padding: 10px 0;
                        border-bottom: 1px solid #eee;
                    }}
                    .cart-item:last-child {{
                        border-bottom: none;
                    }}
                    .cart-item .item-name {{
                        font-weight: bold;
                    }}
                    .cart-item .item-total {{
                        color: #333;
                    }}
                    .cart-item .item-quantity {{
                        color: #999;
                        font-size: 0.9rem;
                    }}
                    .cart-summary {{
                        margin-top: 20px;
                        padding-top: 10px;
                        border-top: 1px solid #eee;
                        font-size: 1.1rem;
                        font-weight: bold;
                    }}
                    .checkout-button {{
                        width: 100%;
                        padding: 15px;
                        margin-top: 20px;
                        background-color: #1330bf;
                        color: white;
                        text-align: center;
                        font-size: 1rem;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }}
                    .checkout-button:hover{{
                        background-color: #B8C0EB;
                        color: #050E39;
                    }}
                </style>
            </head>
            <body>
                <div class="mobile-container">
                    <h3>Checkout</h3>

                    <!-- Cart items inserted here -->
                    {cart_html}

                    <!-- Total Amount -->
                    <div class="cart-summary">
                        Total: ${running_total:.2f}
                    </div>

                    <button class="checkout-button">Proceed to Payment</button>
                </div>
            </body>
            </html>
            """, height=600, scrolling=True)
        else:
            st.write("Cart is empty.")

# pull data from s3
def access_bucket(bucket_name, bucket_obj):
    session = boto3.Session()

    s3 = session.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=bucket_obj)

    response_data = response["Body"].read()

    data = BytesIO(response_data)
    return data

# test run (following section only used when testing buttons.py alone)
if __name__ == "__main__":
    #data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    data = 'Grocery_Dataset.csv' # test local
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
                st.session_state["action"] = "Scanned an item..."
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
