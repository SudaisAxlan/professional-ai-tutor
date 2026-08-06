from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from src.prompts.system_prompt import create_tutor_prompt
from src.llm.llm import local_llm


def create_rag_chain(retriever):
    prompt = create_tutor_prompt()
    llm = local_llm()
    output_parser = StrOutputParser()

    # Document chain
    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt,
        output_parser=output_parser      # ← Added here
    )

    # Full RAG chain
    rag_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=document_chain
    )

    return rag_chain




