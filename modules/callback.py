from telegram import Update
from telegram.ext import ContextTypes
from button import about_buttons

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query:
        return
    await query.answer()
    data = (query.data or "").lower()
    if data == "chat":
        await query.edit_message_text("📝 Send me a message and I’ll reply with AI.")
    elif data == "about":
        await query.edit_message_text(
            "🤖 AI Chatbot\nBuilt with GPT and python-telegram-bot.",
            reply_markup=about_buttons()
        )
