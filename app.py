import streamlit as st
import requests
import io
from PIL import Image

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="منصة لؤي تيك للتصميم الإعلاني", page_icon="🚀", layout="centered")

# التصميم والمظهر (CSS) لجعله يبدو احترافياً
st.markdown("""
    <style>
    .main-title { font-family: 'Cairo', sans-serif; text-align: center; color: #1E3A8A; font-size: 36px; font-weight: bold; }
    .sub-title { font-family: 'Cairo', sans-serif; text-align: center; color: #4B5563; font-size: 18px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_index=True)

st.markdown('<p class="main-title">🚀 منصة لؤي تيك للتصميم الإعلاني المحترف</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">إصدار V4.0 - صمم بوسترات منتجاتك الحقيقية أو النصية بأعلى سرعة وجودة</p>', unsafe_allow_html=True)

# الـ API Key الخاص بك (Together AI)
TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"] if "TOGETHER_API_KEY" in st.secrets else "ضع_مفتاحك_هنا"

# تقسيم الصفحة إلى خيارات
tab1, tab2 = st.tabs(["📸 تصميم بصورة منتج حقيقي", "✍️ تصميم بوصف نصي فقط"])

# ----------------- القسم الأول: تصميم بصورة منتج حقيقي -----------------
with tab1:
    st.write("### 🖼️ ارفع صورة منتجك ودع الذكاء الاصطناعي يبدع خلفه!")
    uploaded_file = st.file_uploader("اختر صورة المنتج (ساعة، عطر، حقيبة...)", type=["png", "jpg", "jpeg"])
    
    product_style = st.selectbox("نمط الخلفية الإعلانية 🎨", [
        "سينمائي فخم (Cinematic Luxury)",
        "طبيعي هادئ (Natural & Organic)",
        "استوديو احترافي (Studio Light)",
        "عصري نيون (Cyberpunk Neon)"
    ], key="tab1_style")
    
    extra_details = st.text_input("إضافات تريد رؤيتها في الخلفية؟ (اختياري بالإنجليزية) 📝", placeholder="e.g., on a dark rock, water drops, smoke...")

    if st.button("أطلق العنان واصنع البوستر بالصورة الحقيقية 🔥", key="btn_img"):
        if uploaded_file is not None:
            with st.spinner("جاري معالجة صورتك الحقيقية ودمجها مع الخلفية السحرية... ⏳"):
                # هنا سيتم دمج الصورة لاحقاً بالـ API الجديد
                st.info("كود استقبال الصورة ممتاز! سنقوم بربط الـ API الخاص بالصور في الخطوة التالية بمجرد تأكيدك.")
        else:
            st.warning("الرجاء رفع صورة المنتج أولاً يا هندسة! ⚠️")

# ----------------- القسم الثاني: التصميم النصي القديم -----------------
with tab2:
    st.write("### ✍️ اكتب وصف المنتج والذكاء الاصطناعي سيتخيله كاملاً")
    text_prompt = st.text_input("اسم المنتج أو وصفه الفخم (بالإنجليزية) 🛍️", placeholder="e.g., Luxury Rolex watch on a golden stand")
    
    text_style = st.selectbox("نمط التصميم الإعلاني 🎨", [
        "سينمائي فخم (Cinematic)",
        "إعلان تجاري ثلاثي الأبعاد (3D Commercial)",
        "واقعي جداً (Photorealistic)",
        "بسيط وراقي (Minimalist)"
    ], key="tab2_style")
    
    aspect_ratio = st.selectbox("أبعاد البوستر الإعلاني 📐", ["مربع (Instagram Post) 1:1", "طولي (Story / Reels) 9:16"])

    if st.button("أطلق العنان واصنع التصميم النصي الآن 🔥", key="btn_text"):
        if text_prompt:
            with st.spinner("جاري تخيل وتوليد بوسترك الأسطوري... ⏳"):
                # الكود النصي القديم المستقر الخاص بـ Together AI
                headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
                payload = {
                    "model": "black-forest-labs/FLUX.1-schnell",
                    "prompt": f"{text_prompt}, {text_style} commercial advertisement product photography, high resolution, 8k",
                    "width": 1024, "height": 1024, "steps": 4, "response_format": "base64"
                }
                try:
                    res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                    if res.status_code == 200:
                        import base64
                        img_data = res.json()["data"][0]["b64_json"]
                        image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                        st.image(image, caption="✨ تم التصميم بنجاح بواسطة منصة لؤي تيك", use_container_width=True)
                    else:
                        st.error(f"حدث خطأ في السيرفر: {res.text}")
                except Exception as e:
                    st.error(f"فشل الاتصال: {str(e)}")
        else:
            st.warning("الرجاء كتابة وصف المنتج أولاً! ⚠️")
