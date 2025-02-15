# Google AI Text Generation Chatbot

This project is a simple chatbot application built using Streamlit and Google Generative AI (Gemini-Pro) to generate text-based responses.

## Features
- Uses Google Generative AI API for text generation.
- Interactive chat interface with Streamlit.
- Maintains conversation history within the session.

## Prerequisites
Before running the script, ensure you have the following:
- Python installed (>=3.7 recommended)
- A valid Google Generative AI API key
- Required Python packages installed

## Installation

1. Clone the repository or create a new Python script `chatBot.py` and paste the provided code.

2. Install the required dependencies using pip:
   ```sh
   pip install streamlit google-generativeai
   ```

3. Replace the `api` variable with your valid Google AI API key in `chatBot.py`:
   ```python
   api = 'YOUR_GOOGLE_AI_API_KEY'
   ```

## Usage

Run the Streamlit app using the following command:
```sh
streamlit run chatBot.py
```

### How It Works
- Enter text in the input field and submit.
- The chatbot will generate a response using the Google Generative AI model.
- The conversation history is maintained throughout the session.

## Notes
- Ensure your API key is valid and has the required permissions.
- This application requires an internet connection to access the Google AI API.

## License
This project is for educational and personal use only.

---

Feel free to modify and enhance the project as per your requirements!

