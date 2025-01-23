import requests

API_KEY = "YOUR_API_KEY"
URL = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

def fetch_news():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data["articles"]  # List of news articles
    return []

news_articles = fetch_news()
print(news_articles)