from flask import Flask, request, jsonify
from fake_news_detection import detect_fake_news
from news_summarization import summarize_news
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detect_fake_news', methods=['POST'])
def detect_fake_news_api():
    data = request.json or {}  # Prevent NoneType error
    text = data.get("text", "")
    result = detect_fake_news(text)
    return jsonify({"result": result})

@app.route('/summarize_news', methods=['POST'])
def summarize_news_api():
    data = request.json or {}  # Prevent NoneType error
    text = data.get("text", "")
    summary = summarize_news(text)
    return jsonify({"summary": summary})

@app.route("/")
def home():
    return "Flask is running!"

if __name__ == "__main__":
    print("Starting Flask on port 5001...")  # Debugging print
    app.run(debug=True, port=5001)
