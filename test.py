from config import (
    BUILD_DATABASE,
    # PDF_FILE,
)

from src.rag.loader import load_douements
from src.rag.chunks import chunk_documents
from src.rag.embedding import get_embedding_model
from src.rag.vector_store import build_db, load_db
from src.rag.retriever import get_advanced_retriever
from src.rag.rag_chain import create_rag_chain

from src.memory.memory import get_memory


def main():

    print("=" * 70)
    print("Initializing AI Tutor...")
    print("=" * 70)

    # ======================================================
    # Load Embedding Model
    # ======================================================

    embedding = get_embedding_model()
    print("Embedding Model Loaded")

    # ======================================================
    # Build Database (Only First Time)
    # ======================================================

    if BUILD_DATABASE:

        documents = load_douements("data/Sudais_Azlan_Professional_Profile.pdf")
        print(f"Documents Loaded : {len(documents)}")

        chunks = chunk_documents(documents)
        print(f"Chunks Created : {len(chunks)}")

        build_db(
            chunks=chunks,
            embedding=embedding,
        )

        print("Knowledge Base Created")

    # ======================================================
    # Load Existing Database
    # ======================================================

    db = load_db(embedding)

    print("Knowledge Base Loaded")

    # ======================================================
    # Retriever
    # ======================================================

    retriever = get_advanced_retriever(db)

    print("Retriever Ready")

    # ======================================================
    # Memory
    # ======================================================

    memory = get_memory()

    print("Memory Ready")

    # ======================================================
    # RAG Chain
    # ======================================================

    rag_chain = create_rag_chain(
        retriever=retriever
    )

    print("RAG Chain Ready")

    print("\n" + "=" * 70)
    print("Professional AI Tutor")
    print("Type 'exit' to quit")
    print("=" * 70)

    # ======================================================
    # Chat Loop
    # ======================================================

    while True:

        question = input("\nYou : ").strip()

        if not question:
            continue

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye 👋")
            break

        # ==================================================
        # Load Memory
        # ==================================================

        history = memory.load_memory_variables(
            {
                "input": question
            }
        )

        # ==================================================
        # Retrieve Documents (Debug)
        # ==================================================

        docs = retriever.invoke(question)

        print("\n" + "=" * 80)
        print("Retrieved Documents")
        print("=" * 80)

        for i, doc in enumerate(docs, start=1):

            print(f"\nChunk {i}")
            print("-" * 60)
            print(doc.page_content[:500])

            print("\nMetadata")
            print(doc.metadata)

        print("=" * 80)

        # ==================================================
        # Generate Answer
        # ==================================================

        print("\nAI : ", end="", flush=True)

        answer = ""

        for chunk in rag_chain.stream(
            {
                "input": question,
                "history": history.get("history", ""),
                "student_level": "Beginner",
                "language": "English",
            }
        ):

            if isinstance(chunk, dict):
                text = chunk.get("answer", "")

            elif hasattr(chunk, "content"):
                text = chunk.content

            else:
                text = str(chunk)

            if text:
                print(text, end="", flush=True)
                answer += text

        print("\n")

        # ==================================================
        # Save Memory
        # ==================================================

        memory.save_context(
            {
                "input": question
            },
            {
                "output": answer
            }
        )

        print("-" * 80)


if __name__ == "__main__":
    main()







# from src.llm.llm import local_llm

# from src.rag.loader import load_douements
# from src.rag.chunks import chunk_documents
# from src.rag.embedding import get_embedding_model
# from src.rag.vector_store import build_db, load_db
# from src.rag.retriever import get_advanced_retriever
# from src.rag.rag_chain import create_rag_chain

# from src.memory.memory import get_memory

# def main():
#     documents = load_douements(
#         "data/Sudais_Azlan_Professional_Profile.pdf"
#     )
#     chunks = chunk_documents(documents)
#     # print(f"✅ Chunks Created : {len(chunks)}")
#     embedding = get_embedding_model()

#     # print("✅ Embedding Model Loaded")

#     # =====================================================
#     # 5. Build Knowledge Base (ONLY FIRST TIME)
#     # =====================================================

#     BUILD_DATABASE = False

#     if BUILD_DATABASE:

#         build_db(
#             chunks=chunks,
#             embedding=embedding,
#         )

#         print("✅ Vector Database Created")

#     # =====================================================
#     # 6. Load Existing Knowledge Base
#     # =====================================================

#     db = load_db(embedding)

#     print("✅ Vector Database Loaded")

#     # =====================================================
#     # 7. Retriever
#     # =====================================================

#     retriever = get_advanced_retriever(db)

#     print("✅ Retriever Ready")

#     # =====================================================
#     # 8. Memory
#     # =====================================================

#     memory = get_memory()

#     print("✅ Memory Ready")

#     # =====================================================
#     # 9. RAG Chain
#     # =====================================================

#     rag_chain = create_rag_chain(
#         retriever=retriever
#     )

#     print("✅ RAG Chain Ready")

#     print("\nProfessional AI Tutor Started")
#     print("Type 'exit' to stop.\n")

#     # =====================================================
#     # Chat Loop
#     # =====================================================

#     while True:

#         question = input("You: ").strip()

#         if not question:
#             continue

#         if question.lower() in ["exit", "quit"]:

#             print("\nGoodbye 👋")

#             break

#         # ---------------------------------------
#         # Load Previous Memory
#         # ---------------------------------------

#         history = memory.load_memory_variables(
#             {
#                 "input": question
#             }
#         )

#         # ---------------------------------------
#         # Generate Response (Streaming)
#         # ---------------------------------------

#         print("\nAI: ", end="", flush=True)
#         answer = ""
#         for chunk in rag_chain.stream(
#             {
#                 "input": question,
#                 "history": history.get("history",""),
#                 "student_level": "Beginner",
#                 "language": "English",
#             }
#         ):
#             if isinstance(chunk, dict):
#                 text = chunk.get(
#                     "answer",
#                     ""
#                 )

#             elif hasattr(chunk, "content"):
#                 text = chunk.content
#             else:
#                 text = str(chunk)
#             if text:
#                 print(
#                     text,
#                     end="",
#                     flush=True
#                 )
#                 answer += text
#         print("\n")
#         # ---------------------------------------
#         # Save Conversation
#         # ---------------------------------------
#         memory.save_context(
#             {
#                 "input": question
#             },
#             {
#                 "output": answer
#             }
#         )
#         print("-" * 70)


# if __name__ == "__main__":

#     main()

             
             
#         # -------- Load relevant memory --------












# # question = (
# #         "Who is Sudais Azlan?"
# #     )


# # response = rag_chain.invoke(
# #     {
# #         "input": "Who is sudais azlan",

# #         "student_level": "Beginner",

# #         "language": "English"
# #     }
# # )
# # print("\nANSWER:")
# # print(
# #         response["answer"]
# #     )


    