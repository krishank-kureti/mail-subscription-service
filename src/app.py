# src/app.py
from src.auth import app

if _name_ == '_main_':
    app.run(debug=True, port=5000)