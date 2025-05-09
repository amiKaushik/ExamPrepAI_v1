import streamlit as st
from utils.ai_tools import generate_mock_questions

st.set_page_config(
    page_title="Mock Questions - ExamPrepAI",
    page_icon="📝",
    layout="wide"
)

if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📝 Mock Exam Questions")
    st.markdown("Generate practice questions and test your knowledge.")
    
    subject = st.text_input("📚 Subject:", placeholder="Enter your subject...")
    topics = st.text_area("📝 Topics (one per line):", placeholder="Enter topics to generate questions for...", height=100)
    
    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            question_type = st.multiselect(
                "Question Types",
                ["Multiple Choice", "Short Answer", "Long Answer", "True/False"],
                default=["Multiple Choice", "Short Answer"]
            )
            num_questions = st.number_input("Number of Questions:", min_value=1, max_value=20, value=5)
        with col2:
            difficulty = st.select_slider("Difficulty Level", options=["Easy", "Medium", "Hard"], value="Medium")
            include_answers = st.checkbox("Include Answers", value=True)
    
    if st.button("📖 Generate Questions", use_container_width=True) and subject and topics:
        with st.spinner("Generating questions..."):
            prompt = f"Subject: {subject}\n"
            prompt += f"Topics:\n{topics}\n"
            prompt += f"Question Types: {', '.join(question_type)}\n"
            prompt += f"Number of Questions: {num_questions}\n"
            prompt += f"Difficulty: {difficulty}\n"
            
            if include_answers:
                prompt += "Include answers for each question.\n"
            
            questions = generate_mock_questions(prompt, st.session_state['gemini_api_key'])
            
            st.markdown("### 📖 Generated Questions")
            st.markdown(questions)
            
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="📥 Download as TXT",
                    data=questions,
                    file_name=f"mock_questions_{subject.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            with col2:
                st.download_button(
                    label="📥 Download as Markdown",
                    data=questions,
                    file_name=f"mock_questions_{subject.replace(' ', '_')}.md",
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
                    st.info("We'll try to improve our questions.")
            with col3:
                if st.button("🔄 Generate New Questions"):
                    st.rerun()
