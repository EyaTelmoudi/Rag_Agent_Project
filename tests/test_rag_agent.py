import sys
import os

# Ajouter le dossier 'project' au path pour que Python trouve rag_agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Imports
from rag_agent.rag_agent import RAGAgent
from rag_agent.retriever import Retriever
from rag_agent.llm import LLM
from db.db_utils import get_connection
from groq import Groq  # Ton client Groq

# 1️⃣ Créer une connexion à la base
conn = get_connection()

# 2️⃣ Instancier le Retriever avec la connexion
retriever = Retriever(conn)

# 3️⃣ Créer un client Groq
client = Groq(api_key="***REMOVED***")  # ou via variable d'environnement GROQ_API_KEY

# 4️⃣ Instancier ton LLM
llm = LLM(client)

# 5️⃣ Créer le RAGAgent
agent = RAGAgent(retriever, llm)

# 6️⃣ Question à tester
question = "Quels sont les symptômes du cancer du poumon ?"

# 7️⃣ Obtenir la réponse
result = agent.answer(question, top_k=3)

# 8️⃣ Afficher le résultat
print("Résultat du RAGAgent :")
print(result)

# 9️⃣ Fermer la connexion à la base
conn.close()
