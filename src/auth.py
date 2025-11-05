# src/auth.py
from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
import jwt  # <-- PERSON 2 ADDS THIS
import datetime # <-- PERSON 2 ADDS THIS

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
    
@app.route('/api/login', methods=['POST'])
def login():
    # 1. Get data from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # 2. Find the user in the mock DB
    user = db['users'].get(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # 3. Check the password hash (CRITICAL rubric item)
    if bcrypt.check_password_hash(user['password'], password):
        # 4. Generate JWT token
        token = jwt.encode({
            'user_id': user['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({"status": "success", "token": token}), 200

    # 5. If password check fails
    return jsonify({"error": "Invalid credentials"}), 401
#