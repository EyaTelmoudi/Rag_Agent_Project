from db.db_utils import get_connection
from rag_agent.retriever import Retriever
from rag_agent.llm import LLM
from rag_agent.rag_agent import RAGAgent

API_KEY = "***REMOVED***"  # ta clé OpenAI

if __name__ == "__main__":
    conn = get_connection()
    retriever = Retriever(conn)
    llm = LLM(API_KEY)
    agent = RAGAgent(retriever, llm)

    questions = [
        "Quels sont les symptômes du cancer du poumon ?",
        "Qu'est-ce qu'un scanner thoracique ?",
        "Quels sont les traitements du diabète de type 2 ?"
    ]

    for q in questions:
        result = agent.answer(q)
        print("Question:", q)
        print("Réponse:", result["answer"])
        print("Sources:", result["sources"])
        print("-"*50)

    conn.close()
