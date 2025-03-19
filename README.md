# News Analyzer and Summarizer

News Analyzer and Summarizer is an intelligent web platform that provides AI-powered summarization, sentiment analysis, and keyword extraction for news articles. Users can input news URLs or raw text to quickly grasp the essence of any article.

## Features
- **AI News Summarization**: Condenses lengthy news articles into concise summaries.
- **Sentiment Analysis**: Identifies the tone of news content (positive, negative, neutral).
- **Keyword Extraction**: Highlights important keywords from the article.
- **URL and Text Input**: Analyze news from web links or directly pasted content.
- **User-Friendly Interface**: Clean and intuitive design for seamless experience.

## Tech Stack
### Frontend:
- HTML, CSS, JavaScript

### Backend:
- Python (Flask)

### NLP & AI Integration:
- HuggingFace Transformers, SpaCy, NLTK
- BeautifulSoup (for web scraping)

## Installation
### Prerequisites
- Python 3.x
- pip

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/suhass204/News_Analyzer-and-Summarizer.git
   cd News_Analyzer-and-Summarizer
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```sh
   python app.py
   ```
5. Open `index.html` in a browser to access the frontend.

## Usage
1. Enter a news article URL or paste news text.
2. Click to receive a summarized version, sentiment analysis, and keywords.
3. Understand news content quickly and efficiently.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for improvements.

## Contact
For any inquiries, reach out at suhasgowda540@gmail.com
