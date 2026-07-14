from __future__ import annotations

class AgentSelector:

    AGENTS={
        "research":"ResearchAgent",
        "drafting":"DraftingAgent",
        "reasoning":"ReasoningAgent",
        "evidence":"EvidenceAgent",
        "ocr":"OCRAgent",
        "general":"GeneralAgent",
    }

    def select(self,task:str)->str:
        return self.AGENTS.get(task,"GeneralAgent")
