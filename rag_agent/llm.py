# rag_agent/llm.py

from groq import Groq
import os

class LLM:
    def __init__(self, client: Groq):
        self.client = client

    def generate(self, question: str, chunks: list, model: str = "llama-3.3-70b-versatile"):
        """
        Génère une réponse à partir d'une question et d'un contexte (chunks)
        """
        # Construire le contexte
        context = "\n---\n".join([c["text"] for c in chunks])
        prompt = f"Question: {question}\nContext:\n{context}"

        # Envoyer la requête à Groq via l'API correcte
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.2
        )

        # Retourner le texte de la réponse
        return response.choices[0].message.content


if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY", "TON_CLE_API")
    client = Groq(api_key=api_key)
    llm = LLM(client)

    chunks = [
        {"text": "Le cancer du poumon se manifeste par une toux persistante et une fatigue."},
    ]
    question = "Quels sont les symptômes du cancer du poumon ?"

    answer = llm.generate(question, chunks)
    print("Réponse générée :")
    print(answer)
