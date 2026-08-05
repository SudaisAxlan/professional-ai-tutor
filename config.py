from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project
# ==========================================================

PROJECT_NAME = "Professional AI Tutor"
PROJECT_VERSION = "0.1.0"

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Data Paths
# ==========================================================

DATA_PATH = BASE_DIR / "data"

PDF_PATH = DATA_PATH / "pdf"
BOOK_PATH = DATA_PATH / "books"
NOTES_PATH = DATA_PATH / "notes"

# ==========================================================
# Storage
# ==========================================================

STORAGE_PATH = BASE_DIR / "storage"

LOG_PATH = STORAGE_PATH / "logs"

MEMORY_DB_PATH = STORAGE_PATH / "memory.db"

# ==========================================================
# Local LLM (Ollama)
# ==========================================================

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:latest")

TEMPERATURE = 0

TOP_P = 0.9

TOP_K = 40

NUM_PREDICT = 1024

REPEAT_PENALTY = 1.1

SEED = 42

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-m3"
)

# ==========================================================
# Text Splitter (RAG)
# ==========================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# ==========================================================
# Retrieval
# ==========================================================

TOP_K_DOCUMENTS = 5

SEARCH_TYPE = "similarity"

# Available:
# similarity
# mmr

# ==========================================================
# Qdrant Cloud
# ==========================================================

QDRANT_URL = os.getenv("QDRANT_URL")

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

QDRANT_COLLECTION = os.getenv(
    "QDRANT_COLLECTION",
    "knowledge_base"
)


# ==========================================================
# Memory
# ==========================================================

MAX_CHAT_HISTORY = 10

MEMORY_TABLE = "conversation_memory"

# ==========================================================
# Languages
# ==========================================================

SUPPORTED_LANGUAGES = [
    "English",
    "Urdu",
    "Spanish",
    "Arabic",
]

DEFAULT_LANGUAGE = "English"

# ==========================================================
# Student Levels
# ==========================================================

SUPPORTED_LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced",
]

DEFAULT_LEVEL = "Beginner"