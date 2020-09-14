from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


def checkLanguage (message):
    b = TextBlob(message)
    lang = b.detect_language()
    return lang
    

def translate (message):
    if checkLanguage == ('en'):
        en_blob = TextBlob(message)
        en_blob=en_blob.translate(from_lang='es',to='en')


def messageSentiment(message):
    checkLanguage(message)
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(message)
    return sentiment