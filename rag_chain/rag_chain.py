from langchain.tools import tool

def create_rag_tools(agent):
    @tool
    def rag_tool(question: str) -> str:
        """Répond aux questions médicales en utilisant les documents médicaux via RAG."""
        return agent.answer(question)["answer"]

    # Simulation simple : PAS de @tool
    def friend_agent_simulation(query: str) -> str:
        """Simule l'utilisation de l'agent de ton ami pour les questions sur les réseaux de neurones."""
        return "⚡ Utilisation de l'agent de ton ami (simulation) ⚡"

    def run_agent(question: str) -> str:
        if "réseaux de neurones" in question.lower():
            return friend_agent_simulation(question)  # appel direct
        else:
            return rag_tool.run(question)  # utilisation LangChain pour RAG

    return run_agent
