"""Answer customer questions from the official documents: retrieval, then Claude."""

import re
from dataclasses import dataclass
from datetime import date

from langchain_anthropic import ChatAnthropic
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

from src.indexer import load_index

LLM_MODEL = "claude-haiku-5-5"
TOP_K = 5
LANGUAGE_NAMES = {"fr": "French", "en": "English"}

# Prompt v5, see the prompt log in notebooks/04_rag_chain.ipynb.
SYSTEM_PROMPT = """You are a virtual assistant answering questions from BNP Paribas individual customers in mainland France about fees, products and procedures.

Rules:
1. Base your answer ONLY on the passages below. Never use outside knowledge, even if you think you know the answer.
2. After each fact, cite the passage it comes from with its number in square brackets, like [1] or [2][3].
3. If the passages do not contain the answer, or only part of it, say so clearly and suggest contacting a BNP Paribas adviser. Never guess. Do not suggest an adviser when the passages fully answer the question.
4. Today's date is {today}. Some passages mention dates (end of a service, rules starting on a given date). Compare them with today's date, and never present a service as available if the passages say it has ended.
5. Answer in {answer_language}. Copy amounts, deadlines and phone numbers exactly as they are written in the passages.
6. Answer only the question that was asked. Include the conditions and exceptions that change the answer (for example, a different deadline in some cases), but do not add information about other topics, even related ones. If the answer is negative (a service has ended, an operation is not possible) and the passages mention an alternative for the same need, give it in one sentence. Keep the answer short: a few sentences are usually enough.
7. Keep the strength of the original wording. If the passages say the customer must do something, do not present it as advice, and do not present advice as an obligation.
8. Never recommend a product or a decision for the customer's personal situation (which card to choose, whether to borrow, save, invest or repay). If the question asks for a recommendation, give the relevant facts from the passages, then explain that a personal recommendation requires a BNP Paribas adviser, who can assess the customer's situation.

Passages:
{context}"""

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ]
)

CITATION = re.compile(r"\[(\d+)\]")


@dataclass
class RagAnswer:
    """The answer to a question, with the passages it was built from."""

    answer: str
    sources: list[Document]
    cited_sources: list[tuple[int, Document]]


def format_passages(docs: list[Document]) -> str:
    """Number the retrieved chunks so that Claude can cite them."""
    blocks = []
    for i, doc in enumerate(docs, start=1):
        blocks.append(f"[{i}] (page {doc.metadata['page']})\n{doc.page_content}")
    return "\n\n".join(blocks)


def find_cited_sources(answer: str, docs: list[Document]) -> list[tuple[int, Document]]:
    """Return the passages actually cited in the answer, with their numbers."""
    numbers = sorted({int(n) for n in CITATION.findall(answer)})
    return [(n, docs[n - 1]) for n in numbers if 1 <= n <= len(docs)]


class RagAssistant:
    """Retrieves the relevant passages and asks Claude to answer from them."""

    def __init__(self) -> None:
        self.retriever = load_index().as_retriever(search_kwargs={"k": TOP_K})
        self.chain = PROMPT | ChatAnthropic(model=LLM_MODEL)

    def answer(self, question: str, language: str = "fr") -> RagAnswer:
        docs = self.retriever.invoke(question)
        response = self.chain.invoke(
            {
                "question": question,
                "context": format_passages(docs),
                "today": date.today().isoformat(),
                "answer_language": LANGUAGE_NAMES[language],
            }
        )
        return RagAnswer(
            answer=response.text,
            sources=docs,
            cited_sources=find_cited_sources(response.text, docs),
        )