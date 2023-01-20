import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze(text):
    sentiment_analyzer=SentimentIntensityAnalyzer()
    sentiment=sentiment_analyzer.polarity_scores(text)

    if sentiment['compound']>0.05:
        return 'positive'
    elif sentiment['compound']< -0.05:
        return 'negative'
    else:
        return 'neutral'

text="Hi I'm a bad boy"
print(analyze(text))