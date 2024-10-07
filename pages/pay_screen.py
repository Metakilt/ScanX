import streamlit as st
import pandas as pd
from buttons import Shopping


def pay_screen():
    st.title("Payment Screen")

    st.markdown(
        """
        <style>
        .payment-button {
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
        }
        .payment-button:hover {
            background-color: #B8C0EB;
            color: #050E39;
        }
        .cart-total {
            margin-top: 20px;
            font-size: 1.2rem;
            font-weight: bold;
            text-align: right;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # read csv to display total amount
    df = pd.read_csv("Grocery_Dataset.csv")
    basket = Shopping(df)
    total_amount = basket.total()

    st.markdown(
        f"<div class='cart-total'>Total: ${total_amount:.2f}</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Payment Options")

    col1, col2 = st.columns(2, gap='small')
    with col1:
        if st.button("PayPal", key="paypal", help="Click to pay via Paypal"):
            st.success("Paypal payment initiated.")
    with col2:
        if st.button("AfterPay", key="afterpay", help="Click to pay via AfterPay"):
            st.success("AfterPay payment initiated.")

    st.markdown("#### Or Pay with Credit/Debit Card")

    card_number = st.text_input("Card Number", placeholder="1234 5678 9012 3456")
    exp_date = st.text_input("Expiration Date", placeholder="MM/YY")
    cvv = st.text_input("CVV", placeholder="123", type="password")

    if st.button("Submit Payment", key="submit_payment"):
        if card_number and exp_date and cvv:
            st.success(
                f"Payment of ${total_amount:.2f} via Credit/Debit Card initiated."
            )
        else:
            st.error("Please fill in all card details to proceed.")

    footer = """
        <div style="
            position: fixed; 
            bottom: 0; 
            left: 0; 
            width: 100%; 
            background-color: #282c34; 
            color: white; 
            text-align: center; 
            padding: 15px 0;  
            font-size: 14px;
            z-index: 1000;
            ">
            <p style="margin: 0;">© 2024 ScanX | All Rights Reserved</p>
            <p style="margin: 5px 0 0 0;">Contact: your.email@example.com | Follow us on 
                <a href="https://twitter.com/yourprofile" style="color: lightblue; text-decoration: none;">Twitter</a> | 
                <a href="https://instagram.com/yourprofile" style="color: lightblue; text-decoration: none;">Instagram</a>
            </p>
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
