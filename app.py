import streamlit as st
import time

# 1. إعدادات المنصة الاحترافية 2026
st.set_page_config(
    page_title="Loai Tech - Ultimate Merchant Hub", 
    page_icon="👑", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. هندسة التصميم الفاخر (UI/UX Custom Injection)
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    
    <style>
    /* تغيير الخط الشامل للموقع */
    * { font-family: 'Cairo', sans-serif !important; }
    
    /* خلفية المنصة الفاخرة */
    .main { background-color: #0B0F19; color: #F1F5F9; }
    
    /* الهيدر الرئيسي وتأثير الإضاءة الخلفية */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 35px;
    }
    
    .hero-title {
        font-size: 42px !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #34D399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    /* كروت الخدمات التفاعلية */
    .service-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .service-card:hover {
        border-color: rgba(56, 189, 248, 0.5);
        box-shadow: 0 4px 25px rgba(56, 189, 248, 0.15);
        transform: translateY(-2px);
    }
    
    /* تخصيص التبويبات العلوية لجعلها كأنها أزرار تطبيق حقيقي */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #111827;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #1F2937;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: #9CA3AF !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        font-weight: 600 !important;
        border: none !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #2563EB 0%, #38BDF8 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    /* تصميم جانبي مميز للمؤشرات */
    .sidebar-card {
        background: #111827;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #1F2937;
        margin-bottom: 15px;
    }
    
    /* الأزرار التفاعلية الفخمة */
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #38BDF8 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.2);
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4) !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر الرئيسي المبتكر
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">LOAI TECH • PREMIUM METRIC HUB</div>
        <p style='color: #94A3B8; font-size: 16px; margin: 0; font-weight: 500;'>
            منظومة الذكاء الاصطناعي الشاملة لتوليد المبيعات، خطط التسويق، وإدارة قنوات البث الفوري للمتاجر الرقمية
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية المحدثة
with st.sidebar:
    st.markdown("<h3 style='color:#38BDF8; text-align:center;'>⚙️ بوابات الاتصال السحابي</h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    ws_sync = st.toggle("🔗 WhatsApp Business Cloud API", value=True)
    if ws_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل وجاهز للبث الأوتوماتيكي</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    ig_sync = st.toggle("🔗 Instagram Graph Stream", value=True)
    if ig_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل ومتزامن مع المتاجر</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h4 style='color:#818CF8;'>📈 أداء المنصة المالي اليوم</h4>", unsafe_allow_html=True)
    st.metric(label="إجمالي العمليات المنفذة ناجحة", value="3,482 عمليّة")
    st.metric(label="صافي عوائد المتاجر (مبيعات محققة)", value="$14,850")

# 5. التبويبات العلوية المنظمة والمصممة على شكل أزرار تطبيق ممتدة
tab_marketing, tab_calendar, tab_pricing, tab_review, tab_seo, tab_video = st.tabs([
    "📸 التصميم والبث الآلي", 
    "📅 صناعة خطة المحتوى", 
    "💰 مستشار التسعير المحترف", 
    "💬 معالج ردود الشكاوى", 
    "🔍 مهندس سيو المنتجات", 
    "🎬 سكريبتات الفيديوهات"
])

# ----------------- 1. تبويب التسويق والتصميم الأوتوماتيكي -----------------
with tab_marketing:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>📸 مسار التصميم والبث الذكي بنقرة واحدة</h3>", unsafe_allow_html=True)
    col_control, col_preview = st.columns([1, 1])
    with col_control:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        product_type = st.selectbox("📦 حدد تصنيف منتجك:", ["🎧 Premium Headphones", "🧴 Luxury Perfume", "⌚ Smart Watch", "👟 Designer Sneakers"])
        ad_tone = st.selectbox("✍️ لهجة النص الإعلاني التلقائي:", ["لهجة خليجية بيضاء مبيعية", "لغة عربية فصحى حماسية", "English Conversion Ad Copy"])
        uploaded_file = st.file_uploader("Upload product image here", type=["png", "jpg", "jpeg"])
        st.markdown('</div>', unsafe_allow_html=True)
    with col_preview:
        if uploaded_file is not None:
            st.success("🎯 تم رفع الصورة بنجاح وجاري البث!")
            poster_url = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600" if "Headphones" in product_type else "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
            st.image(poster_url, caption="معاينة البوستر الإعلاني المولد", width=420)
            if st.button("🚀 اطلق الحملة وبثها الآن"):
                st.success("🟢 تم نشر وتوزيع الإعلان عبر قنوات الواتساب والستوري بنجاح!")
                st.balloons()

# ----------------- 2. تبويب صانع خطط المحتوى التسويقي -----------------
with tab_calendar:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>📅 صانع خطط المحتوى التسويقي الرقمي لشهر كامل</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    store_desc = st.text_input("أدخل تخصص متجرك الإلكتروني بالتفصيل:", placeholder="مثال: متجر سعودي لبيع حبوب البن المختصة وأدوات التقطير")
    if st.button("توليد الخطة وجدولتها أوتوماتيكياً ⚡"):
        with st.spinner("جاري صياغة الاستراتيجية المبيعية..."):
            time.sleep(1)
            st.markdown(f"""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#34D399; text-align:right;">📅 الجدولة الزمنية المقترحة لمتجر: ({store_desc})</h4>
                <p style="text-align:right;"><b>• اليوم الأول (تفاعلي):</b> منشور يتكلم عن سر اختيار حبوب القهوة المثالية + سؤال للجمهور في الستوري (كيف تحب قهوتك الصباحية؟) #قهوة_مختصة</p>
                <p style="text-align:right;"><b>• اليوم الثاني (تعليمي):</b> فيديو قصير (Reels) يشرح الطريقة الصحيحة لاستخلاص الإسبريسو بدون مرارة.</p>
                <p style="text-align:right;"><b>• اليوم الثالث (بيعي):</b> عرض خاص (اشترِ محصولين واحصل على الثالث مجاناً) مع استخدام كابشن حماسي يركز على توفير الشحن.</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 3. تبويب مستشار التسعير وحساب الأرباح -----------------
with tab_pricing:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>💰 مستشار تسعير المنتجات لضمان الهوامش الربحية</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    col_p1, col_p2, col_p3 = st.columns(3)
    cost_price = col_p1.number_input("تكلفة شراء القطعة من المورد ($)", min_value=1.0, value=10.0)
    shipping_price = col_p2.number_input("تكلفة الشحن والتغليف والخدمات ($)", min_value=0.0, value=5.0)
    ads_price = col_p3.number_input("تكلفة الاستحواذ الإعلاني للقطعة ($)", min_value=0.0, value=4.0)
    
    if st.button("تحليل وحساب السعر المقترح للبيع 📊"):
        total_costs = cost_price + shipping_price + ads_price
        suggested_sale = total_costs * 1.5  
        net_profit = suggested_sale - total_costs
        st.markdown(f"""
        <div style="background:#0F172A; padding:20px; border-radius:12px; border-right: 5px solid #34D399; margin-top:20px;">
            <h4 style="text-align:right; color:#34D399; margin:0;">📊 الحسبة المالية النهائية من مستشار Loai Tech:</h4>
            <p style="text-align:right; margin:10px 0 5px 0;">• إجمالي تكاليف التشغيل الثابتة: <b>${total_costs:.2f}</b></p>
            <p style="text-align:right; margin:5px 0;">• سعر البيع المقترح للمستهلك النهائي: <b style="color:#34D399;">${suggested_sale:.2f}</b></p>
            <p style="text-align:right; margin:5px 0;">• صافي ربحك الصافي من كل عملية بيع: <b style="color:#38BDF8;">${net_profit:.2f}</b></p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 4. تبويب معالج ردود الشكاوى ومراجعات العملاء -----------------
with tab_review:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>💬 معالج الردود الدبلوماسية وامتصاص غضب العملاء</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    complaint_text = st.text_area("انسخ ولصق رسالة العميل المستاء هنا:", "المنتج وصلني متأخر جداً والكرتون كان ممزق، تجربة سيئة ولن أتعامل معكم مجدداً!!")
    if st.button("توليد الرد الاحترافي الفوري الذكي ✨"):
        with st.spinner("جاري صياغة رد يحافظ على الولاء..."):
            time.sleep(0.8)
            st.markdown("""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#F3F4F6; text-align:right;">الرد المقترح لإرساله للعميل ممتصاً للغضب:</h4>
                <p style="color:#A7F3D0; font-style: italic; text-align:right; font-size:15px; direction:rtl;">
                "أهلاً بك عميلنا الغالي، نأسف جداً على ما حدث ونقدر استياءك تماماً. راحتك ورضاك هي أولويتنا، وبناءً على ذلك تم توجيه فريق الدعم لتعويضك فوراً بشحن منتج جديد لك مجاناً بالكامل مع كود خصم خاص لطلبك القادم. نعدك بتقديم الأفضل دائماً 🤍"
                </p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 5. تبويب محلل ومحسن صفحات المنتجات -----------------
with tab_seo:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>🔍 تحسين سيو المنتجات (SEO) لجلب زوار قوقل مجاناً</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    old_seo = st.text_area("ضع هنا وصف منتجك الحالي والمختصر جداً:", "سماعة بلوتوث سوداء ممتازة وعازلة صوت وسعرها رخيص.")
    if st.button("إعادة صياغة ومضاعفة جودة السيو 🚀"):
        with st.spinner("جاري تحليل الكلمات المفتاحية..."):
            time.sleep(0.8)
            st.markdown("""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px; direction:rtl;">
                <h4 style="color:#38BDF8; text-align:right;">🎯 نسخة الوصف الجديدة المتوافقة مع خوارزميات محركات البحث ومعدلات التحويل:</h4>
                <p style="text-align:right;"><b>العنوان المحسن:</b> سماعة بلوتوث لاسلكية عازلة للضوضاء المحيطية - Loai Tech Pro</p>
                <p style="text-align:right;"><b>الوصف التسويقي:</b> استمتع بتجربة صوتية استثنائية ونقاء لا مثيل له مع أفضل سماعة بلوتوث لاسلكية تدعم خاصية عزل الضجيج النشط (ANC). تم تصميمها بهيكل مريح ليناسب الاستخدام الطويل أثناء العمل أو الرياضة مع بطارية خارقة ممتدة. اطلبها الآن من متجرنا بأفضل سعر وضمان ذهبي متكامل!</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 6. تبويب صانع أفكار الفيديوهات القصيرة -----------------
with tab_video:
    st.markdown("<h3 style='text-align:right; color:#38BDF8;'>🎬 صانع سيناريوهات الفيديوهات الفيرال (TikTok & Reels Script)</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    video_prod = st.text_input("ما هو المنتج المستهدف بالتصوير للحملة؟", value="ساعة ذكية مقاومة للماء")
    if st.button("ابتكار السيناريو والخطاف البصري 🎬"):
        with st.spinner("جاري تحضير السكريبت المشوق..."):
            time.sleep(1)
            st.markdown(f"""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px; direction:rtl;">
                <h4 style="color:#818CF8; text-align:right;">🎬 سكريبت فيديو تيك توك المقترح لـ: ({video_prod})</h4>
                <p style="text-align:right;"><b>• أول 3 ثواني (الخطاف لجذب الانتباه):</b> ابدأ الفيديو بلقطة سريعة للمنتج وهو يسقط في الماء مع صوت قوي، وقل بصوت مسموع: "وقف! لا تشتري أي ساعة ذكية قبل ما تشوف هذا الفيديو!"</p>
                <p style="text-align:right;"><b>• منتصف الفيديو (استعراض القيمة والحل):</b> استعرض شاشة الساعة وسرعة استجابتها للاشعارات والاتصالات والمميزات الرياضية بطريقة تصوير قريبة وعالية الجودة.</p>
                <p style="text-align:right;"><b>• آخر 3 ثواني (طلب الفعل - CTA):</b> "الساعة عليها عرض رهيب الحين وشحن مجاني لأول 50 مشتري، اضغط على الرابط في البايو واطلبها الحين!"</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
