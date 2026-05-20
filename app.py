import streamlit as st
import time

# 1. إعدادات المنصة الاحترافية 2026
st.set_page_config(
    page_title="منصة رِكاز الذكية - الشريك المتكامل لمتجرك", 
    page_icon="💎", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. هندسة التصميم الفاخر والهوية البصرية العربية
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    
    <style>
    /* تغيير الخط الشامل للموقع ليناسب القراءة العربية */
    * { font-family: 'Cairo', sans-serif !important; direction: rtl; text-align: right; }
    
    /* خلفية المنصة الداكنة الفاخرة */
    .main { background-color: #0B0F19; color: #F1F5F9; }
    
    /* الهيدر الرئيسي العربي المبتكر */
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
        text-align: center !important;
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
    
    /* تخصيص التبويبات العلوية الاحترافية */
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
    
    /* تصميم البطاقات الجانبية */
    .sidebar-card {
        background: #111827;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #1F2937;
        margin-bottom: 15px;
    }
    
    /* الأزرار الفخمة التفاعلية */
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #38BDF8 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.2);
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4) !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر الرئيسي المحدث بالهوية العربية
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">💎 مـنـصـة رِكَـاز الـذَّكِـيَّـة</div>
        <p style='color: #94A3B8; font-size: 16px; margin: 10px 0 0 0; font-weight: 500; text-align: center !important;'>
            المنظومة السحابية المتكاملة لخدمات المتاجر: صناعة الهوية الإعلانية، هندسة المبيعات، وأتمتة النشر والتسويق الرقمي
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية باللغة العربية بالكامل
with st.sidebar:
    st.markdown("<h3 style='color:#38BDF8; text-align:center;'>⚙️ بوابات الربط السحابي</h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    ws_sync = st.toggle("🔗 بوابة واتساب للأعمال (Meta API)", value=True)
    if ws_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل وجاهز للبث التلقائي</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    ig_sync = st.toggle("🔗 نظام بث منشورات انستقرام", value=True)
    if ig_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل ومتزامن مع المتجر</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h4 style='color:#818CF8; text-align:center;'>📈 أداء المنصة المالي اليوم</h4>", unsafe_allow_html=True)
    st.metric(label="إجمالي العمليات الناجحة", value="3,482 عمليّة")
    st.metric(label="عوائد المتاجر المحققة عبر المنصة", value="$14,850")

# 5. التبويبات العلوية المنظمة والمصممة بالكامل بالعربية
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
    st.markdown("<h3 style='color:#38BDF8;'>📸 مسار التصميم التلقائي والبث المباشر</h3>", unsafe_allow_html=True)
    col_control, col_preview = st.columns([1, 1])
    with col_control:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        product_type = st.selectbox("📦 حدد تصنيف منتج المتجر:", ["🎧 سماعات رأس فاخرة", "🧴 عطورات ومستحضرات تجميل", "⌚ ساعات ذكية حديثة", "👟 أحذية رياضية مصممة"])
        ad_tone = st.selectbox("✍️ لهجة النص الإعلاني التلقائي:", ["لهجة خليجية بيضاء مبيعية", "لغة عربية فصحى حماسية", "أسلوب تسويقي حديث وعصري"])
        uploaded_file = st.file_uploader("قم برفع صورة المنتج النظيفة هنا", type=["png", "jpg", "jpeg"])
        st.markdown('</div>', unsafe_allow_html=True)
    with col_preview:
        if uploaded_file is not None:
            st.success("🎯 تم رفع الصورة بنجاح وجاري البث!")
            poster_url = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600" if "سماعات" in product_type else "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
            st.image(poster_url, caption="معاينة البوستر الإعلاني المولد ذكياً", width=420)
            if st.button("🚀 اطلق الحملة وبثها الآن في ثوانٍ"):
                st.success("🟢 تم نشر وتوزيع الإعلان عبر قنوات الواتساب والستوري بنجاح!")
                st.balloons()

# ----------------- 2. تبويب صانع خطط المحتوى التسويقي -----------------
with tab_calendar:
    st.markdown("<h3 style='color:#38BDF8;'>📅 صانع خطط المحتوى التسويقي وجدول المنشورات</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    store_desc = st.text_input("أدخل تخصص ومجال متجرك الإلكتروني بالتفصيل:", placeholder="مثال: متجر سعودي لبيع عينات العطور الفاخرة المستوحاة")
    if st.button("بناء الخطة التسويقية وجدولتها ⚡"):
        with st.spinner("جاري دراسة السوق وصياغة الأفكار..."):
            time.sleep(1)
            st.markdown(f"""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#34D399;">📅 الجدولة الزمنية المقترحة لمتجر: ({store_desc})</h4>
                <p><b>• اليوم الأول (تفاعلي):</b> منشور يتكلم عن سر ثبات العطور الشتوية + سؤال تفاعلي في الستوري (أيش عطرك المفضل بالدوام؟) #عطور_فاخرة</p>
                <p><b>• اليوم الثاني (تعليمي):</b> فيديو قصير (Reels) يشرح أماكن النبض الصحيحة بالجسم لضمان فوحان العطر لأكثر من 24 ساعة.</p>
                <p><b>• اليوم الثالث (بيعي مباشر):</b> كود خصم حصري ومؤقت (FREE) بمناسبة نهاية الأسبوع مع رابط شراء مباشر لرفع معدل التحويل.</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 3. تبويب مستشار التسعير وحساب الأرباح -----------------
with tab_pricing:
    st.markdown("<h3 style='color:#38BDF8;'>💰 حساب وهندسة هوامش الربح والتسعير الذكي</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    col_p1, col_p2, col_p3 = st.columns(3)
    cost_price = col_p1.number_input("تكلفة شراء المنتج الأصلي من المورد ($)", min_value=1.0, value=10.0)
    shipping_price = col_p2.number_input("تكلفة الشحن والتغليف والتشغيل ($)", min_value=0.0, value=5.0)
    ads_price = col_p3.number_input("تكلفة الاستحواذ والتسويق المتوقعة لكل بيعة ($)", min_value=0.0, value=4.0)
    
    if st.button("تحليل وحساب السعر المبيعي المقترح للمستهلك 📊"):
        total_costs = cost_price + shipping_price + ads_price
        suggested_sale = total_costs * 1.5  
        net_profit = suggested_sale - total_costs
        st.markdown(f"""
        <div style="background:#0F172A; padding:20px; border-radius:12px; border-right: 5px solid #34D399; margin-top:20px;">
            <h4 style="color:#34D399; margin:0;">📊 التقرير المالي الصادر من مستشار رِكـاز:</h4>
            <p style="margin:10px 0 5px 0;">• إجمالي تكاليف المنتج والتشغيل: <b>${total_costs:.2f}</b></p>
            <p style="margin:5px 0;">• سعر البيع العادل والمقترح لضمان هامش ربح ممتاز: <b style="color:#34D399;">${suggested_sale:.2f}</b></p>
            <p style="margin:5px 0;">• صافي ربحك الصافي المتوقع من كل عملية بيع: <b style="color:#38BDF8;">${net_profit:.2f}</b></p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 4. تبويب معالج ردود الشكاوى ومراجعات العملاء -----------------
with tab_review:
    st.markdown("<h3 style='color:#38BDF8;'>💬 معالج الردود الذكية والدبلوماسية للشكاوى</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    complaint_text = st.text_area("قم بلصق رسالة أو مراجعة العميل المستاء هنا:", "المنتج وصلني متأخر جداً والكرتون كان ممزق، تجربة سيئة ولن أتعامل معكم مجدداً!!")
    if st.button("توليد رد احترافي لامتصاص غضب العميل ✨"):
        with st.spinner("جاري صياغة رد يحافظ على الولاء والبراند..."):
            time.sleep(0.8)
            st.markdown("""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#F3F4F6;">الرد الجاهز المولد للاستخدام فوراً:</h4>
                <p style="color:#A7F3D0; font-style: italic; font-size:15px;">
                "أهلاً بك عميلنا العزيز، نعتذر بشدة عن هذه التجربة التي لا تمثل معايير جودتنا. راحتك ورضاك هي أولويتنا القصوى، وبناءً على ذلك تم توجيه قسم الشحن لتعويضك فوراً بإرسال طلب جديد لك مجاناً بالكامل دون أي تكاليف إضافية مع كود خصم خاص لطلبك القادم. نعدك بالأفضل دائماً 🤍"
                </p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 5. تبويب محلل ومحسن صفحات المنتجات -----------------
with tab_seo:
    st.markdown("<h3 style='color:#38BDF8;'>🔍 تحسين وتدقيق سيو المنتجات (SEO) لجلب زوار محركات البحث</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    old_seo = st.text_area("ضع هنا وصف منتجك الحالي العادي أو المختصر:", "سماعة بلوتوث سوداء ممتازة وعازلة صوت وسعرها رخيص.")
    if st.button("توليد الكلمات المفتاحية وتحسين الوصف 🚀"):
        with st.spinner("جاري تهيئة الوصف برمجياً..."):
            time.sleep(0.8)
            st.markdown("""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#38BDF8;">🎯 نسخة الوصف والبيانات المهيأة بالكامل لمحركات بحث قوقل:</h4>
                <p><b>العنوان المقترح والجاذب:</b> سماعة بلوتوث لاسلكية عازلة للضوضاء المحيطية المحترفة - رِكاز برو</p>
                <p><b>الوصف الجاذب للمشترين:</b> استمتع بتجربة صوتية استثنائية ونقاء لا مثيل له مع أفضل سماعة بلوتوث لاسلكية متطورة تدعم خاصية عزل الضجيج النشط (ANC). تم تصميمها بهيكل مريح ليناسب الاستخدام الطويل والمكثف أثناء العمل أو التمارين الرياضية مع بطارية خارقة ممتدة الأجل. اطلبها الآن من متجرنا بأفضل سعر وضمان ذهبي متكامل لراحة بالك!</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 6. تبويب صانع أفكار الفيديوهات القصيرة -----------------
with tab_video:
    st.markdown("<h3 style='color:#38BDF8;'>🎬 سكريبتات وسيناريوهات الفيديوهات القصيرة (تيك توك / ريلز)</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    video_prod = st.text_input("أدخل اسم المنتج المستهدف لتصوير الحملة الإعلانية البصرية:", value="ساعة ذكية مقاومة للماء")
    if st.button("صناعة خطاف بصري وسيناريو كامل للمشهد 🎬"):
        with st.spinner("جاري صياغة السكريبت المشوق..."):
            time.sleep(1)
            st.markdown(f"""
            <div style="background:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; margin-top:15px;">
                <h4 style="color:#818CF8;">🎬 سيناريو فيديو تيك توك التسويقي المقترح لمنتج: ({video_prod})</h4>
                <p><b>• أول 3 ثواني (الخطاف لجذب الانتباه):</b> ابدأ الفيديو بلقطة صدمة للمنتج وهو يسقط في الماء مع مؤثر صوتي قوي، وقل بنبرة حماسية: "انتظر! لا تشتري أي ساعة ذكية قبل ما تشوف مميزات هذه الأسطورة!"</p>
                <p><b>• منتصف الفيديو (استعراض القيمة والحل):</b> قم باستعراض شاشة الساعة وسرعة استجابتها الرهيبة للمكالمات والرسائل والمميزات الرياضية والطبية عبر زوايا تصوير قريبة وعالية الفخامة.</p>
                <p><b>• آخر 3 ثواني (طلب الفعل المباشر - CTA):</b> "الساعة عليها عرض مجنون الحين وشحن مجاني لأول 50 طلب بس، اضغط على الرابط أسفل الحساب واطلبها قبل انتهاء الكمية!"</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
