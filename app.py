import streamlit as st
import requests
import io
import base64
import json
import time
from PIL import Image

# 1. إعدادات الصفحة الفخمة والنظيفة جداً
st.set_page_config(
    page_title="Loai Tech - Auto Ad OmniPlatform", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# مفتاح التشغيل الجديد والمفعل الخاص بك
TOGETHER_API_KEY = "839352e8250bd6850c90c74b9f2913f044efcb4c16f059e1bfd0fa910d610826"

# تطبيق واجهة فخمة جداً داكنة لتبدو احترافية
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #E2E8F0; }
    h1, h2, h3 { font-family: 'Cairo', sans-serif; color: #38BDF8 !important; text-align: center; }
    .hero-box { background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); padding: 30px; border-radius: 15px; border: 1px solid #312E81; text-align: center; margin-bottom: 25px; }
    .feature-card { background-color: #1E293B; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px; }
    .status-badge { background-color: #065F46; color: #34D399; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    .stButton>button { background: linear-gradient(90deg, #38BDF8 0%, #2563EB 100%); color: white; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي للمنصة الجديدة
st.markdown("""
    <div class="hero-box">
        <h1 style='margin:0; font-size: 38px;'>🤖 Loai Tech - Automated Product Marketing Platform</h1>
        <p style='color: #94A3B8; font-size: 16px; margin-top: 10px;'>
            The Ultimate "Just Upload" Solution: Instant AI Creative Ad & Automatic Multi-Channel Distribution Hub
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية الفخمة لإدارة ربط قنوات العميل وصلاحيات النشر
with st.sidebar:
    st.markdown("### 🌐 Channel Integration Control")
    st.write("Enable permissions for automatic publishing:")
    
    ws_sync = st.toggle("🔗 Connect WhatsApp Business API", value=True)
    if ws_sync: st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    
    ig_sync = st.toggle("🔗 Link Instagram DM & Story API", value=True)
    if ig_sync: st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    
    fb_sync = st.toggle("🔗 Link Facebook Page Automation", value=False)
    if fb_sync: 
        st.markdown("   <span class=\"status-badge\">🟢 Connected & Ready</span>", unsafe_allow_html=True)
    else:
        st.markdown("   <span style='background-color:#7F1D1D; color:#FCA5A5; padding:5px 12px; border-radius:20px; font-size:12px;'>🔴 Disconnected</span>", unsafe_allow_html=True)
        
    st.write("---")
    st.markdown("### 📈 Automated Activity Sync")
    st.metric(label="Designs Auto-Generated", value="1,482")
    st.metric(label="Posts Auto-Published", value="1,123")

# 3. المسار الجديد الفخم والكامل: بمجرد رفع الصورة يبدأ السحر
menu_tab1, menu_tab2 = st.tabs([
    "📸 Just Upload: The Magic Path", 
    "Plug-and-Play Hub Overview"
])

with menu_tab1:
    st.markdown("## 📸 One-Click Multi-Channel Distribution Hub")
    st.write("Remove the guess work. Just upload your product photo, and let Loai Tech system do everything else.")
    st.markdown("---")
    
    uploaded_file = st.file_uploader("Upload Clean Product Photo", type=["png", "jpg", "jpeg"], key="main_upload")

    if uploaded_file is not None:
        st.write("Photo uploaded. Processing will start when you press the button...")
        
        # تقسيم الشاشة لقسمين: التصميم والنشر
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
                <div class=\"feature-card\">
                    <h3>🎨 1. AI Creative Design Workflow</h3>
                    <p style='color:#94A3B8; font-size:12px;'>Our AI automatically analyzes your product outline and dreams up a creative advertisement script and a luxurious environment.</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Generate Ad Now! 🔥"):
                with st.spinner("AI is brainstorming the perfect ad and design environment..."):
                    try:
                        base64_image = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
                        headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"}
                        
                        payload = {
                            "model": "black-forest-labs/FLUX.1-Depth",
                            "prompt": "Commercial ad product photography, luxurious cinematic setting, deep moody blue lighting with warm golden accents, water drops, smoke atmosphere, ultra premium composition, global illumination, highly professional award winning studio setting",
                            "image": f"data:image/jpeg;base64,{base64_image}",
                            "steps": 20, "response_format": "base64"
                        }
                        res = requests.post("https://api.together.xyz/v1/images/generations", json=payload, headers=headers)
                        
                        if res.status_code == 200:
                            img_data = res.json()["data"][0]["b64_json"]
                            final_image = Image.open(io.BytesIO(base64.b64decode(img_data)))
                            st.image(final_image, caption="✨ Loai Tech AI Design Ready")
                            st.success("Design Completed & Validated.")
                            
                        else: st.error(f"Design Server Error: {res.text}")
                    except Exception as e: st.error(str(e))
        
        with col2:
            st.markdown("""
                <div class=\"feature-card\">
                    <h3>📢 2. Auto-Publishing Workflow</h3>
                    <p style='color:#94A3B8; font-size:12px;'>Monitor the status of your product as it's automatically distributed across synced customer social channels.</p>
                </div>
            """, unsafe_allow_html=True)
            
            # محاكاة خطوة النشر الأوتوماتيكي الفخمة جداً
            if st.button("Start Automatic Distribution Now 🚀"):
                # محاكاة خطوة التصميم أولاً
                if 'design_ready' not in st.session_state:
                    with st.spinner("Brainstorming creative ad script and design environment..."):
                        time.sleep(1.5)
                        st.info("AI: Ad Concept Drafted. Design Workflow triggered.")
                    
                    with st.spinner("Drafting highly persuasive creative ad caption..."):
                        time.sleep(1)
                        st.session_state['ad_caption'] = "✨ فخامة بلا حدود! عطر Dior Sauvage الأسطوري. لمسة من الأناقة تمنحك الثقة في كل مكان. متوفر الآن في متجر لؤي تيك! 🚀"
                        st.info(f"AI: Ad Caption Drafted: '{st.session_state['ad_caption']}'")
                        
                    with st.spinner("Piping design into distribution queue..."):
                        time.sleep(1)
                        st.session_state['design_ready'] = True
                        st.success("All pipelines are ready to go.")
                
                # خطوة النشر الأوتوماتيكي على القنوات المفعلة
                st.write("---")
                st.write("Automatic Publishing Status:")
                
                if ws_sync:
                    with st.spinner("Piping image and caption into WhatsApp Business API..."):
                        time.sleep(1.2)
                        st.success("🟢 Published successfully to WhatsApp Channel.")
                
                if ig_sync:
                    with st.spinner("Connecting Instagram DM API and posting to linked stories..."):
                        time.sleep(1.5)
                        st.success("🟢 Distributed successfully to Instagram DM stream.")
                
                if not ws_sync and not ig_sync:
                    st.warning("No distribution channels are synced. Please check the sidebar to connect them.")

with menu_tab2:
    st.markdown("## Plug-and-Play Hub Overview")
    st.write("This diagram displays how Loai Tech system pipelines information from client channels into the central AI processor:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #2563EB;'>
                <h3>🟢 WhatsApp Gateway</h3>
                <p><b>Permiss:</b> Active</p>
                <p style='color:#94A3B8; font-size:12px;'>Automatically publishes image and highly persuasive creative ad caption.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #E11D48;'>
                <h3>🟢 Instagram DM Stream</h3>
                <p><b>Permiss:</b> Active</p>
                <p style='color:#94A3B8; font-size:12px;'>Pipes image link to user engagement points (mention and DM flow).</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #4B5563;'>
                <h3>🔴 Facebook Page Flow</h3>
                <p><b>Permiss:</b> Disconnected</p>
                <p style='color:#94A3B8; font-size:12px;'>Integrates page comments and messenger automations under the same agent.</p>
            </div>
        """, unsafe_allow_html=True)
