# ExamPrepAI
[![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png)](https://examprepaiv1-wq2cvsjsv8l2axouj7whz3.streamlit.app/)

**ExamPrepAI** is an AI-powered study assistant built with Streamlit. It helps students and learners generate study materials, practice questions, and summaries from their notes or textbooks using OpenAI's language models.

## Features

- 📄 **PDF Analysis**: Upload PDFs and extract key concepts.
- ❓ **Question Answering**: Ask questions based on your study material.
- 📝 **Study Notes Generator**: Generate concise study notes from content.
- 🧠 **Text Summarization**: Summarize long documents quickly.
- 📅 **Study Plan Creator**: Build customized study schedules.
- 🎓 **Mock Questions**: Generate and answer mock exam questions.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/amiKaushik/ExamPrepAI_v1.git
   cd ExamPrepAI
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**
   Create a `.streamlit/secrets.toml` file and add your key:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   ```

## Usage

Start the Streamlit app:
```bash
streamlit run app.py
```

Navigate through the sidebar to access different tools:
- Question Answering
- Study Notes
- Text Summarization
- Study Plan
- Mock Questions
- PDF Analysis

## Folder Structure

- `app.py` – Main entry point.
- `pages/` – Individual Streamlit pages.
- `utils/` – Backend logic and OpenAI interaction.
- `.streamlit/` – Config files for Streamlit.

## License

MIT License. See `LICENSE` for more details.

## Disclaimer

This tool is intended to assist in studying. Always verify the accuracy of generated content.
