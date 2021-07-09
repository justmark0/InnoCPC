import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
