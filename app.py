# Install the required dependencies:
# pip install streamlit-navigation-bar
# Or set up a virtual environment, activate it, and install dependencies using:
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt

import os
import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar
import pages as pg
import boto3

# Set the page configuration for Streamlit
st.set_page_config(initial_sidebar_state="collapsed")

# Define the navigation pages
pages = ["Home", "Grocery Items", "Shopping Cart", "Contact", "About"]

# Include parent_Dir to make the logo appear on the navbar
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(
    parent_dir, "shopping-cart-outline-svgrepo-com.svg"
)  # Ensure this file exists

# Styling for navbar from creator, change if needed
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "#ffff",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(120, 120, 120, 0.35)",
    },
}

page = st_navbar(pages, logo_path=logo_path, styles=styles)

if page == "Home":
    pg.home()
elif page == "Grocery Items":
    pg.grocery_items()
elif page == "Shopping Cart":
    pg.shopping_cart()
elif page == "Contact":
    pg.contact()
elif page == "About":
    pg.about()
# Placed in app.py to consistently have footer
footer = """
    <div style="
        position: fixed; 
        bottom: 0; 
        left: 0; 
        width: 100%; 
        background-color: #282c34; 
        color: white; 
        text-align: center; 
        padding: 15px 0;  /* Increased padding for better spacing */
        font-size: 14px;
        z-index: 1000;  /* Ensure the footer is on top of other elements */
        ">
        <p style="margin: 0;">© 2024 ScanX | All Rights Reserved</p>
        <p style="margin: 5px 0 0 0;">Contact: your.email@example.com | Follow us on 
            <a href="https://twitter.com/yourprofile" style="color: lightblue; text-decoration: none;">Twitter</a> | 
            <a href="https://instagram.com/yourprofile" style="color: lightblue; text-decoration: none;">Instagram</a>
        </p>
    </div>
"""
# Render the footer in Streamlit
st.markdown(footer, unsafe_allow_html=True)
