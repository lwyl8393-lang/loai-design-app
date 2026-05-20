import streamlit as st
import time

# 1. إعدادات المنصة الاحترافية المتكاملة 2026
st.set_page_config(
    page_title="منصة رِكاز الذكية - النظام الجبار للمتاجر", 
    page_icon="💎", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. هندسة التصميم الفاخر والهوية البصرية المتقدمة
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    
    <style>
    /* تغيير الخط الشامل للموقع ليناسب القراءة العربية الفخمة */
    * { font-family: 'Cairo', sans-serif !important; direction: rtl; text-align: right; }
    
    /* خلفية المنصة الداكنة */
    .main { background-color: #0B0F19; color: #F1F5F9; }
    
    /* الهيدر الرئيسي العربي المبتكر */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 35px;
    }
    
    .hero-title {
        font-size: 46px !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #34D399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center !important;
        margin-bottom: 5px;
    }
    
    /* كروت الخدمات التفاعلية المطورة */
    .service-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 26px;
        border-radius: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .service-card:hover {
        border-color: rgba(56, 189, 248, 0.6);
        box-shadow: 0 4px 25px rgba(56, 189, 248, 0.2);
        transform: translateY(-2px);
    }
    
    /* نتائج المعالجة الذكية */
    .result-box {
        background: #111827; 
        padding: 20px; 
        border-radius: 12px; 
        border-right: 5px solid #38BDF8; 
        margin-top: 15px;
    }
    
    /* تخصيص التبويبات العلوية الاحترافية لجعلها كأنها نظام تشغيل متكامل */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #111827;
        padding: 10px;
        border-radius: 14px;
        border: 1px solid #1F2937;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: #9CA3AF !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        border: none !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #2563EB 0%, #38BDF8 100%) !important;
        color: white !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }
    
    /* أزرار مخصصة وعريضة */
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #34D399 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.2);
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 25px rgba(52, 211, 153, 0.4) !important;
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر الرئيسي المحدث بالهوية الفاخرة
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">💎 مـنـصـة رِكَـاز الـذَّكِـيَّـة</div>
        <p style='color: #94A3B8; font-size: 17px; margin: 10px 0 0 0; font-weight: 500; text-align: center !important;'>
            الإصدار الإحترافي الجبار: أتمتة تشغيل المتاجر الرقمية، تعظيم الهوامش الربحية، وصناعة المحتوى الإعلاني الفيرال
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية لإدارة الربط والأداء المالي الحقيقي
with st.sidebar:
    st.markdown("<h3 style='color:#38BDF8; text-align:center;'>⚙️ بوابات الربط ومحاكاة البث</h3>", unsafe_allow_html=True)
    
    st.markdown('<div style="background:#111827; padding:12px; border-radius:10px; border:1px solid #1F2937; margin-bottom:10px;">', unsafe_allow_html=True)
    ws_sync = st.toggle("🔗 ربط الـ WhatsApp API", value=True)
    if ws_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل (Cloud Server Live)</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="background:#111827; padding:12px; border-radius:10px; border:1px solid #1F2937; margin-bottom:10px;">', unsafe_allow_html=True)
    ig_sync = st.toggle("🔗 بث منشورات Instagram", value=True)
    if ig_sync: st.markdown("<p style='color:#34D399; margin:0; font-size:13px;'>🟢 متصل ومتزامن مع المتاجر</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h4 style='color:#818CF8; text-align:center;'>📊 أداء المنصة الإجمالي اليوم</h4>", unsafe_allow_html=True)
    st.metric(label="الحملات الآلية المنشورة بنجاح", value="1,248 حملة")
    st.metric(label="المبيعات المحققة لعملائنا عبر المنصة", value="$48,920")

# 5. التبويبات الستة المطورة كلياً لتصبح تفاعلية بالكامل
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
    st.markdown("<h3 style='color:#38BDF8;'>📸 نظام التصميم المؤتمت ومحاكي البث المباشر للمنصات</h3>", unsafe_allow_html=True)
    col_control, col_preview = st.columns([1, 1])
    
    with col_control:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        prod_title = st.text_input("اسم المنتج المُراد تسويقه:", "سماعة رِكاز اللاسلكية العازلة")
        product_type = st.selectbox("📦 تصنيف وفئة المنتج الداخلي:", ["سماعات وأجهزة صوتية", "عطور ومستحضرات تجميل فاخرة", "ساعات ذكية وإلكترونيات", "أزياء وأحذية رياضية"])
        ad_tone = st.selectbox("✍️ النبرة التسويقية للنص الإعلاني:", ["لهجة خليجية بيضاء (مبيعات مباشرة)", "لغة عربية فصحى (قصصية ملهمة)", "أسلوب عصري سريع (تيك توك تريند)"])
        uploaded_file = st.file_uploader("ارفع لقطة واضحة للمنتج لمعالجتها فورا", type=["png", "jpg", "jpeg"])
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_preview:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.markdown("#### 📺 كرت المعاينة الفورية للإعلان قبل البث:")
        
        # كابشن ديناميكي يتغير حسب اسم المنتج واللهجة المكتوبة
        if "خليجية" in ad_tone:
            generated_caption = f"🔥 لعشاق الفخامة والتميز! وصلنا حديثاً {prod_title} بجودة رهيبة ومميزات ما ترحم. الكمية جداً محدودة، اطلب الحين قبل نفاد المخزون والدفع عند الاستلام! 🛒"
        elif "فصحى" in ad_tone:
            generated_caption = f"✨ ارتقِ بأسلوب حياتك اليومي مع {prod_title}. هندسة متقنة وتصميم ساحر يلبي طموحاتك. متوفر الآن بخصم خاص لفترة محدودة، اضغط على الرابط واكتشف الفرق الأصيل."
        else:
            generated_caption = f"⚡ التريند الجديد وصل! {prod_title} اللي الكل يتكلم عنه متوفر الحين بمتجرنا. توصيل سريع وضمان ذهبي. لا يفوتك العرض الفخم وضغطتين على الشاشة واطلبه! 🚀"
            
        st.info(generated_caption)
        
        poster_url = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600" if "سماعات" in product_type or "صوتية" in product_type else "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80"
        st.image(poster_url, caption="محاكاة معالجة خلفية الصورة بالذكاء الاصطناعي", use_container_width=True)
        
        if st.button("🚀 بث ونشر الحملة أوتوماتيكياً في كل القنوات"):
            with st.spinner("جاري صياغة البوستر وإرسال الـ Webhooks..."):
                time.sleep(1.2)
                st.success("🟢 تم البث! أُرسل الإعلان لـ 3,500 عميل على الواتساب وتم جدولة الستوري بنجاح!")
                st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 2. تبويب صانع خطط المحتوى التسويقي -----------------
with tab_calendar:
    st.markdown("<h3 style='color:#38BDF8;'>📅 مولد خطط المحتوى التسويقي وجدول المنشورات التفاعلي</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    
    store_name = st.text_input("اسم متجرك الإلكتروني:", "متجر بن الأصالة")
    store_desc = st.text_input("ما هو مجال البيع الدقيق للمتجر؟", "بيع حبوب البن المختصة وأدوات تقطير القهوة V60")
    
    if st.button("بناء وإعداد جدول المحتوى الأسبوعي الشامل ⚡"):
        with st.spinner("جاري تحليل اهتمامات الفئة المستهدفة وكتابة السيناريوهات..."):
            time.sleep(1.2)
            st.success("🎯 تم بناء الخطة التسويقية الاستراتيجية بنجاح! إليك جدول المنشورات:")
            
            # عرض جدول حقيقي ومنظم لإبهار العميل بدل النصوص العشوائية
            st.markdown(f"""
            <table style="width:100%; border-collapse: collapse; margin-top:15px; color:#F1F5F9;">
                <tr style="background-color: #1E293B; border-bottom: 2px solid #38BDF8;">
                    <th style="padding: 12px; text-align: right;">اليوم</th>
                    <th style="padding: 12px; text-align: right;">نوع المنشور</th>
                    <th style="padding: 12px; text-align: right;">فكرة المحتوى الإبداعي</th>
                    <th style="padding: 12px; text-align: right;">الهاشتاقات المستهدفة</th>
                </tr>
                <tr style="border-bottom: 1px solid #1F2937;">
                    <td style="padding: 12px; color:#34D399; font-weight:bold;">الأحد</td>
                    <td style="padding: 12px;">تفاعلي / ستوري</td>
                    <td>سؤال الجمهور: "كيف تبدأ صباحك المثالي، إسبريسو حاد ولا مقطرة باردة؟" مع تفعيل خيار التصويت.</td>
                    <td style="padding: 12px; color:#38BDF8;">#{store_name} #قهوة_الصباح</td>
                </tr>
                <tr style="border-bottom: 1px solid #1F2937;">
                    <td style="padding: 12px; color:#34D399; font-weight:bold;">الثلاثاء</td>
                    <td style="padding: 12px;">تعليمي / ريلز فيديو</td>
                    <td>فيديو سريع يشرح تأثير درجة طحن البن على طعم ونقاء كوب القهوة النهائي لمنع المرارة المستفزة.</td>
                    <td style="padding: 12px; color:#38BDF8;">#باريستا #قهوة_مختصة</td>
                </tr>
                <tr style="border-bottom: 1px solid #1F2937;">
                    <td style="padding: 12px; color:#34D399; font-weight:bold;">الخميس</td>
                    <td style="padding: 12px;">بيعي / عرض مباشر</td>
                    <td>صورة فخمة لأدوات التقطير المتوفرة بالمتجر مع كود خصم خاص بنهاية الأسبوع وشحن مجاني للطلبات فوق 199 ريال.</td>
                    <td style="padding: 12px; color:#38BDF8;">#عروض_المتاجر #عشاق_القهوة</td>
                </tr>
            </table>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 3. تبويب مستشار التسعير وحساب الأرباح -----------------
with tab_pricing:
    st.markdown("<h3 style='color:#38BDF8;'>💰 المستشار المالي والهندسة الحقيقية لهوامش وأرباح التاجر</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.write("أدخل تكاليفك الحقيقية بدقة وسيقوم المحرك المالي بحساب السعر الأنسب لضمان عدم الخسارة:")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    cost_price = col_p1.number_input("سعر تكلفة القطعة من المورد الأصلي ($)", min_value=0.5, value=12.0, step=0.5)
    shipping_price = col_p2.number_input("تكلفة الشحن الفردي والتغليف للعميل ($)", min_value=0.0, value=4.5, step=0.5)
    ads_price = col_p3.number_input("ميزانية الإعلانات المخصصة لبيع كل قطعة ($)", min_value=0.0, value=5.0, step=0.5)
    
    # حسابات رياضية حقيقية تتفاعل مع أرقام المستخدم فورياً
    total_costs = cost_price + shipping_price + ads_price
    suggested_sale = total_costs * 1.6  # احتساب هامش ربح مستهدف 60%
    gross_profit = suggested_sale - total_costs
    roi_percent = (gross_profit / total_costs) * 100 if total_costs > 0 else 0
    
    if st.button("تحليل البيانات وإصدار الميزانية التسعيرية المقترحة 📊"):
        with st.spinner("جاري فحص مؤشرات الأسواق وتحليل الهوامش..."):
            time.sleep(0.5)
            st.markdown(f"""
            <div class="result-box" style="border-right-color: #34D399;">
                <h4 style="color:#34D399; margin:0 0 10px 0;">📊 التقرير المالي النهائي المعتمد لمنتجك:</h4>
                <p>• إجمالي المصاريف والتشغيل للقطعة الواحدة: <b style="color:#F3F4F6;">${total_costs:.2f}</b></p>
                <p>• سعر البيع الاستراتيجي الموصى به للمستهلك: <b style="color:#34D399; font-size:18px;">${suggested_sale:.2f}</b></p>
                <p>• صافي الربح المالي المحقق من كل بيعة: <b style="color:#38BDF8;">${gross_profit:.2f}</b></p>
                <p>• العائد المتوقع على الاستثمار الإعلاني والتشغيلي ($ROI$): <b style="color:#A7F3D0;">{roi_percent:.1st}% +</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            # تقديم نصيحة ذكية حية ومبهرة بناء على النتيجة المالية
            if roi_percent >= 50:
                st.success("💡 نصيحة رِكاز: هذا المنتج يتمتع بهامش ربح ممتاز وجبار؛ ننصحك ببدء حملة إعلانية واسعة فوراً والتوسع في كميات المخزون.")
            else:
                st.warning("⚠️ نصيحة رِكاز: هامش الربح الحالي ضيق بعض الشيء؛ حاول التفاوض مع المورد لخفض سعر القطعة أو ارفع سعر البيع قليلاً لضمان الأمان المالي.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 4. تبويب معالج ردود الشكاوى ومراجعات العملاء -----------------
with tab_review:
    st.markdown("<h3 style='color:#38BDF8;'>💬 نظام معالجة الشكاوى الأوتوماتيكي وصياغة خطط التعويض</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    
    complaint_type = st.radio("حدد نوع المشكلة أو الشكوى الواردة من العميل لتخصيص الحل:", ["تأخر الشحن وتوصيل الطلب", "وصول المنتج تالف أو مكسور", "عدم مطابقة المنتج للوصف المتوقع"])
    cust_name = st.text_input("اسم العميل الغاضب (اختياري):", "أبو فهد")
    complaint_text = st.text_area("نص كلام الشكوى الأصلي للعميل:", "الطلب تأخر علي أكثر من أسبوعين وما أحد يرد علي بالدعم، تعاملكم غير احترافي!")
    
    if st.button("توليد رد امتصاص الغضب وصيغة التعويض الفورية ✨"):
        with st.spinner("جاري فحص النبرة المناسبة لتهدئة العميل..."):
            time.sleep(0.7)
            
            # تخصيص رد حقيقي ديناميكي يتغير كليا بناء على نوع المشكلة المختارة
            if "تأخر" in complaint_type:
                compensation = "شحن سريع مجاني لطلبك الحالي مع كود خصم 20% لطلبك القادم كاعتذار من القلب."
                reason_phrase = "بسبب الضغط الحالي على شركات الشحن واللوجستيات"
            elif "تالف" in complaint_type:
                compensation = "إرسال بديل فوري للمنتج التالف مجاناً بالكامل دون الحاجة لإرجاع المنتج المكسور."
                reason_phrase = "نتيجة خطأ غير مقصود أثناء معالجة الشحنات وتغليفها"
            else:
                compensation = "إتاحة خيار استرجاع المبلغ بالكامل أو استبداله بأي منتج آخر تفضله مع قسيمة شرائية مجانية."
                reason_phrase = "لوجود سوء فهم بسيط في تفاصيل وتحديث مواصفات المنتج"
                
            st.markdown(f"""
            <div class="result-box">
                <h4 style="color:#F3F4F6;">الرد الدبلوماسي الجاهز المولد لإرساله إلى ({cust_name}):</h4>
                <p style="color:#A7F3D0; font-style: italic; font-size:15px; line-height: 1.7;">
                "أهلاً بك عميلنا العزيز {cust_name}، نعتذر منك بشدة وبشكل رسمي عن هذه التجربة غير المرضية والتي لا تمثل قيم منصة رِكاز وجودتها بتاتاً. نحن نتفهم استياءك تماماً {reason_phrase}. وتقديراً لوقتك وولائك لنا، يسعدنا تقديم تعويض فوري لك يشمل: ({compensation}). فريق الدعم يتشرف بخدمتك الحين لإنهاء الإجراءات فوراً وراحتك هي غايتنا الأسمى 🤍"
                </p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 5. تبويب محلل ومحسن صفحات المنتجات -----------------
with tab_seo:
    st.markdown("<h3 style='color:#38BDF8;'>🔍 معالج ومحسن السيو (SEO) لرفع تصنيف المتاجر في قوقل</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    
    prod_keyword = st.text_input("الكلمة المفتاحية المستهدفة (مثال: عطر شتوي، سماعة لاسلكية):", "عطر فرنسي فخم")
    old_seo = st.text_area("اكتب الوصف العادي والبدائي للمنتج حالياً:", "عطر رائحته جميلة وممتازة وثابت ومناسب للهدايا وسعره مناسب.")
    
    if st.button("توليد الكلمات الدلالية وتهيئة أكواد الميتا تاقز 🚀"):
        with st.spinner("جاري فحص خوارزميات قوقل ومعدلات البحث..."):
            time.sleep(0.8)
            st.markdown(f"""
            <div class="result-box">
                <h4 style="color:#38BDF8; margin:0 0 10px 0;">🎯 بيانات الـ SEO والوصف الجاذب للمشترين ومحركات البحث:</h4>
                <p><b>• العنوان المحسن والمقترح لصفحة المنتج (Title Tag):</b> أفضل {prod_keyword} ثابث وفوّاح لعام 2026 - متجرك الرسمي</p>
                <p><b>• الوصف الميتا الذكي (Meta Description):</b> هل تبحث عن التميز؟ اكتشف أرقى {prod_keyword} مصمم بتركيبة عطرية ساحرة تمنحك الثقة والفوحان العالي طوال اليوم. مناسب لجميع المناسبات الفخمة ولتقديم كهدية قيمة لمن تحب. اطلبه الآن للاستفادة من خصوماتنا الحصرية!</p>
                <p><b>• الكلمات الدلالية المستهدفة للنسخ (Tags / Keywords):</b> {prod_keyword}, عطورات ثابته, عطر اصلي, عطور شتوية, متجر عطور, توصيل سريع</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- 6. تبويب صانع أفكار الفيديوهات القصيرة -----------------
with tab_video:
    st.markdown("<h3 style='color:#38BDF8;'>🎬 صانع سكريبتات وسيناريوهات الفيديوهات الفيرال والتسويقية القصيرة</h3>", unsafe_allow_html=True)
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    
    video_prod_input = st.text_input("ما هو المنتج المستهدف للتصوير الإعلاني؟", "نظارات شمسية ذكية")
    video_target = st.selectbox("🎯 الهدف الإعلاني للفيديو القصير:", ["زيادة الوعي بالبراند وجلب مشاهدات عالية (Viral)", "بيع مباشر للمنتج عبر عرض مغري وصادم (Conversion)"])
    
    if st.button("توليد وتخطيط سكريبت الفيديو الاحترافي التفاعلي 🎬"):
        with st.spinner("جاري ابتكار خطافات بصرية مشوقة للثواني الأولى..."):
            time.sleep(1)
            
            if "Viral" in video_target:
                hook_text = "ابدأ بلقطة قريبة وصادمة وأنت ترمي النظارات القديمة في سلة المهملات وتقول: 'الموضة هذي انتهت خلاص! شوف المستقبل وين وصل الحين!'"
                body_text = "استعرض التقنية الداخلية للنظارة والعدسات الذكية وحماية العين من الأشعة والوهج بشكل سينمائي مبهر مع موسيقى حماسية هادئة الخلفية."
                cta_text = "تابِع حسابنا لتشوف أحدث التقنيات الغريبة اللي بتنزل قريباً في السوق!"
            else:
                hook_text = "ابدأ الفيديو بلقطة سريعة ومقربة للشاشة والأسعار مكتوب عليها خصم 50% واصرخ بنبرة حماسية: 'تصفية كبرى لنهاية الموسم، العرض هذا حرفياً ما يتفوت!'"
                body_text = "أظهر شكل النظارة الأنيق أثناء ارتدائها الفعلي في وضح النهار مع إبراز فخامة العبوة والتغليف والميزات الملحقة التي يحصل عليها المشتري مجاناً."
                cta_text = "العرض متاح لأول 100 طلب بس والشحن مجاني، اضغط على الرابط في البايو واطلب نظارتك الحين!"
                
            st.markdown(f"""
            <div class="result-box" style="border-right-color: #818CF8;">
                <h4 style="color:#818CF8; margin:0 0 12px 0;">🎬 الهيكلية الاحترافية لسيناريو فيديو منتج: ({video_prod_input})</h4>
                <p><b>• أول 3 ثواني (الخطاف البصري لجذب الانتباه ومنع التمرير):</b> {hook_text}</p>
                <p><b>• منتصف الفيديو (استعراض الميزات وصناعة الرغبة بالشراء):</b> {body_text}</p>
                <p><b>• آخر 3 ثواني (طلب الفعل المباشر وصناعة الاستعجال - CTA):</b> <span style="color:#34D399; font-weight:bold;">{cta_text}</span></p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
