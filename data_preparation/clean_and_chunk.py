import os
import re
import json
import pdfplumber
import tiktoken

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^A-Za-z0-9À-ÿ.,;:!?()’'\- ]+", "", text)
    return text.strip()

def clean_pdfs(raw_folder="raw_docs", clean_folder="../data/cleaned_docs"):
    os.makedirs(clean_folder, exist_ok=True)
    pdf_files = [f for f in os.listdir(raw_folder) if f.lower().endswith(".pdf")]
    for pdf_file in pdf_files:
        full_path = os.path.join(raw_folder, pdf_file)
        try:
            with pdfplumber.open(full_path) as pdf:
                full_text = "".join(page.extract_text() or "" for page in pdf.pages)
        except Exception as e:
            print(f"Erreur fichier {pdf_file}: {e}")
            continue
        cleaned = clean_text(full_text)
        out_path = os.path.join(clean_folder, os.path.splitext(pdf_file)[0] + "_clean.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"[OK] {pdf_file} nettoyé -> {out_path}")

def chunk_texts(clean_folder="../data/cleaned_docs", chunk_folder="../data/chunks", chunk_size=300, overlap=50):
    os.makedirs(chunk_folder, exist_ok=True)
    tokenizer = tiktoken.encoding_for_model("text-embedding-3-large")
    for filename in os.listdir(clean_folder):
        if not filename.endswith(".txt"):
            continue
        with open(os.path.join(clean_folder, filename), "r", encoding="utf-8") as f:
            text = f.read()
        tokens = tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), chunk_size - overlap):
            chunk_text = tokenizer.decode(tokens[i:i + chunk_size])
            chunks.append({"doc": filename, "text": chunk_text})
        out_file = os.path.join(chunk_folder, filename.replace(".txt", "_chunks.json"))
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
        print(f"[OK] {filename} -> {len(chunks)} chunks")
