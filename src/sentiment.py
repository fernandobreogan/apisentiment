from nltk.sentiment.vader import SentimentIntensityAnalyzer

def messageSentiment(message):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(message)
    return sentiment