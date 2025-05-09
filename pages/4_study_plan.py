import streamlit as st
from utils.openai_tools import generate_study_plan

st.set_page_config(
    page_title="Study Plan - ExamPrepAI",
    page_icon="📅",
    layout="wide"
)

# Check for API key
if 'gemini_api_key' not in st.session_state:
    st.warning("Please set up your Gemini API key on the main page first.")
    if st.button("🏠 Go to Main Page"):
        st.switch_page("app.py")
else:
    st.title("📅 Study Plan Generator")
    st.markdown("Create personalized study plans based on your syllabus and exam date.")
    
    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        subject = st.text_input("📚 Subject:", 
                              placeholder="Enter your subject...")
        exam_date = st.date_input("📅 Exam Date:")
    with col2:
        topics = st.text_area("📝 Topics (one per line):", 
                            placeholder="Enter your topics here...",
                            height=100)
        study_hours = st.number_input("⏰ Daily Study Hours:", 
                                    min_value=1, 
                                    max_value=12, 
                                    value=4)
    
    # Advanced options
    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            difficulty_level = st.select_slider(
                "Difficulty Level",
                options=["Beginner", "Intermediate", "Advanced"],
                value="Intermediate"
            )
        with col2:
            include_breaks = st.checkbox("Include Break Times", value=True)
            include_revision = st.checkbox("Include Revision Days", value=True)
    
    if st.button("📖 Generate Study Plan", use_container_width=True) and subject and topics:
        with st.spinner("Generating study plan..."):
            # Prepare the prompt with all options
            prompt = f"Subject: {subject}\n"
            prompt += f"Exam Date: {exam_date}\n"
            prompt += f"Topics:\n{topics}\n"
            prompt += f"Daily Study Hours: {study_hours}\n"
            prompt += f"Difficulty Level: {difficulty_level}\n"
            
            if include_breaks:
                prompt += "Include break times in the schedule.\n"
            if include_revision:
                prompt += "Include dedicated revision days.\n"
            
            study_plan = generate_study_plan(prompt, st.session_state['gemini_api_key'])
            
            # Display the study plan in a nice format
            st.markdown("### 📖 Generated Study Plan")
            st.markdown(study_plan)
            
            # Add download button
            st.download_button(
                label="📥 Download Study Plan",
                data=study_plan,
                file_name=f"study_plan_{subject.replace(' ', '_')}.txt",
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
                    st.info("We'll try to improve our study plans.")
            with col3:
                if st.button("🔄 Generate New Plan"):
                    st.rerun() 