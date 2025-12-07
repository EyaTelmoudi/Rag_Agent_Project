import psycopg2

def get_connection(dbname="RagAgent", user="postgres", password="aya", host="localhost", port=5432):
    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

def create_chunks_table(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS chunks_embeddings (
        id SERIAL PRIMARY KEY,
        doc_name TEXT,
        chunk_text TEXT,
        embedding VECTOR(384)
    );
    """)
    conn.commit()
    cur.close()
