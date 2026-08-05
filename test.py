from src.llm.llm import local_llm
from src.rag.loader import load_douements
# Checking all components

# 1)  LLM Check

# llm=local_llm()
# responce=llm.invoke("Who is imran khan : ")
# print(responce)

# 2 Load Data
doucments=load_douements("data/Sudais_Azlan_Professional_Profile.pdf")

print(len(doucments))
