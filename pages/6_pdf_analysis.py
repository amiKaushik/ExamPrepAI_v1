import streamlit as st
import PyPDF2
from utils.ai_tools import analyze_pdf

st.set_page_config(
    page_title="PDF Analysis - ExamPrepAI",
    page_icon="📄",
    layout="wide"
)

if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📄 PDF Analysis")
    st.markdown("Upload and analyze your study materials with AI assistance.")
    
    uploaded_file = st.file_uploader("📄 Upload PDF:", type=['pdf'])
    
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join([page.extract_text() for page in pdf_reader.pages])
        
        st.info(f"📚 PDF Info: {len(pdf_reader.pages)} pages")

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

        file_format = st.radio("Choose file format for download:", ("Markdown", "Plain Text"))
        
        if st.button("📖 Analyze PDF", use_container_width=True):
            with st.spinner("Analyzing PDF..."):
                prompt = f"Analyze this text:\n{text}\n\n"
                prompt += f"Analysis Type: {analysis_type}\n"
                if include_examples:
                    prompt += "Include relevant examples.\n"
                if include_definitions:
                    prompt += "Include key definitions.\n"
                if file_format == "Markdown":
                    prompt += "Format the analysis using Markdown (headings, lists, emphasis, etc.).\n"
                else:
                    prompt += "Generate the analysis in plain text format without any Markdown formatting.\n"
                
                analysis = analyze_pdf(prompt, st.session_state['gemini_api_key'])

                st.markdown("### 📖 Analysis Results")
                st.markdown(analysis)
                
                if file_format == "Plain Text":
                    st.download_button(
                        label="📥 Download as TXT",
                        data=analysis,
                        file_name=f"pdf_analysis_{uploaded_file.name.replace('.pdf', '')}.txt",
                        mime="text/plain"
                    )
                else:
                    st.download_button(
                        label="📥 Download as Markdown",
                        data=analysis,
                        file_name=f"pdf_analysis_{uploaded_file.name.replace('.pdf', '')}.md",
                        mime="text/markdown"
                    )

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
