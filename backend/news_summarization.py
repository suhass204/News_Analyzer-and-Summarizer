import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

def summarize_news(text, num_sentences=2):
    sentences = sent_tokenize(text)

    # If text is too short, return it as is
    if len(sentences) <= num_sentences:
        return text  

    words = word_tokenize(text.lower())
    words = [word for word in words if word not in stopwords.words('english') and word not in string.punctuation]

    freq_dist = FreqDist(words)
    
    # Score sentences based on word frequency
    sentence_scores = {
        sent: sum(freq_dist[word.lower()] for word in word_tokenize(sent) if word.lower() in freq_dist) 
        for sent in sentences
    }

    # Select top-ranked sentences for summary
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summary_sentences)

