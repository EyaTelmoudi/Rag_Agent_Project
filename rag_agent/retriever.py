from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class Retriever:
    def __init__(self, conn):
        self.conn = conn

    def retrieve(self, query, top_k=5):
        embedding = embedding_model.encode([query])[0].tolist()
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT doc_name, chunk_text
                FROM chunks_embeddings
                ORDER BY embedding <-> %s::vector
                LIMIT %s
            """, (embedding, top_k))
            rows = cur.fetchall()
        return [{"doc_name": r[0], "text": r[1]} for r in rows]
