import azure.functions as func
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from azure_storage import save_to_azure

def main(mytimer: func.TimerRequest) -> None:
    news_articles = fetch_news()
    for article in news_articles:
        title = article["title"]
        sentiment = analyze_sentiment(title)
        save_to_azure(title, sentiment)