"""Embedding model used to index the chunks and to search them."""

from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer

MODEL_NAME = "intfloat/multilingual-e5-base"


class E5Embeddings(Embeddings):
    """LangChain wrapper around a multilingual E5 model, with its required prefixes."""

    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed document chunks."""
        vectors = self.model.encode(
            [f"passage: {text}" for text in texts],
            normalize_embeddings=True,
        )
        return vectors.tolist()

    def embed_query(self, text: str) -> list[float]:
        """Embed a user question."""
        vector = self.model.encode(f"query: {text}", normalize_embeddings=True)
        return vector.tolist()