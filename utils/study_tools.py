import google.generativeai as genai

def generate_study_notes(topic, api_key):
    """
    Generate a set of study notes based on a given topic.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        prompt = f"Generate comprehensive study notes for the topic: {topic}. Include key concepts, definitions, and important points."
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def summarize_text(text, api_key):
    """
    Summarize the given text to help students with quick revision.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        prompt = f"Summarize the following text in a concise and clear manner, highlighting the key points:\n\n{text}"
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_study_plan(subject, duration_weeks, api_key):
    """
    Generate a personalized study plan based on subject and study duration.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        prompt = f"Create a detailed {duration_weeks}-week study plan for learning {subject}. Include weekly goals, study topics, and recommended resources."
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_mock_questions(topic, api_key):
    """
    Generate a list of sample questions for mock exam practice on a specific topic.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        prompt = f"Generate a comprehensive list of mock exam questions for the topic: {topic}. Include different types of questions (multiple choice, short answer, and long answer) with varying difficulty levels."
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def analyze_pdf(text, prompt, api_key):
    """
    Analyze PDF content using AI to provide insights, summaries, and key points.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the full prompt
        full_prompt = f"Analyze the following text based on these requirements:\n{prompt}\n\nText to analyze:\n{text}"
        
        # Generate response
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"
