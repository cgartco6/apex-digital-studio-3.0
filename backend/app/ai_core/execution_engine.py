from .llm_router import LLMRouter
from .memory.vector_store import VectorStore

class ExecutionEngine:
    def __init__(self):
        self.llm = LLMRouter()
        self.memory = VectorStore()

    def execute(self, prompt: str, context_id: str):
        memory_hits = self.memory.search(prompt)
        response = self.llm.generate(prompt)
        self.memory.add(response, {"id": context_id})
        return response
