import streamlit as st

st.set_page_config(page_title="About - Lenzy Joy", layout="wide")

# Fixed CSS - Better spacing & no overflow
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
/* Header */
.main-header { 
    font-family:'Poppins', sans-serif; 
    font-size:2.5rem; 
    font-weight:700;
    background:linear-gradient(135deg,#3498db,#2980b9); 
    -webkit-background-clip:text; 
    -webkit-text-fill-color:transparent; 
    background-clip:text; 
    text-align:center;
    margin-bottom:1.5rem;
    line-height:1.2;
}

/* Cards */
.info-card { 
    background:white; 
    padding:1.8rem; 
    border-radius:12px; 
    box-shadow:0 8px 25px rgba(0,0,0,0.1); 
    border-left:5px solid #3498db; 
    color:#2c3e50; 
    margin:1rem 0;
    min-height:180px;
}

/* Metrics fix - No overflow */
.stMetric {
    margin:0.5rem 0;
}

.stMetric > label {
    font-size:0.9rem !important;
    color:#2c3e50 !important;
    font-weight:500;
    white-space: normal !important;
    line-height:1.3;
}

.stMetric > div > div {
    font-size:1.4rem !important;
    color:#3498db !important;
    font-weight:600;
}

/* Main background */
.main .block-container { 
    background-color:#fafbfc; 
    padding-top:1rem;
}

/* Subheaders */
h2 {
    font-family:'Poppins', sans-serif;
    color:#2c3e50;
    font-weight:600;
    font-size:1.6rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">👩‍🎓 About Me</h1>', unsafe_allow_html=True)

# Personal Info - Fixed spacing & wrapping
st.markdown("---")
st.subheader("📋 Personal Information")

col1, col2, col3, col4 = st.columns(4, gap="small")
with col1:
    st.markdown("""
    <div style="text-align:center; padding:1rem; background:#f8f9ff; border-radius:10px; border:2px solid #3498db;">
        <h4 style="color:#3498db; margin:0.5rem 0;">👤 Full Name</h4>
        <p style="font-size:1rem; font-weight:600; margin:0.5rem 0; color:#2c3e50;">Lenzy Joy C. Lubedeses</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric("🎂 Age", "20")

with col3:
    st.metric("📅 Birth Date", "Sep 20, 2005")

with col4:
    st.metric("🎓 Status", "3rd Year DEBESMSCAT")

# About Me Sections - Better spacing
st.markdown("---")
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#3498db; margin-bottom:1rem;">📖 My Journey</h3>
        <p style="line-height:1.6; font-size:1rem;">
        Passionate 3rd-year student at <strong>DEBESMSCAT</strong> learning 
        programming and web development. From beautiful Masbate, building 
        my tech career with dedication!
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#3498db; margin-bottom:1rem;">📍 Contact Details</h3>
        <div style="font-size:1.1rem; line-height:1.6;">
            <p><strong>📧 Email:</strong><br>lenzyjoyl@gmail.com</p>
            <p><strong>📱 Phone:</strong><br>0930-899-0394</p>
            <p><strong>📍 Address:</strong><br>Sitio Bart-ag<br>Concepcion, Aroroy<br>Masbate</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Education Section - Fixed layout
st.markdown("---")
st.markdown('<h2 style="text-align:center;">🎓 Education Journey</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="info-card">
        <h4 style="color:#3498db; margin-bottom:0.8rem;">🏫 Elementary</h4>
        <p style="margin:0; font-size:1.1rem; font-weight:500;">Concepcion Aroroy Masbate</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card" style="border-left:5px solid #27ae60;">
        <h4 style="color:#27ae60; margin-bottom:0.8rem;">🎓 College (Current)</h4>
        <p style="margin:0 0 0.5rem 0; font-size:1.1rem; font-weight:600;">3rd Year Student</p>
        <p style="margin:0; font-size:1rem;">DEBESMSCAT</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4 style="color:#3498db; margin-bottom:0.8rem;">🎒 High School</h4>
        <p style="margin:0; font-size:1.1rem; font-weight:500;">Luy-a National High School</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding:2rem; background:#f8f9ff; border-radius:12px; margin-top:2rem;">
    <p style="color:#7f8c8d; font-family:'Poppins'; font-size:1.1rem; margin:0;">
        Ready to build amazing things together! ✨
    </p>
</div>
""", unsafe_allow_html=True)