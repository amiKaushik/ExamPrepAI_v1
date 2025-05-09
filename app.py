import streamlit as st

st.set_page_config(
    page_title="App Home - ExamPrepAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin: 0.5rem 0;
        padding: 1rem;
        border-radius: 10px;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Gemini API key input in sidebar
if 'gemini_api_key' not in st.session_state:
    st.sidebar.subheader("🔑 API Key Setup")
    gemini_key = st.sidebar.text_input("Enter your Gemini API key:", type="password")
    if gemini_key:
        st.session_state['gemini_api_key'] = gemini_key
        st.sidebar.success("API key saved!")
        st.rerun()
else:
    st.sidebar.success("✅ API key configured")
    if st.sidebar.button("🔄 Change API Key"):
        del st.session_state['gemini_api_key']
        st.rerun()

# Main content
st.title("🏠 App Home")
st.markdown("---")
st.markdown("Your personalized AI study companion for efficient exam preparation")

# Feature cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📝 AI Question Answering</h3>
        <p>Ask any study-related questions and get instant, accurate answers.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📚 Study Notes Generator</h3>
        <p>Generate comprehensive study notes on any topic.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📑 Text Summarization</h3>
        <p>Get concise summaries of your study materials.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📅 Study Plan Generator</h3>
        <p>Create personalized study plans based on your syllabus and exam date.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📝 Mock Exam Questions</h3>
        <p>Generate practice questions and test your knowledge.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📄 PDF Analysis</h3>
        <p>Upload and analyze your study materials with AI assistance.</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation buttons
st.markdown("### 🚀 Quick Navigation")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Ask Questions", use_container_width=True):
        st.switch_page("pages/1_question_answering.py")
    if st.button("📚 Generate Notes", use_container_width=True):
        st.switch_page("pages/2_study_notes.py")

with col2:
    if st.button("📑 Summarize Text", use_container_width=True):
        st.switch_page("pages/3_text_summarization.py")
    if st.button("📅 Create Study Plan", use_container_width=True):
        st.switch_page("pages/4_study_plan.py")

with col3:
    if st.button("📝 Practice Questions", use_container_width=True):
        st.switch_page("pages/5_mock_questions.py")
    if st.button("📄 PDF Analysis", use_container_width=True):
        st.switch_page("pages/6_pdf_analysis.py")

# Footer
st.markdown("""
    <style>
    .footer {
        background-color: #2c2c2c;
        color: #f1f1f1;
        padding: 10px;
        text-align: center;
        position: relative;
        width: 100%;
        bottom: 0;
    }
    .content {
        min-height: calc(100vh - 200px);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    a {
        color: #64b5f6;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="content">
        <div></div>
        <div class="footer">
            <p><b>Contact Us</b></p>
            <p>Ping me on GitHub: <a href="https://github.com/amiKaushik" target="_blank">https://github.com/amiKaushik</a></p>
        </div>
    </div>
""", unsafe_allow_html=True)