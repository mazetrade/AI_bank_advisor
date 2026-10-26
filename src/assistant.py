"""The bank assistant: guardrails first, then the RAG pipeline for factual questions."""

from dataclasses import dataclass, field

from langchain_core.documents import Document

from src.guardrails import Classifier
from src.messages import get_fixed_message
from src.rag import RagAssistant


@dataclass
class AssistantReply:
    """Everything the app needs to display one answer."""

    text: str
    category: str
    language: str
    cited_sources: list[tuple[int, Document]] = field(default_factory=list)
    sources: list[Document] = field(default_factory=list)


class BankAssistant:
    """Classifies each message, then answers it with a fixed message or the RAG pipeline."""

    def __init__(self) -> None:
        self.classifier = Classifier()
        self.rag = RagAssistant()

    def reply(self, message: str) -> AssistantReply:
        route = self.classifier.classify(message)
        if route.category != "question":
            return AssistantReply(
                text=get_fixed_message(route.category, route.language),
                category=route.category,
                language=route.language,
            )
        result = self.rag.answer(message, route.language)
        return AssistantReply(
            text=result.answer,
            category=route.category,
            language=route.language,
            cited_sources=result.cited_sources,
            sources=result.sources,
        )