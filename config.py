from pathlib import Path

# ===========================
# LLM
# ===========================

OLLAMA_MODEL = "llama3.2:latest"

# ===========================
# Embedding Model
# ===========================

EMBEDDING_MODEL = "BAAI/bge-m3"

# ===========================
# Vector Database
# ===========================

QDRANT_COLLECTION = "knowledge_base"

# ===========================
# Storage
# ===========================

DATA_PATH = Path("data")

PDF_PATH = DATA_PATH / "pdf"

MEMORY_DB = "memory.db"