from langchain_ollama import ChatOllama

from config import OLLAMA_MODEL


def local_llm():

    llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0,
    top_p=0.9,
    repeat_penalty=1.1,
)

    return llm