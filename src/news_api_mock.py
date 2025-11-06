# src/news_api_mock.py
# This is a mock stub for the external News API[cite: 28, 67].
# It returns fake data based on the requested topics.

def fetch_news(topics, sources):
    """
    Simulates fetching news from a mock API[cite: 64].
    """
    print(f"Mock API: Fetching news for topics: {topics}, sources: {sources}")
    
    mock_data = {
        "Technology": [
            {"headline": "Tech Headline 1", "summary": "Summary of tech 1..."},
            {"headline": "Tech Headline 2", "summary": "Summary of tech 2..."}
        ],
        "Sports": [
            {"headline": "Sports Headline 1", "summary": "Summary of sports 1..."},
            {"headline": "Sports Headline 2", "summary": "Summary of sports 2..."}
        ],
        "Politics": [
            {"headline": "Politics Headline 1", "summary": "Summary of politics 1..."}
        ]
    }
    
    # Build a list of news based on the user's topics
    news_items = []
    for topic in topics:
        if topic in mock_data:
            news_items.extend(mock_data[topic])
            
    return news_items