import sys
import os

# Ajouter le dossier 'project' au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_utils import get_connection, create_chunks_table

# Exemple rapide de test
conn = get_connection()
create_chunks_table(conn)
print("Table chunks_embeddings créée avec succès")
conn.close()
