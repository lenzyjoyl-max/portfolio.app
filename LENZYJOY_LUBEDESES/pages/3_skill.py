import streamlit as st

st.set_page_config(page_title="Skills - Lenzy Joy", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:2.8rem; background:linear-gradient(135deg,#3498db,#2980b9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-align:center;}
.info-card {background:white; padding:1.5rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.08); border-left:4px solid #3498db; color:#2c3e50;}
.main .block-container {background-color:#fafbfc;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🛠️ My Skills</h1>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💻 Technical Skills", "🤝 Soft Skills"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Programming")
        st.progress(0.85); st.caption("🐍 Python - 85%")
        st.progress(0.75); st.caption("🌐 HTML/CSS/JS - 75%")
        st.progress(0.90); st.caption("⚡ Streamlit - 90%")
    
    with col2:
        st.subheader("Tools")
        st.progress(0.70); st.caption("🔧 Git/GitHub - 70%")
        st.progress(0.65); st.caption("📊 Databases - 65%")
        st.progress(0.60); st.caption("🔌 APIs - 60%")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Problem Solving", "85%")
        st.metric("Teamwork", "80%")
        st.metric("Learning", "90%")
    with col2:
        st.metric("Time Management", "88%")
        st.metric("Communication", "75%")
        st.metric("Adaptability", "82%")

st.markdown("""
<div class="info-card" style="text-align:center;">
    <h3 style="color:#3498db;">📈 Learning Now</h3>
    <p>React.js • Data Analysis • Full-Stack Development</p>
</div>
""", unsafe_allow_html=True)