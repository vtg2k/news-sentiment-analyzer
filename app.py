import streamlit as st
from azure.data.tables import TableServiceClient

AZURE_CONNECTION_STRING = "your_azure_connection_string"
TABLE_NAME = "NewsSentiment"

service_client = TableServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
table_client = service_client.get_table_client(TABLE_NAME)

def fetch_news_data():
    entities = table_client.list_entities()
    return [(e["Title"], e["Sentiment"]) for e in entities]

news_data = fetch_news_data()

st.title("News Sentiment Analysis")
st.write("Live sentiment analysis of news headlines.")

for title, sentiment in news_data:
    st.write(f"**{title}** - Sentiment Score: {sentiment}")