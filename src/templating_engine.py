# src/templating_engine.py
# This is a stub for the Templating Engine.
# It formats raw news data into a simple HTML string.

def format_digest_html(user_email, news_items):
    """
    Generates a simple HTML string for the email digest[cite: 79, 146].
    """
    print(f"Templating: Formatting digest for {user_email}")
    
    # Start the HTML
    html = f"<h1>Your Daily News Digest, {user_email}!</h1>"
    
    if not news_items:
        html += "<p>No news items found for your preferences today.</p>"
        return html
        
    # Add each news item
    for item in news_items:
        html += "<div>"
        html += f"<h3>{item['headline']}</h3>"
        html += f"<p>{item['summary']}</p>"
        html += "</div>"
        
    return html