
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder



def get_advanced_retriever(db, k=6):

    # 1. Normal Vector Retriever
    base_retriever = db.as_retriever(
        search_kwargs={
            "k": k
        }
    )


    # 2. Load Cross Encoder Reranker Model
    reranker_model = HuggingFaceCrossEncoder(
        model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"
    )


    # 3. Create Compressor
    compressor = CrossEncoderReranker(
        model=reranker_model,
        top_n=4
    )


    # 4. Combine Retriever + Reranker
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=base_retriever
    )


    return compression_retriever


