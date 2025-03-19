import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Load Datasets
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

# Add a label column: 1 for fake news, 0 for real news
fake_df["label"] = 1
true_df["label"] = 0

# Combine both datasets
df = pd.concat([fake_df, true_df], ignore_index=True)

# Use only the "title" field since frontend input is a title
df = df[['title', 'label']]

# Text Preprocessing
stop_words = set(stopwords.words('english'))
important_words = {"not", "fake", "true", "real"}  # Manually keeping key words

def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())  # Convert to lowercase and tokenize
    tokens = [word for word in tokens if word not in stop_words or word in important_words]
    tokens = [word for word in tokens if word not in string.punctuation]  # Remove punctuation
    return " ".join(tokens)

df['processed_text'] = df['title'].apply(preprocess_text)  # Use only titles

# Train Model
X_train, X_test, y_train, y_test = train_test_split(df['processed_text'], df['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Save Model & Vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Load Model & Vectorizer Once (for better performance)
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("model.pkl")

def detect_fake_news(text):
    text = preprocess_text(text)  # Preprocess title input
    text_vec = vectorizer.transform([text])  # Transform text
    prediction = model.predict(text_vec)[0]
    return "Fake News" if prediction == 1 else "Real News"
