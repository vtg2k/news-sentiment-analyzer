# News Sentiment Analyzer (Azure Function App)

This project demonstrates the development and deployment of an Azure Function App that analyzes the sentiment of news articles in real-time.

## Technologies Used:
- **Azure Functions** (for serverless execution)
- **Python** (for sentiment analysis logic)
- **NewsAPI** (for fetching news articles)
- **Azure Storage** (for app data storage)

## Features:
- Pulls real-time news data from NewsAPI.
- Analyzes the sentiment of each news article.
- Provides an HTTP API endpoint for sentiment analysis.

## Setup and Usage:

1. Clone this repository:
    ```bash
    git clone https://github.com/vtg2k/news-sentiment-analyzer.git
    cd news-sentiment-analyzer
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Deploy to Azure:
    - Follow the instructions in the `Azure` setup section.
    - Make sure to configure the **NewsAPI** key in the environment variables.

## Running Locally:
To run the function app locally for development purposes:
```bash
func start

4. Azure Deployment:
    - For Azure deployment, use:

    ```bash
    func azure functionapp publish YOUR_FUNCTION_APP_NAME
    ```

