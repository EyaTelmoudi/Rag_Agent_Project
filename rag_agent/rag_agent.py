class RAGAgent:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def answer(self, question, top_k=5):
        chunks = self.retriever.retrieve(question, top_k=top_k)
        answer = self.llm.generate(question, chunks)
        sources = [c["doc_name"] for c in chunks]
        return {"answer": answer, "sources": sources}
