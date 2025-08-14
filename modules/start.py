# start.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from helper import get_user_info

# Change these to your details
OWNER_ID = 123456789  # Your Telegram numeric ID
DEVELOPER_USERNAME = "YourUsername"  # Without @

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    user_info = get_user_info(update)

    keyboard = [
        [InlineKeyboardButton("📜 Help", callback_data="help")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [
            InlineKeyboardButton("👑 Owner", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton("💻 Developer", url=f"https://t.me/{DEVELOPER_USERNAME}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=f"👋 Hello {update.effective_user.first_name}!\n\n"
             "I'm your AI-powered Telegram chatbot.\n"
             "Ask me anything and I'll try to help.\n\n"
             f"Your info: {user_info}",
        reply_markup=reply_markup
    )
