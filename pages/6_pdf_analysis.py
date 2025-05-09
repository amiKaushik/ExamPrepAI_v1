import streamlit as st
import PyPDF2
from utils.openai_tools import analyze_pdf

st.set_page_config(
    page_title="PDF Analysis - ExamPrepAI",
    page_icon="📄",
    layout="wide"
)

# Check for API key
if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📄 PDF Analysis")
    st.markdown("Upload and analyze your study materials with AI assistance.")
    
    # File upload
    uploaded_file = st.file_uploader("📄 Upload PDF:", type=['pdf'])
    
    if uploaded_file is not None:
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Display PDF info
        st.info(f"📚 PDF Info: {len(pdf_reader.pages)} pages")
        
        # Analysis options
        with st.expander("⚙️ Analysis Options"):
            col1, col2 = st.columns(2)
            with col1:
                analysis_type = st.selectbox(
                    "Analysis Type",
                    ["Summary", "Key Points", "Questions", "Full Analysis"],
                    index=0
                )
            with col2:
                include_examples = st.checkbox("Include Examples", value=True)
                include_definitions = st.checkbox("Include Definitions", value=True)
        
        if st.button("📖 Analyze PDF", use_container_width=True):
            with st.spinner("Analyzing PDF..."):
                # Prepare the prompt with options
                prompt = f"Analyze this text:\n{text}\n\n"
                prompt += f"Analysis Type: {analysis_type}\n"
                
                if include_examples:
                    prompt += "Include relevant examples.\n"
                if include_definitions:
                    prompt += "Include key definitions.\n"
                
                analysis = analyze_pdf(prompt, st.session_state['gemini_api_key'])
                
                # Display the analysis in a nice format
                st.markdown("### 📖 Analysis Results")
                st.markdown(analysis)
                
                # Add download button
                st.download_button(
                    label="📥 Download Analysis",
                    data=analysis,
                    file_name=f"pdf_analysis_{uploaded_file.name.replace('.pdf', '')}.txt",
                    mime="text/plain"
                )
                
                # Add a feedback section
                st.markdown("---")
                st.markdown("### 💭 Was this helpful?")
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("👍 Yes"):
                        st.success("Thank you for your feedback!")
                with col2:
                    if st.button("👎 No"):
                        st.info("We'll try to improve our analysis.")
                with col3:
                    if st.button("🔄 Analyze Another PDF"):
                        st.rerun() 