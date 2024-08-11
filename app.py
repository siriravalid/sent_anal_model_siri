import streamlit as st
from transformers import pipeline
try:
    sentiment_pipeline = pipeline('sentiment-analysis')
except ImportError as e:
    st.error(f"Import error: {e}")
    st.stop()
st.title("Sentiment Analysis(using model)-Siri")
text = st.text_area("Enter text for sentiment analysis")
if st.button("Analyze"):
    result = sentiment_pipeline(text)
    sentiment_label = result[0]['label']
    
    if sentiment_label == 'POSITIVE':
        sentiment = 'Positive'
    elif sentiment_label == 'NEGATIVE':
        sentiment = 'Negative'
    else:
        sentiment = 'Unknown'
    
    st.write(sentiment)
