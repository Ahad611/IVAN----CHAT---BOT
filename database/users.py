# users.py
import json
import os

USERS_FILE = "users.json"

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# Add or update a user
def add_user(user_id: int, name: str):
    users = load_users()
    users[str(user_id)] = {"name": name}
    save_users(users)

# Check if a user exists
def user_exists(user_id: int) -> bool:
    users = load_users()
    return str(user_id) in users

# Get all users
def get_all_users():
    return load_users()

# Remove a user
def remove_user(user_id: int):
    users = load_users()
    if str(user_id) in users:
        del users[str(user_id)]
        save_users(users)
￼Enter
