import streamlit as st

st.title("Payment Screen")

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
