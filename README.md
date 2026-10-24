# CodeAlpha FAQ Chatbot (NLP)

A beginner-friendly desktop FAQ chatbot built with Python, Tkinter, and scikit-learn. It cleans text, converts FAQ questions into TF-IDF vectors, and uses cosine similarity to select a likely answer.

## Features
- Chat-style graphical interface
- FAQ question and answer dataset included in `app.py`
- Text preprocessing using lowercase conversion and punctuation removal
- TF-IDF vectorization with unigrams and bigrams
- Cosine similarity to match the user's question
- Fallback message for questions without a close match
- Enter key and Send button support

## Requirements
- Python 3.10 or newer recommended
- pip
- Internet access only to install scikit-learn; the chatbot itself runs locally

## Run on Windows (PowerShell)
1. Open this folder in VS Code.
2. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```
3. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt and run `.venv\\Scripts\\activate.bat`, or run `.venv\\Scripts\\python.exe -m pip install -r requirements.txt` without activation.
4. Install the dependency:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```powershell
   python app.py
   ```

## Test questions
- How do I reset my password?
- Where can I find my order status?
- How can I contact support?
- Tell me about dinosaurs on Mars (should trigger the fallback)

## How it works
1. `clean()` normalizes the user's question.
2. `TfidfVectorizer` converts FAQ questions into numerical vectors.
3. `cosine_similarity()` scores the question against each FAQ.
4. The highest-scoring answer is returned if it passes a similarity threshold.

## Limitations
This is a demonstration FAQ bot, not a generative AI model or a live customer-support system. Its answers are limited to the FAQ dataset and similarity matching can choose an imperfect match. Expand and test the dataset for your chosen topic.

## Internship submission checklist
- Run the app and test the listed questions.
- Add screenshots of your own running app.
- Update this README with your name and any changes you make.
- Push the source code to a GitHub repository named `CodeAlpha_FAQChatbot`.
- Do not commit virtual environments, secrets, or personal data.
