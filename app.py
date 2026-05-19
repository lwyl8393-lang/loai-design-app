import streamlit as st
import requests
import io
import base64
import json
from PIL import Image

# 1. إعدادات الصفحة الفخمة باللون الداكن والستايل الاحترافي
st.set_page_config(
    page_title="Loai Tech Multi-Channel AI OmniPlatform", 
    page_icon="👑", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# مفتاح التشغيل الخاص بك
TOGETHER_API_KEY = "839352e8250bd6850c90c74b9f2913f044efcb4c16f059e1bfd0fa910d610826"

# تطبيق واجهة وتصميم دارك فخم جداً وبلمسات برمجية راقية
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #E2E8F0; }
    h1, h2, h3 { font-family: 'Cairo', sans-serif; color: #38BDF8 !important; text-align: center; }
    .hero-box { background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); padding: 30px; border-radius: 15px; border: 1px solid #312E81; text-align: center; margin-bottom: 25px; }
    .feature-card { background-color: #1E293B; padding: 20px; border-radius: 12px; border-left: 5px solid #38BDF8; margin-bottom: 15px; }
    .status-badge { background-color: #065F46; color: #34D399; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    .btn-custom { background: linear-gradient(90deg, #38BDF8 0%, #2563EB 100%); color: white; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي للمنصة الفخمة
st.markdown("""
    <div class="hero-box">
        <h1 style='margin:0; font-size: 38px;'>👑 Loai Tech Advanced AI OmniPlatform</h1>
        <p style='color: #94A3B8; font-size: 16px; margin-top: 10px;'>
            Next-Gen Marketing Suite: Ultimate Product Design, Intelligent Auto-Bot, & Multi-Channel Social Sync
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية الفخمة لإدارة حسابات العميل وصلاحيات الربط
with st.sidebar:
    st.markdown("### 🌐 Channel Integration Control")
    st.write("Grant permissions and manage client sync status:")
    
    # محاكاة ربط القنوات مع حالات التشغيل
    ws_sync = st.toggle("🔗 Connect WhatsApp Business API", value=True)
    if ws_sync: st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    
    ig_sync = st.toggle("🔗 Sync Instagram Graph API", value=True)
    if ig_sync: st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    
    fb_sync = st.toggle("🔗 Link Facebook Meta Suite", value=False)
    if fb_sync: 
        st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    else:
        st.markdown("   <span style='background-color:#7F1D1D; color:#FCA5A5; padding:5px 12px; border-radius:20px; font-size:12px;'>🔴 Disconnected</span>", unsafe_allow_html=True)
        
    st.write("---")
    st.markdown("### 📊 AI Performance Metrics")
    st.metric(label="Auto-Replies Processed", value="1,482 messages")
    st.metric(label="AI Designs Generated", value="342 Posters")

# 3. تقسيم الواجهة الرئيسية إلى 3 أقسام كبرى ومبتكرة
menu_tab1, menu_tab2, menu_tab3 = st.tabs([
    "🎨 AI Poster Studio", 
    "🤖 Intelligent CRM Auto-Bot", 
    "🔌 Multi-Channel Hub Overview"
])

# ----------------- القسم الأول: أستوديو التصميم الذكي -----------------
with menu_tab1:
    st.markdown("## 🎨 Premium Ad Poster Generation")
    
    sub_tab1, sub_tab2 = st.tabs(["📸 Product Image Mode (Depth)", "✍️ Pure Text Conceptual Mode"])
    
    with sub_tab1:
        uploaded_file = st.file_uploader("Upload Clean Product Photo", type=["png", "jpg", "jpeg"], key="main_upload")
        style_preset = st.selectbox("Select Advertisement Background Theme 🔮", [
            "Cinematic Luxury style, premium studio lighting, golden accents",
            "Natural and Organic style with soft shadows, wet dark stone podium",
            "Professional dark minimalist product display showcase, soft neon glow",
            "Cyberpunk futuristic presentation layout, abstract geometric lines"
        ])
        details = st.text_input("Refine Background Elements (English Only)", placeholder="e.g., floating luxury silk ribbon, studio atmosphere, reflections")
        
        if st.button("Craft Luxury Ad Now 🔥", key="btn1"):
            if uploaded_file and details:
                with st.spinner("Analyzing product outline and drawing professional background..."):
                    try:
                        base64_image = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
                        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"}
                        payload = {
                            "model": "black-forest-labs/FLUX.1-Depth",
                            "prompt": f"Professional commercial product photography, {style_preset}, {details}, ultra-premium composition, 8k resolution, global illumination",
                            "image": f"data:image/jpeg;base64,{base64_image}",
                            "steps": 20, "response_format": "base64"
                        }
                        res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                        if res.status_code == 200:
                            img_data = res.json()["data"][0]["b64_json"]
                            st.image(Image.open(io.BytesIO(base64.b64decode(img_data))), caption="✨ Masterpiece Crafted Successfully by Loai Tech")
                        else: st.error(res.text)
                    except Exception as e: st.error(str(e))
            else: st.warning("Please upload a file and specify background instructions! ⚠️")

    with sub_tab2:
        concept = st.text_input("Conceptual Idea", placeholder="e.g., Limited edition perfume bottle floating above a crystal ocean split")
        if st.button("Generate from Text Concept 🚀"):
            if concept:
                with st.spinner("Painting your imagination..."):
                    try:
                        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"}
                        payload = {
                            "model": "black-forest-labs/FLUX.1-schnell",
                            "prompt": f"{concept}, high-end commercial ad photography, studio layout, breathtaking, hyperrealistic",
                            "width": 1024, "height": 1024, "steps": 4, "response_format": "base64"
                        }
                        res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                        if res.status_code == 200:
                            img_data = res.json()["data"][0]["b64_json"]
                            st.image(Image.open(io.BytesIO(base64.b64decode(img_data))), caption="✨ Prompt Concept Built Successfully")
                        else: st.error(res.text)
                    except Exception as e: st.error(str(e))

# ----------------- القسم الثاني: بوت الرد التلقائي الذكي -----------------
with menu_tab2:
    st.markdown("## 🤖 Intelligent CRM Auto-Bot Simulation")
    st.write("Test how the AI bot acts and auto-responds to customer queries on synced networks:")
    
    st.markdown("""
        <div class="feature-card">
            <h4>🤖 System Prompt (Instructions for the Bot)</h4>
            <p style='font-size:13px; color:#A0AEC0;'>The bot is configured to act as an elite, polite, and persuasive sales representative for the client's store. It answers instantly and closes deals gracefully.</p>
        </div>
    """, unsafe_allow_html=True)
    
    customer_msg = st.text_area("Simulate Incoming Customer Message (Can be Arabic or English) 💬", "مرحباً، أعجبني التصميم الإعلاني وأريد معرفة الأسعار وطريقة التوصيل والطلب؟")
    
    if st.button("Trigger AI Agent Auto-Response ⚡"):
        if customer_msg:
            with st.spinner("AI Agent is drafting an optimal response..."):
                try:
                    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"}
                    payload = {
                        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                        "messages": [
                            {"role": "system", "content": "You are an elite, super polite and expert customer service AI agent for a luxurious product store. Reply in the same language as the customer beautifully, use professional emojis, encourage sales, and offer assistance."},
                            {"role": "user", "content": customer_msg}
                        ]
                    }
                    res = requests.post("https://api.together.xyz/v1/chat/completions", json=payload, headers=headers)
                    if res.status_code == 200:
                        reply = res.json()["choices"][0]["message"]["content"]
                        st.markdown("### 💬 Automated Response Output:")
                        st.info(reply)
                    else: st.error(res.text)
                except Exception as e: st.error(str(e))

# ----------------- القسم الثالث: لوحة التحكم الشاملة لربط مواقع العميل -----------------
with menu_tab3:
    st.markdown("## 🔌 Multi-Channel Hub Architecture Overview")
    st.write("This diagram displays how Loai Tech system pipelines information from client channels into the central AI processor:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #2563EB;'>
                <h3>🟢 WhatsApp Gateway</h3>
                <p><b>Webhook Status:</b> Active</p>
                <p><b>Latency:</b> 120ms</p>
                <p style='color:#94A3B8; font-size:12px;'>Intercepts incoming WhatsApp texts, triggers AI Auto-Bot, and pipes answers instantly.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #E11D48;'>
                <h3>🟢 Instagram DM Stream</h3>
                <p><b>Webhook Status:</b> Active</p>
                <p><b>Listening on:</b> Mentions & DMs</p>
                <p style='color:#94A3B8; font-size:12px;'>Monitors user engagement on Instagram stories and posts to trigger design links.</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #4B5563;'>
                <h3>⚫ Facebook Suite</h3>
                <p><b>Webhook Status:</b> Idle</p>
                <p><b>Action Required:</b> Re-authenticate</p>
                <p style='color:#94A3B8; font-size:12px;'>Integrates page comments and messenger automations under the same agent.</p>
            </div>
        """, unsafe_allow_html=True)
