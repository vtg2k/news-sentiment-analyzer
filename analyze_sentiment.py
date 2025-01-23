from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Score between -1 (negative) and 1 (positive)

# Example usage
print(analyze_sentiment("Stock market is crashing!"))