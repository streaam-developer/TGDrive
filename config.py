from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID = int(os.getenv("API_ID", "23149497"))  # Your Telegram API ID
API_HASH = os.getenv("API_HASH", "b5129d40ff05cec2432b97f1bf26e954")  # Your Telegram API Hash

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = os.getenv("BOT_TOKENS", "7190050666:AAGec7JH8eiUjwWNxFgS1Lsx79MC4nQ4u_4, 7498558459:AAEh5A-CkY3UZPPeKOrm6u53Du0Ji6zdLrs, 6514010635:AAF7f1QjuCZ31UoscTHuH-Z1YB0PyYo-CbE, 6674251566:AAHeI6nuYP1hTK802beqIiOChpJLY03O2pE, 6342113383:AAHjIB0upZ0RTPvhRbiI14wKvska4rmI-Zg, 5857392333:AAHsMGonGgO_XB1NwDwOaMpVMg8hJGH_r1E, 5983400035:AAGQs1ITBxqc94YPoagIC5_dwfJz4LOcm7c, 6231686503:AAHX59LUx3xcL2x2M7dewmZxSv5SH7Wway0, 5822225258:AAHzJCvixTXkRIvnTaIwaF0SNcQtXTz8Keo, 5990499406:AAG4cRIY5S0jmOS-i6ydTh3i_ivi_OhSKfE, 6257817586:AAHiHfYz_Ykn_n1QHgE7o1aRdOn5Gxg6M4U, 6250661928:AAENOvRUaMe1ATG5drGbYQ3KhyfkV-C_1-M, 5676877386:AAHARA3jUG9nNTd7dt_mpKrz_z1Lb3vz0Tg, 5918078029:AAG9eW76xvyeUUX-RdUPRrts-svb4Yz3zNA, 5606869491:AAHJbj5U_fEbYmODiezZsqWP5lIWSJalQ6Y, 5580813031:AAHbEdD_g1MwYozWxEJdi3EIl5YwkMa1pvY, 7209848123:AAFpI7krTXBRE0HYAvR5LYGL6faryOQGzmo, 7294373055:AAHcDtNHfwuXiZqDQN_EvAxFEf_9DXWnH6M, 6936728011:AAEf1Thv1fFLv_yvXMqWYyEyO2Am2oHZjjQ, 7043988904:AAFwcP3zPqHmkyetGxZl3Kbqw-t5UJvLnIU, 7185552648:AAFt8UMY1O_oFhewPHGSxuIBCkc_02rFQ2M, 6956498960:AAFekL2rqkfLP_herOZdD3zHrs9wa7T2uH8, 6800223017:AAEsQnMM4hVCL95XbXyIN4q0_KsqQeBHW8o, 6133264799:AAGqGTZzecI-5fA-GLwH20SWkFfCdyxuGzY, 6609449380:AAGle29QwW3faG8wxXCGFDGVFEVoEfc-hyw, 6302756306:AAEdWTi86exWgTt8Y4hUYu6IEOqvOTUQ0Y8, 6405501523:AAGo0G4fs7oe673lZ76eNzeIh76ra9-_7gU").strip(", ").split(",")
#BOT_TOKENS = os.getenv("BOT_TOKENS", "").strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip() != ""]

# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "BQFhO7kAdghnsLeeqwCAoKxvF03AI33Zob-iZ3JJ6h_BPv6HASYaDyc1Y7fHFh4TDwo1rf9IpeqF3kLF9Xp19xKr0l5Uy2Omc4XQTssAcrinuVoiG2xH0-7tMzj2UNlZMVvEGEltUWz4z6G8CfhSwqx9LVsYGXavhYorDcvTUiNDmCbAOjOYiXLNSGU63EAYl2m1G8rUPMsVytvUv_QN3rwpOlRF9opuqIebVotC9lUVeomyK9sKqaCU1G6g64mK0HAiZq7Lb89JQhOXHb70RPQEcoRxOG6wEM2lTCUrQk-QQXTN9Sp7HRe2F9sXQBTg9qrLZEA-kJ7sb9-i4jjx5qzZJe70QAAAAAGJPQdCAA").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", "-1002229884306"))  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = int(
    os.getenv("DATABASE_BACKUP_MSG_ID", "549")
)  # Message ID for database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "frontech")  # Default to "admin" if not set

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
WEBSITE_URL = os.getenv("WEBSITE_URL", "https://streaamstore.shop/")


# For Using TG Drive's Bot Mode

# Main Bot Token for TG Drive's Bot Mode
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN", "6662816722:AAEz_HNUaoX9kZBl632Eq485_HnW8vhnZnQ")
if MAIN_BOT_TOKEN.strip() == "":
    MAIN_BOT_TOKEN = None

# List of Telegram User IDs who have admin access to the bot mode
TELEGRAM_ADMIN_IDS = os.getenv("TELEGRAM_ADMIN_IDS", "5764988016, 1833940312").strip(", ").split(",")
TELEGRAM_ADMIN_IDS = [int(id) for id in TELEGRAM_ADMIN_IDS if id.strip() != ""]
