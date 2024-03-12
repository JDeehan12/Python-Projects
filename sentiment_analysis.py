#The purpose of this script is develop a model that performs sentiment analysis on a dataset of product reviews.

import pandas as pd
from textblob import TextBlob
import spacy
import random

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Create function to preprocess the text data
def preprocess_text(text):
    # Remove stopwords and perform basic text cleaning
    doc = nlp(text)
    processed_text = ' '.join(token.text.lower().strip() for token in doc if not token.is_stop)
    return processed_text

# Create a function for sentiment analysis
def sentiment_analyses(review1, review2):
    # Process the input reviews
    processed_review1 = preprocess_text(review1)
    processed_review2 = preprocess_text(review2)

    # Analyze sentiment using TextBlob
    blob1 = TextBlob(processed_review1)
    blob2 = TextBlob(processed_review2)
    
    polarity1 = blob1.sentiment.polarity
    polarity2 = blob2.sentiment.polarity

    # Compare the polarity of the reviews
    if polarity1 > 0:
        sentiment1 = "Positive"
    elif polarity1 < 0:
        sentiment1 = "Negative"
    else:
        sentiment1 = "Neutral"

    if polarity2 > 0:
        sentiment2 = "Positive"
    elif polarity2 < 0:
        sentiment2 = "Negative"
    else:
        sentiment2 = "Neutral"

    # Analyze similarity
    doc1 = nlp(processed_review1)
    doc2 = nlp(processed_review2)
    similarity_score = doc1.similarity(doc2)

    # Print the reviews, their sentiment, and similarity
    print("Review 1:", review1)
    print("Sentiment of Review 1:", sentiment1)
    print("Review 2:", review2)
    print("Sentiment of Review 2:", sentiment2)
    print("Similarity Score:", similarity_score)
    print()

# Load the dataset
data = pd.read_csv("amazon_product_reviews.csv")

# Test the 'sentiment_analyses' function on sample product reviews
sample_review1 = "This product exceeded my expectations. Highly recommended!"
sample_review2 = "I am very disappointed with this product. Waste of money."
sentiment_analyses(sample_review1, sample_review2)


# Randomly select two reviews without using an index that is out of bounds 
random_indexes = random.sample(range(len(data)), 2)
review1 = data['reviews.text'][random_indexes[0]]  
review2 = data['reviews.text'][random_indexes[1]]  

# Test the 'sentiment_analyses' function on the randomly selected product reviews
sentiment_analyses(review1, review2)
