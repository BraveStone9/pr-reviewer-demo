API_KEY = "sk-live-abc123xyz"


def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    db.execute(query)
    return db.fetchone()
