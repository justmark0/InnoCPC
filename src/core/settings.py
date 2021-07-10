import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = (
    os.getenv("SECRET_KEY")
    or "79d4ad2337c95a602ca7aba62cdef8af0e4d8803cb903540b4ebe1f2e7abc109"
)

#  Develop
DEBUG = os.getenv("DEBUG").lower() == "true"

# Database settings
POSTGRES_DB = os.getenv("POSTGRES_DB") or "InnoCPC"
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") or "InnoCPC"
POSTGRES_USER = os.getenv("POSTGRES_USER") or "InnoCPC"
POSTGRES_HOST = os.getenv("POSTGRES_HOST") or "db"
DB_SETTINGS = {
    "provider": "postgres",
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "host": POSTGRES_HOST,
    "database": POSTGRES_DB,
}

#  Authentication settings
TOKEN_EXPIRES = os.getenv("TOKEN_EXPIRES") or 1  # In days
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
