import openai
import config
from helper import format_ai_reply

# Using legacy openai client for simplicity/predictability on Heroku
openai.api_key = config.OPENAI_API_KEY

def get_ai_reply(prompt: str) -> str:
    if not config.OPENAI_API_KEY:
        return "⚠️ OPENAI_API_KEY is not set."
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return format_ai_reply(resp.choices[0].message.content)
    except Exception as e:
        return f"⚠️ AI Error: {e}"
