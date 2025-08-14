# __main__.py
import logging
from bot import start_bot

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    logging.info("🚀 Starting Telegram AI Chatbot via __main__.py ...")
    start_bot()
Enter
