import os

# Telegram credentials
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Allowed users (optional, comma-separated Telegram user IDs)
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "")
if ALLOWED_USERS:
    try:
        ALLOWED_USERS = [int(u.strip()) for u in ALLOWED_USERS.split(",") if u.strip()]
    except ValueError:
        ALLOWED_USERS = []
else:
    ALLOWED_USERS = []
