"""Build the vector index of the chunks, and load it for searching."""

import shutil

from langchain_chroma import Chroma

from src.chunker import chunk_documents
from src.embeddings import E5Embeddings
from src.loader import PROJECT_ROOT, load_all_documents

VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"
COLLECTION_NAME = "bank_documents"


def build_index() -> Chroma:
    """Load, chunk and embed all the documents, then store them on disk."""
    if VECTORSTORE_DIR.exists():
        shutil.rmtree(VECTORSTORE_DIR)
    chunks = chunk_documents(load_all_documents())
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=E5Embeddings(),
        persist_directory=str(VECTORSTORE_DIR),
    )
    vectorstore.add_documents(chunks)
    return vectorstore


def load_index() -> Chroma:
    """Open the index stored on disk, without recomputing any embedding."""
    if not VECTORSTORE_DIR.exists():
        raise FileNotFoundError(
            f"No index found in {VECTORSTORE_DIR}. Build it first with: python -m src.indexer"
        )
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=E5Embeddings(),
        persist_directory=str(VECTORSTORE_DIR),
    )


if __name__ == "__main__":
    store = build_index()
    print("Chunks indexed:", len(store.get()["ids"]))