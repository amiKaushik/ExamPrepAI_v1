import streamlit as st
from utils.ai_tools import generate_study_notes

st.set_page_config(
    page_title="Study Notes - ExamPrepAI",
    page_icon="📚",
    layout="wide"
)

if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📚 Study Notes Generator")
    st.markdown("Generate comprehensive study notes on any topic.")

    topic = st.text_input("📝 Topic:", placeholder="Enter the topic you want to study...")

    syllabus = st.text_area(
        "📋 Syllabus (Optional):",
        placeholder="Paste the syllabus outline or bullet points if you have them...",
        height=120
    )

    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            detail_level = st.select_slider(
                "Detail Level",
                options=["Basic", "Comprehensive", "In-depth"],
                value="Comprehensive"
            )
        with col2:
            include_examples = st.checkbox("Include Examples", value=True)
            include_diagrams = st.checkbox("Include Diagram Descriptions", value=True)

    file_format = st.radio("Choose file format for download:", ("TXT", "Markdown"))

    if st.button("📖 Generate Notes", use_container_width=True) and topic:
        with st.spinner("Generating study notes..."):
            prompt = f"Generate study notes on the topic: {topic}.\n"
            if syllabus.strip():
                prompt += f"\nFocus especially on the following syllabus outline:\n{syllabus.strip()}\n"
            if detail_level == "Basic":
                prompt += "\nProvide basic concepts and key points."
            elif detail_level == "In-depth":
                prompt += "\nProvide detailed explanations with advanced concepts."
            if include_examples:
                prompt += " Include practical examples."
            if include_diagrams:
                prompt += " Include descriptions of relevant diagrams or visual aids."

            notes = generate_study_notes(prompt, st.session_state['gemini_api_key'])

            st.markdown("### 📖 Generated Notes")
            st.markdown(notes)

            if file_format == "TXT":
                st.download_button(
                    label="📥 Download Notes as TXT",
                    data=notes,
                    file_name=f"study_notes_{topic.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            else:
                st.download_button(
                    label="📥 Download Notes as Markdown",
                    data=notes,
                    file_name=f"study_notes_{topic.replace(' ', '_')}.md",
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
                    st.info("We'll try to improve our notes.")
            with col3:
                if st.button("🔄 Generate New Notes"):
                    st.rerun()
