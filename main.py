import sys
import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

# Ajouter le dossier project au path pour que Python trouve les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

# Import des modules RAG
from db.db_utils import get_connection
from rag_agent.retriever import Retriever
from rag_agent.llm import LLM
from rag_agent.rag_agent import RAGAgent
from rag_chain.rag_chain import create_rag_tools
from groq import Groq  # ou OpenAI si tu changes de client

def main():
    # 1️⃣ Vérifier la clé API
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("⚠️ La variable d'environnement GROQ_API_KEY n'est pas définie ! "
                         "Ajoute-la dans le fichier .env à la racine du projet.")
    
    # 2️⃣ Créer la connexion à la DB
    conn = get_connection()
    
    try:
        # 3️⃣ Instancier le Retriever
        retriever = Retriever(conn)
        
        # 4️⃣ Instancier le client Groq
        client = Groq(api_key=api_key)
        
        # 5️⃣ Instancier le LLM
        llm = LLM(client)
        
        # 6️⃣ Créer l'agent RAG
        agent = RAGAgent(retriever, llm)
        
        # 7️⃣ Créer run_agent qui gère RAG + friend_agent_simulation
        run_agent = create_rag_tools(agent)
        
        print("🟢 RAG Agent prêt à répondre à vos questions !")
        
        # 8️⃣ Boucle interactive
        while True:
            question = input("\nPosez votre question (ou 'exit' pour quitter) :\n> ")
            if question.lower() in ["exit", "quit"]:
                print("Fermeture de l'application...")
                break
            
            result = run_agent(question)
            print("\nRéponse :\n", result)
    
    finally:
        # Fermer proprement la connexion DB
        conn.close()
        print("Connexion à la base fermée.")

if __name__ == "__main__":
    main()
