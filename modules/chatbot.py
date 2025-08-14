import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, InlineQueryHandler, filters
import config
from chatbot import get_ai_reply
from helper import get_user_info
from stats import log_message, get_stats
from callback import button_handler
from inlinie import inline_query
from chats import chat_info

logging.basicConfig(level=logging.INFO)

async def start_command(update, context):
    await update.message.reply_text("🌺 Welcome! Type a message and I'll reply with AI.")

async def stats_command(update, context):
    await update.message.reply_text(f"📊 Stats: {get_stats()}")

async def chat_with_ai(update, context):
    log_message(update.message.from_user.id)
    reply = get_ai_reply(update.message.text)
    await update.message.reply_text(reply)

def start_bot():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("chatinfo", chat_info))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(InlineQueryHandler(inline_query))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_ai))

    app.run_polling()
￼Enter
