from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

DB_PATH = "vector_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

MODEL_NAME = "mistral-small-2506"