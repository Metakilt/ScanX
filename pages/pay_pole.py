import streamlit as st
import base64


def pay_pole():

    mobile_view = """
        <style>
            .mobile-container {{
                max-width: 375px;
                margin: auto;
                padding: 20px;
                background-color: #f3f6f4;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                bottom: 400px;
            }}
            .qr-code {{
                width: 80%;
                margin: 20px auto;
            }}
            .instructions {{
                margin-top: 10px;
                font-size: 16px;
                color: #232B2B;
            }}

            h2 {{
                font-size: 40px;
                text-align: center;
                color: #232B2B;
            }}
        </style>

        <div class="mobile-container">
            <h2>Scan to Pay</h2>
            <img class="qr-code" src="data:image/png;base64,{}" alt="QR Code">
            <br></br>
            <p class="instructions">Use your phone to scan the QR code and complete the payment.</p>
        </div>
    """

    with open("qr_code.png", "rb") as file:
        image_data = file.read()

    encoded_image = base64.b64encode(image_data).decode()

    st.markdown(mobile_view.format(encoded_image), unsafe_allow_html=True)