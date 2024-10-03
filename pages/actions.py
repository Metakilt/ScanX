import streamlit as st
import pandas as pd
from buttons import Shopping, access_bucket  # Importing from buttons.py


def actions():
    #st.title("Customer Actions Page")

    # Access data from the S3 bucket
    #data = access_bucket(bucket_name="itpm-products", bucket_obj="Grocery_Dataset.csv")
    data = 'Grocery_Dataset.csv' # local test
    df = pd.read_csv(data)

    # Initialize the Shopping basket from buttons
    basket = Shopping(df)

    # Buttons from buttons.py (no need for st.rewrite since buttons already has this)
    # buttons follow the columns layout of streamlit so needs to be 5 including pay feature.
    # html/css styling in customer action page does not really matter since it's only used in the background
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1.5,1.5,1.5,1.5,1.25])

        with col1:
            if st.button("Scan Muffin"):
                st.session_state["action"] = "Scanned choc muffin."
                basket.scan_muffin()
            if st.button("Remove Muffin"):
                st.session_state["action"] = "Removed choc muffin."
                basket.remove_muffin()

        with col2:
            if st.button("Scan Water"):
                st.session_state["action"] = (
                    "Scanned bottled water."
                )
                basket.scan_water()
            if st.button("Remove Water"):
                st.session_state["action"] = "Removed bottled water."
                basket.remove_water()

        with col3:
            if st.button("Scan Protein"):
                st.session_state["action"] = "Scanned protein powder."
                basket.scan_protein_powder()
            if st.button("Remove Protein"):
                st.session_state["action"] = "Removed protein powder."
                basket.remove_protein_powder()

        with col4:
            if st.button("Scan Coffee"):
                st.session_state["action"] = "Scanned coffee."
                basket.scan_coffee()
            if st.button("Remove Coffee"):
                st.session_state["action"] = "Removed coffee."
                basket.remove_coffee()

        with col5:
            if st.button("Clear Cart"):
                st.session_state["action"] = "Cleared cart..."
                basket.clear()

    st.write(f"Shopping Total: ${basket.total()}") # comment this line if final format is checkout page
    # show table // (convert to checkout page (basket.format_2()) if sync library does not work)
    basket.format()