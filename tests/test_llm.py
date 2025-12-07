import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_agent.llm import LLM
from groq import Groq

# Créer un client Groq
client = Groq(api_key="***REMOVED***")  # ou via variable d'env GROQ_API_KEY

llm = LLM(client)

fake_chunks = [
    {"doc_name": "test.txt", "text": "Le cancer du poumon peut provoquer toux et fatigue."},
    {"doc_name": "doc2.txt", "text": "Les patients peuvent également ressentir une perte de poids et des douleurs thoraciques."}
]

question = "Quels sont les symptômes du cancer du poumon ?"
answer = llm.generate(question, fake_chunks)

print("Réponse générée par LLM :")
print(answer)
