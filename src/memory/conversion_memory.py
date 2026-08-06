from langchain_community.vectorstores import Chroma

def create_memory_vectorstore(embeding):
    """
    Create and return the Memory Vector Database.
    """

    memory_db = Chroma(
        collection_name="chat_memory",
        embedding_function=embeding,
        persist_directory="chat_memory",
    )

    return memory_db


def load_memeory_vector_db(embedding):
    db = Chroma(
        persist_directory="chat_memory",
        embedding_function=embedding
    )

    return db