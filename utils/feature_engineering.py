from textblob import TextBlob
import pandas as pd
import numpy as np

def create_features(review, playtime):
    blob = TextBlob(review)
    
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    wc = len(review.split())
    playtime_log = np.log1p(playtime)
    
    # Scaler'ın eğitildiği tam 9 feature
    df = pd.DataFrame({
        'playtime_x_word_count': [playtime_log * wc],
        'playtime_x_sentiment_polarity': [playtime_log * polarity],
        'word_count_x_sentiment_polarity': [wc * polarity],
        'sentiment_ratio': [polarity / (subjectivity + 0.01)],
        'engagement_score': [(playtime_log + wc) / 2],
        'polarity_intensity': [polarity * subjectivity],
        'has_positive_sentiment': [int(polarity > 0.1)],
        'has_negative_sentiment': [int(polarity < -0.1)],
        'is_very_subjective': [int(subjectivity > 0.7)],
    })
    
    return df