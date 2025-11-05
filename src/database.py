# src/database.py


db = {
    "users": {
        "admin@example.com": {
            "id": 1,
            "password": "mock_hashed_password", # This is just a placeholder
            "preferences": {
                "topics": ["Technology", "Sports"],
                "sources": ["Mock News API"]
            }
        }
    },
    "logs": [
        {"timestamp": "2025-10-04T09:00:00Z", "status": "success", "job": "digest_run"}
    ]
}