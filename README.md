# 📰 Fake News Detection Project

An AI-powered Fake News Detection system that analyzes news articles and predicts whether the given news is **Real** or **Fake** using Machine Learning and Natural Language Processing.

---

## 📌 Problem Statement

Misinformation spreads very quickly through online news platforms and social media. Students often find it difficult to differentiate between reliable and fake information.  
There is a need for an AI-based system that can analyze news content and help users identify fake news in a simple and effective way.

---

## ✨ Features

- 🧠 **Text Analysis** using Natural Language Processing (NLP)
- 📊 **Machine Learning Model** using Logistic Regression and TF-IDF
- 🌐 **Web Interface** built with Streamlit
- ⚡ **Real-time Prediction** of Fake or Real news
- ✅ Easy to use and student-friendly interface

---

## 🚀 Live Deployment

🔗 **Live Application Link:**  
👉 https://fake-news-detector-for-students-01.streamlit.app

Users can access the application online, enter news text, and instantly check whether it is fake or real.

---

## 🗂️ Project Structure


```
Fake-News-Detector-For-Students/
├── app.py # Streamlit application
├── fake_news_model.pkl # Trained ML model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── utils.py # Text preprocessing utilities
├── train_model.ipynb # Model training notebook
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

### Training the Model

Run the Jupyter notebook `Analysis_Model.ipynb` to train the model and save it.

Or run the training script directly:

```bash
python model.py
```

### Running the Prediction App

Run the Streamlit app:

```bash
streamlit run app.py
```

Enter news text and get predictions on whether it's fake or real.

## How It Works

1. **Data Preprocessing**: Text is cleaned, tokenized, and lemmatized
2. **Feature Extraction**: TF-IDF vectorization converts text to numerical features
3. **Model Training**: Logistic Regression classifier learns patterns in fake vs real news
4. **Prediction**: New articles are processed and classified with confidence scores

## Model Performance

The model achieves approximately 98% accuracy on the test dataset, with strong performance in distinguishing between fake and real news articles.

## 🛠️ Technologies Used

- **🐍Python**: Core programming language
- **Pandas & 📊NumPy**: Data manipulation
- **📦Scikit-learn**: Machine learning algorithms
- **🧾NLTK**: Natural language processing
- **🌐Streamlit**: Web application framework
- **Matplotlib & Seaborn**: Data visualization
- **☁️Streamlit Community Cloud**:  Deployment

## 🔮 Future Improvements

- Add more advanced NLP techniques (BERT, transformers)
- Include source credibility analysis
- Add fact-checking integration
- Implement multi-language support
- Add article summarization features

## Disclaimer

This tool provides an estimation based on machine learning patterns and should not be used as the sole source of truth. Always verify information from multiple reliable sources.
