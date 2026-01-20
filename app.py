import streamlit as st
import pickle
import nltk
from utils import preprocess_text

# Download NLTK resources (runs once on cloud)
nltk.download('stopwords')
nltk.download('wordnet')

# Load model and vectorizer
try:
    with open('fake_news_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found. Please train and save the model first.")
    st.stop()

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
