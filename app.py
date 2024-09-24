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

# Styling for navbar
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "10px",
        "height": "40px",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.95rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
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
