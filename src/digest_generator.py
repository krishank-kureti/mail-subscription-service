# src/digest_generator.py
# This is the main Digest Generator module.
# It uses the other stubs to perform its job.

from src.database import db
from src.news_api_mock import fetch_news
from src.templating_engine import format_digest_html

def generate_digest_for_user(email):
    """
    Main logic to generate a digest for a single user[cite: 97, 137].
    """
    print(f"Generator: Starting digest for {email}")
    
    # 1. Get user preferences from DB [cite: 66, 141]
    user = db['users'].get(email)
    if not user:
        return {"status": "error", "message": "User not found"}
        
    topics = user['preferences'].get('topics', [])
    sources = user['preferences'].get('sources', [])
    
    # 2. Fetch news from Mock API (US-006) [cite: 64, 143]
    news_items = fetch_news(topics, sources)
    
    # 3. Format news using Template Engine (US-007) [cite: 69, 146]
    html_content = format_digest_html(email, news_items)
    
    # 4. Log the job (for US-009 later) [cite: 68, 150]
    db['logs'].append({
        "timestamp": "2025-10-06T09:00:00Z", # Mock timestamp
        "user_email": email,
        "status": "success",
        "content_length": len(html_content)
    })
    
    return {"status": "success", "html": html_content}