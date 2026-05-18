import streamlit as st
import requests

# إعداد واجهة البرنامج المتقدمة
st.set_page_config(page_title="منصة لؤي تيك الذكية", page_icon="🚀", layout="centered")

st.title("🚀 منصة لؤي تيك للتصميم الإعلاني المحترف")
st.write("صمم بوسترات منتجاتك الإعلانية فوراً وبأعلى سرعة وحملها مباشرة!")

# خانات الإدخال والتحكم الاحترافية
product_name = st.text_input("📦 اسم المنتج (بالإنجليزية)", placeholder="مثال: Dior Sauvage perfume")

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("🎨 نمط التصميم الإعلاني", [
        "سينمائي فخم (Cinematic)", 
        "استوديو مودرن (Modern Studio)", 
        "خلفية طبيعية (Natural/Volcanic)",
        "نيون وغموض (Neon Cyberpunk)"
    ])

with col2:
    dimension = st.selectbox("📏 أبعاد البوستر الإعلاني", [
        "مربع (Instagram Post) 1:1", 
        "طولي (TikTok / Story) 9:16"
    ])

# زر البدء بالتصميم
if st.button("🔥 أطلق العنان واصنع التصميم الآن"):
    if not product_name:
        st.warning("⚠️ من فضلك اكتب اسم المنتج أولاً!")
    else:
        with st.spinner("⏳ جاري تصميم البوستر الأسطوري في ثوانٍ معدودة..."):
            try:
                # تحديد الأبعاد بدقة
                width, height = 1024, 1024
                if "9:16" in dimension:
                    width, height = 1024, 1792

                # تخصيص الوصف بناءً على خيارات العميل
                style_prompt = ""
                if "Cinematic" in style:
                    style_prompt = "dramatic dark luxury cinematic lighting, central composition, dark background, golden hour rims"
                elif "Modern" in style:
                    style_prompt = "clean minimalist light gray studio background, soft shadows, high-end commercial look"
                elif "Natural" in style:
                    style_prompt = "standing majestic on a dark volcanic rock surrounded by splashing clean water"
                else:
                    style_prompt = "glowing neon lights, cyberpunk aesthetic, dark violet and cyan contrast reflection"

                magical_prompt = f"Professional luxury advertising studio photography of {product_name}, {style_prompt}, hyper-realistic, 8k resolution, commercial grade masterpiece."
                
                # رابط السيرفر السريع والمستقر جداً
                image_url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(magical_prompt)}?width={width}&height={height}&model=flux&nologo=true&seed=42"
                
                # جلب الصورة
                response = requests.get(image_url)
                
                if response.status_code == 200:
                    image_bytes = response.content
                    st.success("✨ تم تصميم البوستر بنجاح خرافي!")
                    
                    # عرض الصورة الفخمة
                    st.image(image_bytes, caption=f"إعلان احترافي لـ {product_name}", use_container_width=True)
                    
                    # 💾 زر تحميل الصورة المباشر بجودة عالية
                    st.download_button(
                        label="💾 تحميل البوستر الإعلاني بجودة عالية",
                        data=image_bytes,
                        file_name=f"{product_name.replace(' ', '_')}_poster.png",
                        mime="image/png"
                    )
                    
                    # توليد النص الإعلاني الذكي
                    st.subheader("📝 النص التسويقي المقترح للمنتج:")
                    product_tag = product_name.replace(" ", "_")
                    ad_copy = f"""
                    📢 **سر الجاذبية المطلقة بين يديك!** 💎
                    
                    تميز بحضور لا يُنسى مع **{product_name}**. التصميم الأنيق الذي يعبر عن شخصيتك الفريدة ويخطف الأنظار من أول ثانية.
                    
                    🌟 **عرض لؤي تيك:** توصيل سريع مجاني + الدفع عند الاستلام!
                    🔗 اضغط على الرابط في البايو واطلبه الآن.
                    
                    #فخامة #{product_tag} #تسويق_ذكي #أناقة_متاجر #ترند
                    """
                    st.info(ad_copy)
                else:
                    st.error("❌ حدثت مشكلة بسيطة في الاتصال، اضغط على زر التصميم مرة أخرى.")
                
            except Exception as e:
                st.error(f"❌ عذراً، حدث خطأ أثناء التوليد: {str(e)}")

st.markdown("---")
st.caption("تطوير منصة لؤي تيك الذكية v3.0 🚀")