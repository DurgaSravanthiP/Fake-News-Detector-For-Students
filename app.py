import streamlit as st
import pickle
import nltk
from utils import preprocess_text

# ---- Safe NLTK downloads for Streamlit Cloud ----
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# ---- Load model and vectorizer ----
try:
    with open('fake_news_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# ---- UI ----
st.title("Fake News Detection")
st.write("Enter news text to predict if it's fake or real.")

news_text = st.text_area(
    "News Text",
    height=200,
    placeholder="Paste the news article here..."
)

if st.button("Predict"):
    if news_text.strip():
        clean_text = preprocess_text(news_text)
        vectorized = tfidf.transform([clean_text])
        prediction = model.predict(vectorized)[0]

        result = "Real News" if prediction == 1 else "Fake News"
        st.success(f"Predicted: {result}")
    else:
        st.warning("Please enter some text.")
