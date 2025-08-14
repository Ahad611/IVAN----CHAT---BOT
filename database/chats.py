from telegram import Update
from telegram.ext import ContextTypes

async def chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if not chat:
        return await update.message.reply_text("No chat info available.")
    title = chat.title or chat.username or "Private Chat"
    await update.message.reply_text(f"Chat: {title}\nChat ID: {chat.id}")
