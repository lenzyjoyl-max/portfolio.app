import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Lenzy Joy Portfolio", page_icon="🎓", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:3rem; background:linear-gradient(135deg,#3498db,#2980b9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-align:center;}
.sub-header {font-family:'Poppins'; color:#2c3e50; text-align:center; font-size:1.4rem;}
.metric-card {background:linear-gradient(135deg,#3498db,#2980b9); color:white; padding:2rem; border-radius:15px; text-align:center;}
.info-card {background:white; padding:1.8rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.08); border-left:4px solid #3498db; color:#2c3e50;}
.stButton > button {background:linear-gradient(135deg,#3498db,#2980b9); color:white !important; border-radius:25px; font-weight:600;}
.main .block-container {background-color:#fafbfc;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">👋 Welcome to My Portfolio</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Lenzy Joy C. Lubedeses<br>3rd Year DEBESMSCAT Student</p>', unsafe_allow_html=True)

# Stats Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">20</h2><p>Years Old</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">3rd</h2><p>Year Student</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">🎓</h2><p>DEBESMSCAT</p></div>', unsafe_allow_html=True)

# Contact Info
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#3498db;">📍 Address</h3>
        <p><strong>Sitio Bart-ag</strong><br>Concepcion, Aroroy<br>Masbate</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#3498db;">📧 Contact</h3>
        <p><strong>lenzyjoyl@gmail.com</strong><br><strong>0930-899-0394</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Birthday Counter
st.markdown("---")
today = datetime.now()
next_bday = datetime(today.year + 1, 9, 20) if today.month > 9 or (today.month == 9 and today.day >= 20) else datetime(today.year, 9, 20)
days_left = (next_bday - today).days
st.subheader("🎂 Days Until Birthday")
st.metric("Days Left", f"{days_left} days", f"Sep 20, {next_bday.year}")

st.markdown("---")
st.markdown("<p style='text-align:center;color:#7f8c8d;font-family:Poppins;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)