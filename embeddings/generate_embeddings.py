import os
import json
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from db.db_utils import get_connection

model = SentenceTransformer('all-MiniLM-L6-v2')

def insert_embeddings(chunk_folder="../data/chunks"):
    conn = get_connection()
    cur = conn.cursor()
    for filename in os.listdir(chunk_folder):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(chunk_folder, filename), "r", encoding="utf-8") as f:
            chunks = json.load(f)
        for chunk in tqdm(chunks):
            text = chunk["text"]
            doc = chunk["doc"]
            embedding = model.encode(text).tolist()
            embedding_str = "ARRAY[{}]::vector".format(",".join(map(str, embedding)))
            cur.execute(
                f"INSERT INTO chunks_embeddings (doc_name, chunk_text, embedding) VALUES (%s, %s, {embedding_str})",
                (doc, text)
            )
    conn.commit()
    cur.close()
    conn.close()
