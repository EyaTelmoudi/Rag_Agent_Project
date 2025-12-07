# Projet RAG Médical

Ce projet est un **agent RAG** capable de répondre à des questions médicales sur le cancer du poumon en utilisant un corpus de documents vectorisés.  
Le projet est organisé pour être facilement installé et utilisé avec un environnement virtuel Python.

---

## 1️⃣ Structure du projet

project/
│
├─ data_preparation/
│ └─ clean_and_chunk.py # Nettoyage et chunking des documents
│
├─ db/
│ └─ db_utils.py # Connexion PostgreSQL et création table
│
├─ embeddings/
│ └─ generate_embeddings.py # Génération et insertion des embeddings
│
├─ rag_agent/
│ ├─ llm.py # Classe LLM
│ ├─ rag_agent.py # Classe RAGAgent
│ └─ retriever.py # Classe Retriever
│
├─ rag_chain/
│ └─ rag_chain.py # LangChain wrapper + tools + run_agent()
│
├─ tests/
│ └─ test_agent.py # Tests unitaires de l’agent
│
├─ data/
│ └─ raw_docs/ # Corpus original
│ └─ cleaned_docs/ # Textes nettoyés
│ └─ chunks/ # Chunks JSON
│
├─ RagAgent_dump.sql # Backup complet de la base PostgreSQL
├─ run_agent.py # Script pour lancer l’agent
├─ requirements.txt # Dépendances Python
└─ README.md

---

## 2️⃣ Installation

### a) Décompresser le projet

unzip project.zip
cd project

### b) Créer un environnement virtuel

python -m venv venv
venv\Scripts\activate

### c) Installer les dépendances

pip install -r requirements.txt

## 3️⃣ Configurer PostgreSQL

### 1. Créer la base de données :
createdb -U postgres RagAgent
### 2. Restaurer la base avec les chunks et embeddings :
psql -U postgres -d RagAgent -f RagAgent_dump.sql
### 4️. Générer les embeddings (optionnel car sa se trouve déja dans la base ) 
python -m embeddings.generate_embeddings

### 5️. Lancer l’agent RAG

python main.py


Exemple de question :
    Quels sont les symptômes du cancer du poumon ?

