import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


class Shopping:
    def __init__(self, data):
        self.data = data
        if "cart" not in st.session_state:
            st.session_state.cart = {}

    # added img_url
    def scan_muffin(self):
        item_index = 0
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        img_url = self.data.iloc[item_index]["img_url"]

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += 1
            st.session_state.cart[item_index][3] += item_price
        else:
            st.session_state.cart[item_index] = [
                item_name,
                1,
                item_price,
                item_price * 1,
                img_url,
            ]

    def scan_water(self):
        item_index = 1
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        img_url = self.data.iloc[item_index]["img_url"]

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += 1
            st.session_state.cart[item_index][3] += item_price
        else:
            st.session_state.cart[item_index] = [
                item_name,
                1,
                item_price,
                item_price * 1,
                img_url,
            ]

    def scan_protein_powder(self):
        item_index = 2
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        img_url = self.data.iloc[item_index]["img_url"]

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += 1
            st.session_state.cart[item_index][3] += item_price
        else:
            st.session_state.cart[item_index] = [
                item_name,
                1,
                item_price,
                item_price * 1,
                img_url,
            ]

    def scan_coffee(self):
        item_index = 3
        item_name = self.data.iloc[item_index]["Title"]
        item_price = self.data.iloc[item_index]["Price"]
        img_url = self.data.iloc[item_index]["img_url"]

        if item_index in st.session_state.cart:
            st.session_state.cart[item_index][1] += 1
            st.session_state.cart[item_index][3] += item_price
        else:
            st.session_state.cart[item_index] = [
                item_name,
                1,
                item_price,
                item_price * 1,
                img_url,
            ]

    def remove_muffin(self):
        item_index = 0
        item_price = self.data.iloc[item_index]["Price"]
        try:
            if st.session_state.cart[item_index][1] > 1:
                st.session_state.cart[item_index][1] -= 1
                st.session_state.cart[item_index][3] -= item_price
            else:
                del st.session_state.cart[item_index]
        except:
            pass

    def remove_water(self):
        item_index = 1
        item_price = self.data.iloc[item_index]["Price"]
        try:
            if st.session_state.cart[item_index][1] > 1:
                st.session_state.cart[item_index][1] -= 1
                st.session_state.cart[item_index][3] -= item_price
            else:
                del st.session_state.cart[item_index]
        except:
            pass

    def remove_protein_powder(self):
        item_index = 2
        item_price = self.data.iloc[item_index]["Price"]
        try:
            if st.session_state.cart[item_index][1] > 1:
                st.session_state.cart[item_index][1] -= 1
                st.session_state.cart[item_index][3] -= item_price
            else:
                del st.session_state.cart[item_index]
        except:
            pass

    def remove_coffee(self):
        item_index = 3
        item_price = self.data.iloc[item_index]["Price"]
        try:
            if st.session_state.cart[item_index][1] > 1:
                st.session_state.cart[item_index][1] -= 1
                st.session_state.cart[item_index][3] -= item_price
            else:
                del st.session_state.cart[item_index]
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
            cart_html = ""  # dynamic html placeholder
            running_total = 0
            # for each item create div elements to show in cart

            for item, details in st.session_state.cart.items():
                name = details[0]
                quantity = details[1]
                price = details[2]
                total = quantity * price
                img_url = details[4]
                running_total += price

                cart_html += f"""<div class="cart-item">
                <div class="item-details">
                    <div class="item-name">{name}</div>
                    <div class="item-quantity">Quantity: {quantity}</div>
                    <img src="{img_url}" alt="{name}" style="width:50px;height:50px;" />
                </div>
                <div class="item-total">${total:.2f}</div>
                </div>"""

            # mobile screen checkout
            components.html(
                f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Shopping List</title>
                <style>
                    head {{
                        bottom: 300px;
                    }}
                    title {{
                        font-size: 20px;
                        align-items: left;
                    }}
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #0f1117;
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
                        color: #232B2B;
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
                        background-color: #0B1C72;
                    }}
                </style>
            </head>
            <body>
                <div class="mobile-container">
                    <h3>Shopping List</h3>

                    <!-- Cart items inserted here -->
                    {cart_html}

                    <!-- Total Amount -->
                    <div class="cart-summary">
                        Total: ${running_total:.2f}
                    </div>

                    <button class="checkout-button">Pay via Card</button>
                    <button class="checkout-button">Pay via Pole</button>
                </div>
            </body>
            </html>
            """,
                height=800,
                scrolling=False,
            )
        else:
            cart_html = f"""<div class="cart-item">
                <div class="item-details">
                    <div class="item-name">You do not have any items in cart.</div>
                </div>
                </div>"""

            components.html(
                f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Shopping List</title>
                <style>
                    title {{
                        font-size: 20px;
                        align-items: left;
                    }}
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #0f1117;
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
                    <h3>Shopping List</h3>

                    <!-- Cart items inserted here -->
                    {cart_html}
                </div>
            </body>
            </html>
            """,
                height=800,
                scrolling=False,
            )


# test run (following section only used when testing buttons.py alone)
if __name__ == "__main__":
    data = "Grocery_Dataset.csv"
    df = pd.read_csv(data)
    basket = Shopping(df)

    st.markdown(
        """
        <style>
        .stButton>button {
            padding: 2px 2px;
            font-size: 28px;
            margin: 1px 1px;
            cursor: pointer;
            background-color: #0f1117;
            color: #282828;
            border: 0px;
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

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            if st.button("1"):
                st.session_state["action"] = "Scanned choc muffin."
                basket.scan_muffin()
            if st.button("5"):
                st.session_state["action"] = "Removed choc muffin."
                basket.remove_muffin()

        with col2:
            if st.button("2"):
                st.session_state["action"] = "Scanned bottled water."
                basket.scan_water()
            if st.button("6"):
                st.session_state["action"] = "Removed bottled water."
                basket.remove_water()

        with col3:
            if st.button("3"):
                st.session_state["action"] = "Scanned protein powder."
                basket.scan_protein_powder()
            if st.button("7"):
                st.session_state["action"] = "Removed protein powder."
                basket.remove_protein_powder()

        with col4:
            if st.button("4"):
                st.session_state["action"] = "Scanned coffee."
                basket.scan_coffee()
            if st.button("8"):
                st.session_state["action"] = "Removed coffee."
                basket.remove_coffee()

        with col5:
            if st.button("c"):
                st.session_state["action"] = "Cleared cart..."
                basket.clear()

    # current action
    if "action" in st.session_state:
        st.write(f"Status: {st.session_state['action']}")
    else:
        st.write("No action taken yet.")

    basket.format()
