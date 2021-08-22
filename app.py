# Core Packages
import streamlit as st
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
#For QR code
import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,border=14)

from PIL import Image
#Function to load them images
def load_image(img):
    im = Image.open(img)
    return im

# Application
def main():
    menu = ["Home"]


    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        # Text input
        with st.form(key='myqr_form'):
            raw_text = st.text_area("Put your text here")
            submit_button = st.form_submit_button("Generate")
        # Layout
        if submit_button:

            col1,col2= st.beta_columns(2)
            with col1:
                # Add Data
                qr.add_data(raw_text)
                #Generate
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')

                #File name
                img_filename = 'generate_img_{}.png'.format(timestr)
                path_for_images = os.path.join('image_folder', img_filename)
                img.save(path_for_images)

                final_img = load_image(path_for_images)
                st.image(final_img)

            with col2:
                st.info("Original Text")
                st.write(raw_text)

if __name__ == '__main__':
            main()
