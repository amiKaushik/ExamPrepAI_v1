import streamlit as st
from utils.ai_tools import ask_ai_question

st.set_page_config(
    page_title="Question Answering - ExamPrepAI",
    page_icon="📝",
    layout="wide"
)

if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📝 AI Question Answering")
    st.markdown("Ask any study-related questions and get instant, accurate answers.")

    st.subheader("Your Question")
    context = st.text_area(
        "📚 Context (optional):", 
        placeholder="Add any relevant context or background information...", 
        height=100
    )
    question = st.text_input(
        "❓ Your Question:", 
        placeholder="Type your question here..."
    )

    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            detail_level = st.select_slider(
                "Detail Level",
                options=["Concise", "Balanced", "Detailed"],
                value="Balanced"
            )
        with col2:
            include_examples = st.checkbox("Include Examples", value=True)

    file_format = st.radio("Choose file format for download:", ("TXT", "Markdown"))

    if st.button("🤖 Get Answer", use_container_width=True) and question:
        with st.spinner("Generating answer..."):
            full_prompt = f"Context: {context}\n\nQuestion: {question}\n\n"
            if detail_level == "Concise":
                full_prompt += "Please provide a concise answer."
            elif detail_level == "Detailed":
                full_prompt += "Please provide a detailed answer with explanations."

            if include_examples:
                full_prompt += " Include relevant examples."

            answer = ask_ai_question(full_prompt, st.session_state['gemini_api_key'])

            st.markdown("### 📖 Answer")
            st.markdown(answer, unsafe_allow_html=True)

            if file_format == "TXT":
                answer_plain_text = answer.replace("**", "").replace("*", "").replace("`", "")
                st.download_button(
                    label="📥 Download Answer as TXT",
                    data=answer_plain_text,
                    file_name="ai_answer.txt",
                    mime="text/plain"
                )
            else:
                st.download_button(
                    label="📥 Download Answer as Markdown",
                    data=answer,
                    file_name="ai_answer.md",
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
                    st.info("We'll try to improve our answers.")
            with col3:
                if st.button("🔄 Ask Another Question"):
                    st.rerun()
