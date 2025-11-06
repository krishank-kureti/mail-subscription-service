# src/preferences.py
from flask import jsonify, request
from src.auth import app # Import the 'app' from auth.py
from src.database import db

@app.route('/api/preferences/topics', methods=['PUT'])
def update_topics():
    data = request.get_json()
    email = data.get('email')
    topics = data.get('topics')

    if not email or not topics:
        return jsonify({"error": "Email and topics list are required"}), 400
    if email not in db['users']:
        return jsonify({"error": "User not found"}), 404
        
    db['users'][email]['preferences']['topics'] = topics
    return jsonify({"status": "updated", "message": "Topic preferences saved"}), 200

@app.route('/api/preferences/sources', methods=['PUT'])
def update_sources():
    data = request.get_json()
    email = data.get('email')
    sources = data.get('sources')

    if not email or not sources:
        return jsonify({"error": "Email and sources list are required"}), 400
    if email not in db['users']:
        return jsonify({"error": "User not found"}), 404
        
    db['users'][email]['preferences']['sources'] = sources
    return jsonify({"status": "updated", "message": "Source preferences saved"}), 200