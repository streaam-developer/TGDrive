from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID = int(os.getenv("API_ID", "23149497"))  # Your Telegram API ID
API_HASH = os.getenv("API_HASH", "b5129d40ff05cec2432b97f1bf26e954")  # Your Telegram API Hash

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = os.getenv("BOT_TOKENS", "7190050666:AAGec7JH8eiUjwWNxFgS1Lsx79MC4nQ4u_4").strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip() != ""]

# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", "-1002229884306"))  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = int(
    os.getenv("DATABASE_BACKUP_MSG_ID", "4")
)  # Message ID for database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")  # Default to "admin" if not set

# Determine the maximum file size (in bytes) allowed for uploading to Telegram
# 1.98 GB if no premium sessions are provided, otherwise 3.98 GB
if len(STRING_SESSIONS) == 0:
    MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2 GB in bytes
else:
    MAX_FILE_SIZE = 3.98 * 1024 * 1024 * 1024  # 4 GB in bytes

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = int(
    os.getenv("DATABASE_BACKUP_TIME", 10)
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Domain to auto-ping and keep the website active
WEBSITE_URL = os.getenv("WEBSITE_URL", "https://cinemanearme.online/")


# For Using TG Drive's Bot Mode

# Main Bot Token for TG Drive's Bot Mode
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN", "6662816722:AAEz_HNUaoX9kZBl632Eq485_HnW8vhnZnQ")
if MAIN_BOT_TOKEN.strip() == "":
    MAIN_BOT_TOKEN = None

# List of Telegram User IDs who have admin access to the bot mode
TELEGRAM_ADMIN_IDS = os.getenv("TELEGRAM_ADMIN_IDS", "5764988016, 1833940312").strip(", ").split(",")
TELEGRAM_ADMIN_IDS = [int(id) for id in TELEGRAM_ADMIN_IDS if id.strip() != ""]
