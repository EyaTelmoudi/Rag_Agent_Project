import sys
import os

# Ajouter le dossier 'project' au path pour que Python trouve rag_agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_agent.retriever import Retriever
from db.db_utils import get_connection  # Assure-toi d'avoir importé get_connection

# Créer une connexion à la base
conn = get_connection()

# Instancier le Retriever avec la connexion
r = Retriever(conn)
print("Importer et instancier Retriever OK")

# Exemple de test rapide
query = "symptômes du cancer du poumon"
results = r.retrieve(query, top_k=3)
for res in results:
    print(res)

# Fermer la connexion à la fin
conn.close()
