from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ContextTypes
from chatbot import get_ai_reply

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.inline_query
    if not q or not q.query:
        return
    ai_response = get_ai_reply(q.query)
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="AI Response",
            input_message_content=InputTextMessageContent(ai_response)
        )
    ]
    await q.answer(results, cache_time=0)
