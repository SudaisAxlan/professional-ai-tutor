from langchain_community.document_loaders import PyPDFLoader

def load_douements(path:str):
    douc=PyPDFLoader(path)
    return douc.load()