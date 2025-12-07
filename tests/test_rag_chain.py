import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_chain.rag_chain import create_rag_tools
from rag_agent.rag_agent import RAGAgent
from rag_agent.retriever import Retriever
from rag_agent.llm import LLM
from db.db_utils import get_connection
from groq import Groq

# Préparer les composants
conn = get_connection()
retriever = Retriever(conn)
client = Groq(api_key="***REMOVED***")
llm = LLM(client)
agent = RAGAgent(retriever, llm)

# Créer le run_agent avec l'agent injecté
run_agent = create_rag_tools(agent)

# Test
q = "Quels sont les symptômes du cancer du poumon ?"
print("Question :", q)
result = run_agent(q)
print("Résultat :", result)

conn.close()
