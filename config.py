#========================================================================
# Nittu Movies Custom Config
#========================================================================
import os
import random
from dotenv import load_dotenv

load_dotenv()

# నీ సొంత టెలిగ్రామ్ API వివరాలు (డైరెక్ట్ సెట్ చేయబడ్డాయి)
API_ID = int("35992347")
API_HASH = "a3c7960f6fb6a8b4cd3cdd9f4b93737f"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8791951760:AAHCTPRz1lfzZILE0Uhye7rHQphxKnZ1urQ")

# నీ సినిమా ఫైల్స్ స్టోర్ అయ్యే ఛానెల్ ID (-1001813593588)
DB_CHANNEL_ID = -1001813593588

START_TEXT = os.environ.get("START_TEXT", "🚀 **Welcome to Nittu Movies**\n\n🎬 Movies • Series • Anime — All in One Place\n⚡ Lightning Fast Search with Smart Auto Filters\n\n🔍 Just send any movie name to start exploring!")
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", 10))

# Help and About Texts
HELP_TEXT = os.environ.get("HELP_TEXT", "📖 **Help Menu**\n\n1. Send any movie or series name to search.\n2. Click on the file name to receive it instantly.")
ABOUT_TEXT = os.environ.get("ABOUT_TEXT", "❄️ **About Nittu Movies**\n\nThis is a high-speed file search bot for Nittu Movies users.")

# MongoDB సెట్టింగ్స్
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://jagadishrao008_db_user:OwRNyuQsYWxyH3VB@cluster0.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = "NittuMovieDB"
COLLECTION_NAME = "files"

# ఓనర్ మరియు అడ్మిన్ ఐడీలు
OWNER_ID = 0
ADMINS = []

# ఫోర్స్ సబ్స్క్రైబ్ ఛానెల్స్
FORCE_SUB_CHANNELS = []
ADMIN_IDS = ADMINS + [OWNER_ID] if OWNER_ID else ADMINS
FORCE_SUB_TEXT = os.environ.get("FORCE_SUB_TEXT", "📥 **దయచేసి మా ఛానెల్‌లో జాయిన్ అవ్వండి!**")

UPDATES = ""

AUTO_DELETE_TIME = "0" # 0 అంటే ఆటో-డిలీట్ ఉండదు
DELETE_MESSAGE_TEXT = "⚠️ <b><u>IMPORTANT:</u></b>\n\n<i>Messages will be deleted after {time}.</i>"

PICS = [
    "https://ibb.co/39zW3dNh",
    "https://ibb.co/v4FX9rMN"
]

def get_random_pic():
    return random.choice(PICS)

START_PIC = PICS[0]
FORCE_PIC = PICS[1]

BOT_COMMANDS = [
    ("start", "🚀 Start the bot"),
    ("help", "🆘 How to use"),
    ("delete_file", "🗑️ Delete files (admin)"),
    ("broadcast", "⚡ Broadcast (admin)"),
    ("status", "👀 Statistics (admin)")
]


