import streamlit as st
from utils.ai_tools import summarize_text

st.set_page_config(
    page_title="Text Summarization - ExamPrepAI",
    page_icon="📑",
    layout="wide"
)

if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📑 Text Summarization")
    st.markdown("Get concise summaries of your study materials.")

    text = st.text_area("📝 Enter your text:", placeholder="Paste your text here...", height=300)

    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            summary_length = st.select_slider(
                "Summary Length",
                options=["Very Short", "Short", "Medium", "Detailed"],
                value="Medium"
            )
        with col2:
            include_key_points = st.checkbox("Include Key Points", value=True)
            include_bullet_points = st.checkbox("Use Bullet Points", value=True)

    if st.button("📖 Generate Summary", use_container_width=True) and text:
        with st.spinner("Generating summary..."):
            prompt = f"Summarize the following text:\n{text}\n\n"
            if summary_length == "Very Short":
                prompt += "Provide a very concise summary (2-3 sentences)."
            elif summary_length == "Short":
                prompt += "Provide a brief summary (1-2 paragraphs)."
            elif summary_length == "Detailed":
                prompt += "Provide a detailed summary with main points."

            if include_key_points:
                prompt += " Include key points."
            if include_bullet_points:
                prompt += " Use bullet points for better readability."

            summary = summarize_text(prompt, st.session_state['gemini_api_key'])

            st.markdown("### 📖 Generated Summary")
            st.markdown(summary)

            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="text_summary.md",
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
                    st.info("We'll try to improve our summaries.")
            with col3:
                if st.button("🔄 Generate New Summary"):
                    st.rerun()
