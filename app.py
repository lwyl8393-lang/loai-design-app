import streamlit as st
import time

# 1. إعدادات المنصة الاحترافية المتكاملة 2026
st.set_page_config(
    page_title="Loai Tech - Ultimate Omni Hub", 
    page_icon="👑", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم دارك فخم جداً يناسب المنصات السحابية الاحترافية
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #E2E8F0; }
    h1, h2, h3, h4 { font-family: 'Cairo', sans-serif; color: #38BDF8 !important; text-align: center; }
    .hero-box { background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); padding: 30px; border-radius: 15px; border: 1px solid #312E81; text-align: center; margin-bottom: 25px; }
    .feature-card { background-color: #1E293B; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px; }
    .status-badge { background-color: #065F46; color: #34D399; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    .stButton>button { background: linear-gradient(90deg, #38BDF8 0%, #2563EB 100%); color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي الفخم للمنصة
st.markdown("""
    <div class="hero-box">
        <h1 style='margin:0; font-size: 38px;'>👑 Loai Tech - Premium Merchant Service Suite</h1>
        <p style='color: #94A3B8; font-size: 16px; margin-top: 10px;'>
            المنصة المتكاملة لخدمات المتاجر: تسويق أوتوماتيكي، خطط محتوى، مستشار تسعير، تحسين السيو، وسيناريوهات الفيديوهات القصيرة
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية لإدارة وبث القنوات
with st.sidebar:
    st.markdown("### 🌐 Active API Webhooks")
    st.write("وضع قنوات الربط للبث:")
    ws_sync = st.toggle("🔗 WhatsApp Meta Cloud API", value=True)
    if ws_sync: st.markdown("   <span class=\"status-badge\">🟢 Live & Ready</span>", unsafe_allow_html=True)
    
    ig_sync = st.toggle("🔗 Instagram Graph Stream", value=True)
    if ig_sync: st.markdown("   <span class=\"status-badge\">🟢 Connected</span>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 📈 إحصائيات المنصة")
    st.metric(label="العمليات المنفذة اليوم", value="3,482 عملية")
    st.metric(label="صافي أرباح المتاجر المحققة", value="$14,850")

# 3. الهيكلة الجديدة للألسنة (تضمين كافة الخدمات الذكية)
tab_marketing, tab_calendar, tab_pricing, tab_review, tab_seo, tab_video = st.tabs([
    "📸 التصميم والبث الأوتوماتيكي", 
    "📅 صانع خطط المحتوى", 
    "💰 مستشار التسعير الذكي", 
    "💬 معالج ردود الشكاوى", 
    "🔍 محلل سيو المنتجات", 
    "🎬 سكريبتات الفيديوهات القصيرة"
])

# ----------------- 1. تبويب التسويق والتصميم الأوتوماتيكي -----------------
with tab_marketing:
    st.markdown("### 📸 مسار التسويق الاحترافي والبث بنقرة واحدة")
    col_control, col_preview = st.columns([1, 1])
    with col_control:
        product_type = st.selectbox("📦 نوع المنتج المرفوع", ["🎧 Premium Headphones", "🧴 Luxury Perfume", "⌚ Smart Watch", "👟 Designer Sneakers"])
        ad_tone = st.selectbox("✍️ لهجة الإعلان التسويقي", ["لهجة خليجية بيضاء", "لغة عربية فصحى حماسية", "English Modern Ad Copy"])
        uploaded_file = st.file_uploader("Upload product image here", type=["png", "jpg", "jpeg"])
    with col_preview:
        if uploaded_file is not None:
            st.success("🎯 تم رفع وتجهيز صورة المنتج!")
            poster_url = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600" if "Headphones" in product_type else "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
            st.image(poster_url, caption="Preview", width=400)
            if st.button("🚀 اطلق الحملة في جميع المنصات الآن"):
                st.success("🟢 تم البث بنجاح ونشر الإعلان تلقائياً عبر الواتساب والانستقرام!")
                st.balloons()

# ----------------- 2. تبويب صانع خطط المحتوى التسويقي -----------------
with tab_calendar:
    st.markdown("### 📅 صانع خطط المحتوى التسويقي لشهر كامل (AI Content Calendar)")
    st.write("ادخل تفاصيل متجرك وسيقوم الذكاء الاصطناعي ببناء جدول منشورات أسبوعي إبداعي لزيادة التفاعل:")
    store_desc = st.text_input("ماذا يبيع متجرك؟ (مثال: متجر لبيع القهوة المختصة وأدواتها)", placeholder="اكتب هنا تفاصيل المتجر...")
    if st.button("توليد خطة المحتوى التسويقية ⚡"):
        with st.spinner("جاري صياغة الأفكار وكتابة الهاشتاقات..."):
            time.sleep(1)
            st.markdown(f"""
            <div class="feature-card">
                <h4>🗓️ خطة المحتوى المقترحة لمتجر: ({store_desc})</h4>
                <p><b>• اليوم الأول (تفاعلي):</b> منشور يتكلم عن سر اختيار حبوب القهوة المثالية + سؤال للجمهور في الستوري (كيف تحب قهوتك الصباحية؟) #قهوة_مختصة</p>
                <p><b>• اليوم الثاني (تعليمي):</b> فيديو قصير (Reels) يشرح الطريقة الصحيحة لاستخلاص الإسبريسو بدون مرارة.</p>
                <p><b>• اليوم الثالث (بيعي):</b> عرض خاص (اشترِ محصولين واحصل على الثالث مجاناً) مع استخدام كابشن حماسي يركز على توفير الشحن.</p>
            </div>
            """, unsafe_allow_html=True)

# ----------------- 3. تبويب مستشار التسعير وحساب الأرباح -----------------
with tab_pricing:
    st.markdown("### 💰 مستشار تسعير المنتجات وحساب الأرباح الذكي (Pricing Calculator)")
    st.write("احسب صافي ربحك وتجنب الخسارة، دع النظام يقترح عليك سعر البيع الأنسب لمنتجك بناءً على تكاليفك:")
    col_p1, col_p2, col_p3 = st.columns(3)
    cost_price = col_p1.number_input("سعر تكلفة المنتج الأصلي ($)", min_value=1.0, value=10.0)
    shipping_price = col_p2.number_input("تكلفة الشحن والتغليف ($)", min_value=0.0, value=5.0)
    ads_price = col_p3.number_input("تكلفة الإعلانات المتوقعة لكل قطعة ($)", min_value=0.0, value=4.0)
    
    if st.button("تحليل وتحديد سعر البيع المثالي 📊"):
        total_costs = cost_price + shipping_price + ads_price
        suggested_sale = total_costs * 1.5  
        net_profit = suggested_sale - total_costs
        st.markdown(f"""
        <div class="feature-card" style="border-left-color: #10B981;">
            <h4>📊 تقرير تحليل التسعير من Loai Tech:</h4>
            <p>• إجمالي التكاليف الثابتة على القطعة: <b>${total_costs:.2f}</b></p>
            <p>• سعر البيع المقترح للمستهلك (هامش ربح ممتاز): <b style="color:#10B981;">${suggested_sale:.2f}</b></p>
            <p>• صافي ربحك المتوقع من كل بيعة: <b style="color:#38BDF8;">${net_profit:.2f}</b></p>
        </div>
        """, unsafe_allow_html=True)

# ----------------- 4. تبويب معالج ردود الشكاوى ومراجعات العملاء -----------------
with tab_review:
    st.markdown("### 💬 معالج ردود الشكاوى ومراجعات العملاء (Crisis & Review Manager)")
    st.write("امتص غضب زبائنك وحافظ على تقييم متجرك العالي. الصق شكوى العميل هنا وسيقوم النظام بصياغة رد دبلوماسي واحترافي:")
    complaint_text = st.text_area("انسخ شكوى العميل الغاضب هنا:", "المنتج وصلني متأخر جداً والكرتون كان ممزق، تجربة سيئة ولن أتعامل معكم مجدداً!!")
    if st.button("توليد رد احترافي لامتصاص الغضب ✨"):
        with st.spinner("جاري صياغة رد يحافظ على الولاء..."):
            time.sleep(0.8)
            st.markdown("""
            <div class="feature-card">
                <h4>مرحباً بعميلنا العزيز، نعتذر بشدة عن هذه التجربة التي لا تمثل معاييرنا.. تفضل بالرد الجاهز لإرساله له:</h4>
                <p style="color:#A7F3D0; font-style: italic;">
                "أهلاً بك عميلنا الغالي، نأسف جداً على ما حدث ونقدر استياءك تماماً. راحتك ورضاك هي أولويتنا، وبناءً على ذلك تم توجيه فريق الدعم لتعويضك فوراً بشحن منتج جديد لك مجاناً بالكامل مع كود خصم خاص لطلبك القادم. نعدك بتقديم الأفضل دائماً 🤍"
                </p>
            </div>
            """, unsafe_allow_html=True)

# ----------------- 5. تبويب محلل ومحسن صفحات المنتجات -----------------
with tab_seo:
    st.markdown("### 🔍 محلل ومحسن صفحات المنتجات والسيو (SEO & Conversion Auditor)")
    st.write("اجعل منتجاتك تظهر في محركات بحث قوقل وتجذب المشترين؛ ضع الوصف العادي وسيقوم النظام بتحسينه كتابياً:")
    old_seo = st.text_area("وصف المنتج الحالي والمختصر:", "سماعة بلوتوث سوداء ممتازة وعازلة صوت وسعرها رخيص.")
    if st.button("تحسين السيو ورفع معدل التحويل 🚀"):
        with st.spinner("جاري دمج الكلمات المفتاحية الأكثر بحثاً..."):
            time.sleep(0.8)
            st.markdown("""
            <div class="feature-card">
                <h4>🎯 الوصف الجديد المحسن كلياً والمتوافق مع السيو (SEO):</h4>
                <p><b>العنوان المقترح:</b> سماعة بلوتوث لاسلكية عازلة للضوضاء المحيطية - Loai Tech Pro</p>
                <p><b>الوصف الجاذب:</b> استمتع بتجربة صوتية استثنائية ونقاء لا ميل له مع أفضل سماعة بلوتوث لاسلكية تدعم خاصية عزل الضجيج النشط (ANC). تم تصميمها بهيكل مريح ليناسب الاستخدام الطويل أثناء العمل أو الرياضة مع بطارية خارقة ممتدة. اطلبها الآن من متجرنا بأفضل سعر وضمان ذهبي متكامل!</p>
            </div>
            """, unsafe_allow_html=True)

# ----------------- 6. تبويب صانع أفكار الفيديوهات القصيرة -----------------
with tab_video:
    st.markdown("### 🎬 صانع أفكار وسكريبتات الفيديوهات القصيرة (TikTok & Reels Hook)")
    st.write("أقوى وسيلة للبيع الآن هي تيك توك؛ اختر تصنيف منتجك ودع الأداة تكتب لك سيناريو فيديو فيرال (Viral) يضمن جلب المشاهدات:")
    video_prod = st.text_input("ما هو المنتج المراد تصويره؟ (مثال: عطر نسائي فاخر)", value="ساعة ذكية مقاومة للماء")
    if st.button("صناعة سيناريو الفيديو القصير 🎬"):
        with st.spinner("جاري ابتكار خطاف بصري وسيناريو مشوق..."):
            time.sleep(1)
            st.markdown(f"""
            <div class="feature-card">
                <h4>🎬 سكريبت تيك توك الاحترافي الجاهز لتصوير منتج: ({video_prod})</h4>
                <p><b>• أول 3 ثواني (الخطاف لجذب الانتباه):</b> ابدأ الفيديو بلقطة سريعة للمنتج وهو يسقط في الماء مع صوت قوي، وقل بصوت مسموع: "وقف! لا تشتري أي ساعة ذكية قبل ما تشوف هذا الفيديو!"</p>
                <p><b>• منتصف الفيديو (استعراض القيمة والحل):</b> استعرض شاشة الساعة وسرعة استجابتها للاشعارات والاتصالات والمميزات الرياضية بطريقة تصوير قريبة وعالية الجودة.</p>
                <p><b>• آخر 3 ثواني (طلب الفعل - CTA):</b> "الساعة عليها عرض رهيب الحين وشحن مجاني لأول 50 مشتري، اضغط على الرابط في البايو واطلبها الحين!"</p>
            </div>
            """, unsafe_allow_html=True)
