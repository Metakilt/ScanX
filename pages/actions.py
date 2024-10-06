import streamlit as st
import pandas as pd
from buttons import Shopping # Importing from buttons.py
import streamlit.components.v1 as components


def actions():

    data = 'Grocery_Dataset.csv'
    df = pd.read_csv(data)

    # Initialize the Shopping basket from buttons
    basket = Shopping(df)

    # button styling
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

    # buttons
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
    
    basket.format()