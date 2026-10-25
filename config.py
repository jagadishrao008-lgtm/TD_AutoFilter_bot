#========================================================================
# Don't Remove Credit Tg - @TDBotDev
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TDBotDev
# Ask Doubt on telegram https://t.me/TDBotDev
#========================================================================
import os
import random
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID", 35992347))
API_HASH = os.environ.get("API_HASH", "a3c7960f6fb6a8b4cd3cdd9f4b97371f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8791951760:AAFzdpbwlnLUNXuqcAeKGXya1TcKd8NSh6I")

# Search Settings
DB_CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", -1001813593588))
START_TEXT = os.environ.get("START_TEXT", "👋 Welcome to NittuMovies4K Auto Filter Bot!")
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", 10))

# Database Settings
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://jagadishrao008_db_user:0wRNyuQcYWkyH3VB@cluster0.ngv7r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "autofilterbot")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "files")

# Optional Settings
OWNER_ID = int(os.environ.get("OWNER_ID", 1688168923))
ADMIN_IDS = [int(x) for x in os.environ.get("ADMINS", "1688168923").split(",")]

# Force Subscribe Settings
FORCE_SUB_CHANNELS = [int(x) for x in os.environ.get("FORCE_SUB_CHANNELS", "-1001813593588").split(",")]
FORCE_SUB_TEXT = os.environ.get("FORCE_SUB_TEXT", "🚨 Please join our channel to use this bot!")

UPDATES = os.environ.get("UPDATES", "")
ADMINS = ADMIN_IDS + [OWNER_ID]

# Auto-Delete Settings
AUTO_DELETE_TIME = os.environ.get("AUTO_DELETE_TIME", "30")
DELETE_MESSAGE_TEXT = os.environ.get("DELETE_MESSAGE_TEXT", "⚠️ All messages will be deleted after 30 seconds!")

PICS = ["https://telegra.ph"]

def get_random_pic():
    return random.choice(PICS)

START_PIC = PICS
FORCE_PIC = PICS

BOT_COMMANDS = {
    "start": "🎯 Start the bot",
    "help": "❓ How to use the bot",
    "status": "📊 Bot statistics",
    "reset": "🔄 Total reset (only owner)"
}


#========================================================================
# Don't Remove Credit Tg - @TDBotDev
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TDBotDev
# Ask Doubt on telegram https://t.me/TDBotDev
#========================================================================
