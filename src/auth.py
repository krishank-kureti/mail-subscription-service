# src/auth.py
from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt

# This 'app' instance will be used by our main file
app = Flask(_name_)
bcrypt = Bcrypt(app)

# Import the mock database (Person 4 is creating this)
from src.database import db

# Secret key for JWT (Person 2 will use this)
app.config['SECRET_KEY'] = 'your-super-secret-key' 

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if email in db['users']:
        return jsonify({"error": "User already exists"}), 409 # [cite: 1557]

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') # [cite: 1514]
    
    # Store the new user
    user_id = len(db['users']) + 1
    db['users'][email] = {
        "id": user_id,
        "password": hashed_password,
        "preferences": {}
    }

    print(f"User DB updated: {db['users']}") # For debugging
    return jsonify({
        "status": "success",
        "userId": user_id
    }), 201 # 201 = Created