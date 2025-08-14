import os

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","22657083"))
API_HASH = getenv("API_HASH","d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "8195241636"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP","https://t.me/+G42j7plUt91mYmQx")
UPDATE_CHNL = getenv("UPDATE_CHNL","UPDATE_IN_BOTS")
OWNER_USERNAME = getenv("OWNER_USERNAME", None)

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")

# Random Start Images
IMG = [
     "https://telegra.ph/file/45e5da1eab8f5892981ca.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
