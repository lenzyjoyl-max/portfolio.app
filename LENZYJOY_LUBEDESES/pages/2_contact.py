import streamlit as st

st.set_page_config(page_title="Contact - Lenzy Joy", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:2.8rem; background:linear-gradient(135deg,#3498db,#2980b9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-align:center;}
.info-card {background:white; padding:1.8rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.08); border-left:4px solid #3498db; color:#2c3e50;}
.main .block-container {background-color:#fafbfc;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📞 Contact Me</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card" style="background:linear-gradient(135deg,#3498db,#2980b9); color:white; text-align:center;">
        <h2>📧 Reach Out</h2>
        <p style="font-size:1.3rem;"><strong>lenzyjoyl@gmail.com</strong></p>
        <p style="font-size:1.2rem;"><strong>📱 0930-899-0394</strong></p>
        <p>📍 Sitio Bart-ag, Concepcion<br>Aroroy, Masbate</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="height:280px; background:linear-gradient(135deg,#e3f2fd,#bbdefb); border-radius:12px; 
                display:flex; align-items:center; justify-content:center; text-align:center;">
        <div style="color:#1976d2;">
            <h3>📍 Masbate, Philippines</h3>
            <p>🌴 My Beautiful Hometown</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Contact Form
st.markdown("---")
st.subheader("💌 Send Message")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Your Name *")
        email = st.text_input("📧 Your Email *")
    with col2:
        subject = st.text_input("📝 Subject *")
        phone = st.text_input("📱 Your Phone")
    
    message = st.text_area("💬 Your Message *", height=120)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.form_submit_button("🚀 Send Message", use_container_width=True):
            if name and email and subject and message:
                st.success("✅ Message sent successfully! 🎉")
                st.balloons()
            else:
                st.error("❌ Please fill all required fields!")

st.markdown("---")
st.markdown("<p style='text-align:center;color:#7f8c8d;font-family:Poppins;'>Available for projects & collaboration! ✨</p>", unsafe_allow_html=True)