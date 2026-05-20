import streamlit as st
import time

# 1. إعدادات المنصة الفخمة والواجهة الاحترافية الداكنة
st.set_page_config(
    page_title="Loai Tech - Auto Ad OmniPlatform", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق الطابع البصري الفاخر للمنصة
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #E2E8F0; }
    h1, h2, h3 { font-family: 'Cairo', sans-serif; color: #38BDF8 !important; text-align: center; }
    .hero-box { background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); padding: 30px; border-radius: 15px; border: 1px solid #312E81; text-align: center; margin-bottom: 25px; }
    .feature-card { background-color: #1E293B; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px; }
    .status-badge { background-color: #065F46; color: #34D399; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الترحيبي بمنصة لؤي تيك الأوتوماتيكية
st.markdown("""
    <div class="hero-box">
        <h1 style='margin:0; font-size: 38px;'>🤖 Loai Tech - Automated Product Marketing Platform</h1>
        <p style='color: #94A3B8; font-size: 16px; margin-top: 10px;'>
            The Ultimate "Just Upload" Solution: Instant AI Creative Ad & Automatic Multi-Channel Distribution Hub
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية لإدارة ربط القنوات وتفعيل الصلاحيات
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

# 3. الألسنة الرئيسية لعرض آلية العمل
menu_tab1, menu_tab2 = st.tabs([
    "📸 Just Upload: The Magic Path", 
    "Plug-and-Play Hub Overview"
])

with menu_tab1:
    st.markdown("## 📸 One-Click Multi-Channel Distribution Hub")
    st.write("Remove the guesswork. Just upload your product photo, select the type, and let Loai Tech do the magic.")
    st.markdown("---")
    
    # 📝 إتاحة خيار تحديد نوع المنتج لتغيير البوستر والنص بذكاء
    product_type = st.selectbox(
        "📦 Select Product Category (🎯 اختر تصنيف المنتج لملائمة الأبعاد والخلفية)",
        ["🎧 Premium Headphones (سماعات رأس فاخرة)", 
         "🧴 Luxury Perfume & Fragrance (عطور وبخور)", 
         "⌚ Smart Watches & Accessories (ساعات ذكية)", 
         "👟 Limited Edition Sneakers (أحذية ورياضة)"]
    )
    
    # مربع رفع الملفات
    uploaded_file = st.file_uploader("Upload Clean Product Photo", type=["png", "jpg", "jpeg"], key="main_upload")

    if uploaded_file is not None:
        st.success("🎯 Photo uploaded successfully! Activating AI Creative workflows...")
        
        col1, col2 = st.columns([1, 1])
        
        # تجهيز البيانات والمكتبة الذكية بناءً على اختيار المستخدم
        if "Headphones" in product_type:
            poster_url = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600"
            caption_text = "🎧 انغمس في عالم من الصوت النقي! سماعات لؤي تيك الاحترافية تعزل الضجيج وتمنحك بيئة صوتية سينمائية ساحرة مع بطارية تدوم طويلاً. اطلبها الآن وعش التجربة الفاخرة! 🚀"
        elif "Perfume" in product_type:
            poster_url = "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
            caption_text = "🧴 سحر يفوح بالفخامة! نأخذك في رحلة تأسر الحواس مع عطرنا الجديد المصمم عبر منصة Loai Tech ليواكب تطلعاتك الأنيقة. متاح للطلب الفوري بنسبة خصم حصرية! ✨"
        elif "Watches" in product_type:
            poster_url = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=600"
            caption_text = "⌚ وقتك ثمين، اجعله أكثر ذكاءً! الساعة الذكية المتكاملة لمتابعة نشاطك اليومي بأناقة عصرية تناسب جميع المناسبات. متوفرة الآن مع شحن مجاني وسريع! 🌍"
        else:
            poster_url = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=600"
            caption_text = "👟 انطلق بخطوات واثقة ومريحة! الحذاء الرياضي الحصري ذو التصميم الانسيابي المبتكر لتوفير أقصى درجات الراحة لقدميك أثناء الجري أو العمل. الكمية محدودة جداً! 🔥"

        with col1:
            st.markdown("### 🎨 AI Creative Design Output")
            with st.spinner("AI is rendering premium studio environment in real-time..."):
                time.sleep(1.2) # محاكاة معالجة سريعة مستقرة وآمنة
                st.image(poster_url, caption=f"✨ Premium Poster Generated for {product_type}")
                st.success("✅ Design Rendered Instantly.")
        
        with col2:
            st.markdown("### 📢 Auto-Publishing & Campaign Sync")
            st.info(f"📝 AI Creative Caption Ready:\n\n {caption_text}")
            st.write("---")
            
            # زر النشر الفوري المستقر
            if st.button("Start Automatic Distribution Now 🚀"):
                st.write("🌍 Broadcasting Status:")
                if ws_sync:
                    with st.spinner("Piping image and caption into WhatsApp Business API..."):
                        time.sleep(1)
                        st.success("🟢 Broadcasted successfully to WhatsApp Subscribers.")
                
                if ig_sync:
                    with st.spinner("Connecting Instagram Graph API and uploading to stories..."):
                        time.sleep(1)
                        st.success("🟢 Published successfully to Instagram Feed/Story Stream.")
                st.balloons()

with menu_tab2:
    st.markdown("## Plug-and-Play Hub Overview")
    st.write("This diagram displays how Loai Tech system pipelines information from client channels into the central AI processor:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #2563EB;'>
                <h3>🟢 WhatsApp Gateway</h3>
                <p><b>Permission:</b> Active</p>
                <p style='color:#94A3B8; font-size:12px;'>Automatically publishes image and highly persuasive creative ad caption.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #E11D48;'>
                <h3>🟢 Instagram DM Stream</h3>
                <p><b>Permission:</b> Active</p>
                <p style='color:#94A3B8; font-size:12px;'>Pipes image link to user engagement points (mention and DM flow).</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class=\"feature-card\" style='border-left-color: #4B5563;'>
                <h3>🔴 Facebook Page Flow</h3>
                <p><b>Permission:</b> Disconnected</p>
                <p style='color:#94A3B8; font-size:12px;'>Integrates page comments and messenger automations under the same agent.</p>
            </div>
        """, unsafe_allow_html=True)
