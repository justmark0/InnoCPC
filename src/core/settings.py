from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.getenv("DEBUG").lower() == 'true'
