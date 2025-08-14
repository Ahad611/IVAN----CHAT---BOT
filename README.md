# 🤖 Ivan x AI Chatbot

A simple Telegram AI chatbot built with [python-telegram-bot](https://python-telegram-bot.org) and [OpenAI GPT](https://openai.com).

## ✨ Features
- AI-powered chat with OpenAI GPT
- Inline buttons for quick actions
- User logging (stores all users who interact)
- `/ping` command to check latency
- `/help` and `/start` commands
- Easy to deploy to Heroku

---

## 🚀 Deploy to Heroku
Click the button below to deploy instantly:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Ahad611/IVAN----CHAT---BOT)

---

## 🔧 Environment Variables
You’ll need the following environment variables in Heroku or your `.env` file:

| Variable           | Description |
|--------------------|-------------|
| `BOT_TOKEN`        | Telegram Bot API Token from [BotFather](https://t.me/BotFather) |
| `OPENAI_API_KEY`   | Your OpenAI API Key from [OpenAI](https://platform.openai.com) |

---

## 🖥 Local Development
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
cd YOUR_REPO_NAME
pip install -r requirements.txt
python main.py
