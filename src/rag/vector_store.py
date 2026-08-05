from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION

def build_db(chunks, embedding):
    db = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embedding,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=QDRANT_COLLECTION,
    )
    print("✅ Qdrant Vector Database Created Successfully!")
    return db

def load_db(embedding):
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
    db = QdrantVectorStore(
        client=client,
        collection_name=QDRANT_COLLECTION,
        embedding=embedding,
    )
    print("✅ Qdrant Vector Database Loaded Successfully!")
    return db

















# from langchain_qdrant import QdrantVectorStore
# from qdrant_client import QdrantClient

# from config import (
#     QDRANT_URL,
#     QDRANT_API_KEY,
#     QDRANT_COLLECTION,
# )



# def build_db(chunks, embedding):

#     client = QdrantClient(
#         url=QDRANT_URL,
#         api_key=QDRANT_API_KEY,
#     )

#     db = QdrantVectorStore.from_documents(
#         documents=chunks,
#         embedding=embedding,
#         client=client,
#         collection_name=QDRANT_COLLECTION,
#     )

#     print("✅ Qdrant Vector Database Created Successfully!")

#     return db

# def load_db(embedding):

#     client = QdrantClient(
#         url=QDRANT_URL,
#         api_key=QDRANT_API_KEY,
#     )

#     db = QdrantVectorStore(
#         client=client,
#         collection_name=QDRANT_COLLECTION,
#         embedding=embedding,
#     )

#     print("✅ Qdrant Vector Database Loaded Successfully!")

#     return db


