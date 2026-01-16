# Fake News Detection Project

An AI-powered fake news detection system that analyzes news articles to determine their credibility.

## Problem Statement

Misinformation spreads quickly through online news and social media, making it hard for students to differentiate between reliable and fake information. There is a need for an AI solution that can analyze articles, assess credibility, and provide concise, trustworthy summaries to prevent the spread of false information.

## Features

- **Text Analysis**: Analyzes news article content using natural language processing
- **Machine Learning Model**: Uses Logistic Regression with TF-IDF vectorization
- **Web Interface**: Clean Streamlit app for easy interaction
- **Real-time Prediction**: Instant results with confidence scores

## Project Structure

```
fake-news-detection/
├── fake_news_dataset.csv  # Combined dataset with labels
├── Analysis_Model.ipynb   # Jupyter notebook for analysis and training
├── fake_news_detection.py # Streamlit app for prediction
├── utils.py               # Text preprocessing utilities
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

Run the Jupyter notebook `Analysis_Model.ipynb` to train the model and save it.

Or run the training script directly:

```bash
python model.py
```

### Running the Prediction App

Run the Streamlit app:

```bash
streamlit run fake_news_detection.py
```

Enter news text and get predictions on whether it's fake or real.

## How It Works

1. **Data Preprocessing**: Text is cleaned, tokenized, and lemmatized
2. **Feature Extraction**: TF-IDF vectorization converts text to numerical features
3. **Model Training**: Logistic Regression classifier learns patterns in fake vs real news
4. **Prediction**: New articles are processed and classified with confidence scores

## Model Performance

The model achieves approximately 98% accuracy on the test dataset, with strong performance in distinguishing between fake and real news articles.

## Technologies Used

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Machine learning algorithms
- **NLTK**: Natural language processing
- **Streamlit**: Web application framework
- **Matplotlib & Seaborn**: Data visualization

## Future Improvements

- Add more advanced NLP techniques (BERT, transformers)
- Include source credibility analysis
- Add fact-checking integration
- Implement multi-language support
- Add article summarization features

## Disclaimer

This tool provides an estimation based on machine learning patterns and should not be used as the sole source of truth. Always verify information from multiple reliable sources.
