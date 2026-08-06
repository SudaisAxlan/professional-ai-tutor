from src.rag.embedding import get_embedding_model
from src.memory.conversion_memory import load_memeory_vector_db
from langchain_classic.memory import VectorStoreRetrieverMemory
def get_memory():
    """
    Create and return the Memory system (using simple retriever)
    """

    # 1. Get embedding
    embedding =get_embedding_model()

    # 2. Load Memory Vector Database
    memory_db = load_memeory_vector_db(embedding)

    # 3. Create SIMPLE retriever (Important!)
    memory_retriever = memory_db.as_retriever(
        search_kwargs={"k": 3}
    )

    # 4. Create Memory
    memory = VectorStoreRetrieverMemory(
        retriever=memory_retriever,
        memory_key="history",
        input_key="input",
        return_docs=False
    )

    return memory