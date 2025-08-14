# Ivan x AI Chatbot 🤖

A modular Telegram chatbot powered by OpenAI's GPT models and `python-telegram-bot`.

## Features
- AI replies (`/start` or just type)
- Inline mode (@YourBot in any chat)
- Usage stats (`/stats`)
- Eval for devs (`/eval <expr>` for IDs in `ALLOWED_USERS`)
- Chat info (`/chatinfo`)
- Inline buttons

## Quick Deploy (Heroku)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)]([https://www.herokucdn.com/deploy/button.svg](https://github.com/Ahad611/IVAN----CHAT---BOT))

### Env Vars
- `API_ID` — from https://my.telegram.org
- `API_HASH` — from https://my.telegram.org
- `BOT_TOKEN` — from @BotFather
- `OPENAI_API_KEY` — from https://platform.openai.com
- `ALLOWED_USERS` — optional, comma-separated user IDs

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export API_ID=12345 API_HASH=abcd BOT_TOKEN=123:abc OPENAI_API_KEY=sk-xxxx
python start.py
```

## Notes
- This repo pins `openai==0.28.1` to use `ChatCompletion` for simplicity.
- For newer OpenAI SDKs, migrate to the `client.chat.completions.create` API.
