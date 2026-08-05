from src.llm.llm import local_llm
from src.rag.loader import load_douements
from src.rag.chunks import chunk_documents
from src.rag.embedding import get_embedding_model
from src.rag.vector_store import build_db, load_db
from src.rag.retriever import get_advanced_retriever

# from src.rag import load_db,build_db,get_embedding_model,chunk_documents,load_douements


# =====================================================
# 1. LLM Test
# =====================================================

# llm = local_llm()
# response = llm.invoke("What is Artificial Intelligence?")
# print(response.content)


# =====================================================
# 2. Loader Test
# =====================================================

documents = load_douements(
    "data/Sudais_Azlan_Professional_Profile.pdf"
)

print(f"Documents Loaded : {len(documents)}")


# =====================================================
# 3. Chunk Test
# =====================================================

chunks = chunk_documents(documents)

print(f"Chunks Created : {len(chunks)}")


# =====================================================
# 4. Embedding Test
# =====================================================

embedding = get_embedding_model()

print("Embedding Model Loaded Successfully")


# =====================================================
# 5. Build Qdrant Database
# =====================================================

db = build_db(chunks, embedding)

print("Vector Database Created Successfully")


# =====================================================
# 6. Load Existing Database
# =====================================================

db = load_db(embedding)

print("Vector Database Loaded Successfully")

retriever=get_advanced_retriever(db=db)
question="Who is sudais azlan ?"
# responce=retiver.invoke(question)



docs = retriever.invoke(question)

print(f"\nRetrieved Chunks : {len(docs)}\n")

for index, doc in enumerate(docs, start=1):

    print("=" * 80)
    print(f"Chunk {index}")
    print("=" * 80)

    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)

    print()
# /rested_douemnents=get_advanced_retriever(db=db)


