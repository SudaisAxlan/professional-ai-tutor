from config import EMBEDDING_MODEL
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Initialize the HuggingFace embedding model.
    """

    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    return embedding