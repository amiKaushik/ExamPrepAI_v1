import google.generativeai as genai
import streamlit as st

def configure_genai(api_key):
    """Configure the Gemini API with the provided API key."""
    try:
        genai.configure(api_key=api_key)
        # List available models
        models = [m.name for m in genai.list_models()]
        st.sidebar.info(f"Available models: {', '.join(models)}")
        return True
    except Exception as e:
        st.error(f"Error configuring Gemini API: {str(e)}")
        return False

def get_model():
    """Get the appropriate Gemini model."""
    try:
        # Use gemini-1.5-flash model
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        return model
    except Exception as e:
        st.error(f"Error getting model: {str(e)}")
        return None

def ask_ai_question(prompt, api_key):
    """Ask a question to the AI and get a response."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def generate_study_notes(prompt, api_key):
    """Generate study notes based on the given topic."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating study notes: {str(e)}"

def summarize_text(prompt, api_key):
    """Summarize the given text."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def generate_study_plan(prompt, api_key):
    """Generate a study plan based on the given parameters."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating study plan: {str(e)}"

def generate_mock_questions(prompt, api_key):
    """Generate mock exam questions based on the given parameters."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating questions: {str(e)}"

def analyze_pdf(prompt, api_key):
    """Analyze PDF content using AI."""
    if not configure_genai(api_key):
        return "Error: Could not configure Gemini API."
    
    model = get_model()
    if not model:
        return "Error: Could not get Gemini model."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing PDF: {str(e)}"
