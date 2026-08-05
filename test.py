from src.llm.llm import local_llm

llm=local_llm()
responce=llm.invoke("Who is imran khan : ")
print(responce)