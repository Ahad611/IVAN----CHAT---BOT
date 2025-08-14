# ping.py
import time
from telegram import Update
from telegram.ext import ContextTypes

async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responds with the bot's ping time."""
    start_time = time.time()
    msg = await update.message.reply_text("🏓 Pinging...")
    end_time = time.time()
    ping_ms = int((end_time - start_time) * 1000)
    await msg.edit_text(f"🏓 Pong!\n⚡ {ping_ms} ms")
￼Enter
