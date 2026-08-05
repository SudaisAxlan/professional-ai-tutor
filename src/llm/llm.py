from langchain_ollama import ChatOllama

from config import (
    OLLAMA_MODEL,
    TEMPERATURE,
    TOP_P,
    TOP_K,
    NUM_PREDICT,
    REPEAT_PENALTY,
    SEED,
)


def local_llm():
    """
    Initialize and return the local Ollama LLM.
    """

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        top_k=TOP_K,
        num_predict=NUM_PREDICT,
        repeat_penalty=REPEAT_PENALTY,
        seed=SEED,
    )

    return llm