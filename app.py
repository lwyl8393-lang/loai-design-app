import streamlit as st
import requests
import io
import base64
import json
from PIL import Image

st.title("Loai Tech AI Platform")
st.write("Welcome to the ultimate design studio")

# المفتاح الصحيح الخاص بك
TOGETHER_API_KEY = "839352e8250bd6850c90c74b9f2913f044efcb4c16f059e1bfd0fa910d610826"

tab1, tab2 = st.tabs(["Image Design", "Text Design"])

with tab1:
    st.write("Upload product image:")
    uploaded_file = st.file_uploader("Choose Image", type=["png", "jpg", "jpeg"])
    extra_details = st.text_input("Enter Details (In English)", placeholder="e.g., premium light, dark background")

    if st.button("Generate Ad Poster"):
        if uploaded_file is not None and extra_details:
            with st.spinner("Processing..."):
                try:
                    img_bytes = uploaded_file.getvalue()
                    base64_image = base64.b64encode(img_bytes).decode('utf-8')
                    
                    headers = {
                        "Authorization": f"Bearer {TOGETHER_API_KEY}",
                        "Content-Type": "application/json"
                    }
                    
                    payload = {
                        "model": "black-forest-labs/FLUX.1-Depth",
                        "prompt": f"A luxury commercial advertisement photography, {extra_details}, 8k resolution, studio lighting",
                        "image": f"data:image/jpeg;base64,{base64_image}",
                        "steps": 20,
                        "response_format": "base64"
                    }
                    
                    res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                    
                    if res.status_code == 200:
                        img_data = res.json()["data"][0]["b64_json"]
                        final_image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                        st.image(final_image, caption="Success by Loai Tech")
                    else:
                        st.error(f"Server Error: {res.text}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

with tab2:
    st.write("Type prompt to generate:")
    text_prompt = st.text_input("Product prompt (In English)", placeholder="e.g., Luxury watch on a golden stand")
    
    if st.button("Generate Text Poster"):
        if text_prompt:
            with st.spinner("Visualizing..."):
                try:
                    headers = {
                        "Authorization": f"Bearer {TOGETHER_API_KEY}",
                        "Content-Type": "application/json"
                    }
                    payload = {
                        "model": "black-forest-labs/FLUX.1-schnell",
                        "prompt": f"{text_prompt}, commercial product advertisement photography, 8k",
                        "width": 1024, "height": 1024, "steps": 4, "response_format": "base64"
                    }
                    
                    res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                    
                    if res.status_code == 200:
                        img_data = res.json()["data"][0]["b64_json"]
                        image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                        st.image(image, caption="Success by Loai Tech")
                    else:
                        st.error(f"Server Error: {res.text}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
