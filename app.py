import streamlit as st
import requests
import io
import base64
import json
from PIL import Image

# Luxury Page Config
st.set_page_config(page_title="Loai Tech Ad Platform", page_icon="🚀", layout="centered")

# Custom Professional CSS Styles
st.markdown("""
    <style>
    .main-title { font-family: 'Cairo', sans-serif; text-align: center; color: #1E3A8A; font-size: 36px; font-weight: bold; }
    .sub-title { font-family: 'Cairo', sans-serif; text-align: center; color: #4B5563; font-size: 18px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🚀 Loai Tech AI Design Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Version 5.3 - Generate High-End Product Advertisements Instantly</p>', unsafe_allow_html=True)

# Fetch API Key from Secrets Safely
TOGETHER_API_KEY = "key_CbAnhR1GeN9tPjjpzGBZe0826"


# Clean English Navigation Tabs to Prevent Latin-1 Encoding Errors
tab1, tab2 = st.tabs(["📸 Design via Product Image", "✍️ Design via Text Description"])

# ----------------- SECTION 1: IMAGE TO IMAGE DESIGN -----------------
with tab1:
    st.write("### 🖼️ Upload Product Image & Generate Background")
    uploaded_file = st.file_uploader("Choose a clean product image (PNG/JPG)", type=["png", "jpg", "jpeg"])
    
    product_style = st.selectbox("Select Advertisement Background Theme 🎨", [
        "Cinematic Luxury style, premium studio lighting",
        "Natural and Organic style with soft shadows, leaves and water drops",
        "Professional dark minimalist product display showcase podium",
        "Cyberpunk Neon modern tech background with abstract lasers"
    ], key="tab1_style")
    
    extra_details = st.text_input("Enter Background Details (In English Only) 📝", placeholder="e.g., on a dark rock, floating water splashing, smoke atmosphere...")

    if st.button("Generate Image Poster Now 🔥", key="btn_img"):
        if uploaded_file is not None and extra_details:
            with st.spinner("Processing your product image and crafting the layout... ⏳"):
                try:
                    # Reading raw image bytes to avoid any file name encoding issues
                    img_bytes = uploaded_file.getvalue()
                    base64_image = base64.b64encode(img_bytes).decode('utf-8')
                    
                    headers = {
                        "Authorization": f"Bearer {TOGETHER_API_KEY}",
                        "Content-Type": "application/json; charset=utf-8"
                    }
                    
                    payload = {
                        "model": "black-forest-labs/FLUX.1-Depth",
                        "prompt": f"A high-end commercial advertisement product photography, {product_style}, {extra_details}, highly professional, 8k resolution, award winning studio composition",
                        "image": f"data:image/jpeg;base64,{base64_image}",
                        "steps": 20,
                        "response_format": "base64"
                    }
                    
                    # Hardcoded UTF-8 Enforcement for API Request Payload
                    data_json = json.dumps(payload, ensure_ascii=False).encode('utf-8')
                    res = requests.post("https://api.together.xyz/v1/images/generations", data=data_json, headers=headers)
                    
                    if res.status_code == 200:
                        img_data = res.json()["data"][0]["b64_json"]
                        final_image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                        st.image(final_image, caption="✨ Poster Designed Successfully by Loai Tech", use_container_width=True)
                    else:
                        st.error(f"Server Processing Error: {res.text}")
                except Exception as e:
                    st.error(f"Connection Failed: {str(e)}")
        elif uploaded_file is None:
            st.warning("Please upload a product image first! ⚠️")
        elif not extra_details:
            st.warning("Please type extra details in English to guide the AI! ⚠️")

# ----------------- SECTION 2: TEXT TO IMAGE DESIGN -----------------
with tab2:
    st.write("### ✍️ Type Product Description to Generate from Scratch")
    text_prompt = st.text_input("Product Name & Description (In English Only) 🛍️", placeholder="e.g., Luxury Rolex watch on a golden stand")
    
    text_style = st.selectbox("Design Creative Style 🎨", [
        "Cinematic Luxury Commercial Photography",
        "3D Commercial Render Studio Profile",
        "Photorealistic Hyper-detailed Shot",
        "Minimalist Elegant Design Layout"
    ], key="tab2_style")
    
    if st.button("Generate Text Poster Now 🔥", key="btn_text"):
        if text_prompt:
            with st.spinner("Visualizing your imagination... ⏳"):
                try:
                    headers = {
                        "Authorization": f"Bearer {TOGETHER_API_KEY}",
                        "Content-Type": "application/json; charset=utf-8"
                    }
                    payload = {
                        "model": "black-forest-labs/FLUX.1-schnell",
                        "prompt": f"{text_prompt}, {text_style}, high resolution, commercial product advertisement photography, 8k",
                        "width": 1024, "height": 1024, "steps": 4, "response_format": "base64"
                    }
                    
                    data_json = json.dumps(payload, ensure_ascii=False).encode('utf-8')
                    res = requests.post("https://api.together.xyz/v1/images/generations", data=data_json, headers=headers)
                    
                    if res.status_code == 200:
                        img_data = res.json()["data"][0]["b64_json"]
                        image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                        st.image(image, caption="✨ Poster Designed Successfully by Loai Tech", use_container_width=True)
                    else:
                        st.error(f"Server Error: {res.text}")
                except Exception as e:
                    st.error(f"Connection Error: {str(e)}")
        else:
            st.warning("Please enter a product description first! ⚠️")
