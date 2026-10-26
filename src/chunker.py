"""Split the loaded pages into chunks ready to be embedded."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# Chunks shorter than this (mostly titles left alone) are merged with a neighbor.
MIN_CHUNK_CHARS = 100

# Fee brochure: lists of fees. In the pypdf output, section titles
# start with two spaces and items start with a bullet.
FEE_BROCHURE_SEPARATORS = ["\n\n", "\n  ", "\n•", "\n", " ", ""]

# Legal texts (account agreement, card contract). Line breaks come from the PDF
# layout and often fall mid-sentence, so after the document structure we cut
# at sentence ends.
LEGAL_TEXT_SEPARATORS = [
    r"\n(?=PARTIE |CHAPITRE |TITRE |[IVXL]+\s*[–-]\s)",  # parts and chapters: "CHAPITRE III –", "XI –"
    r"\n(?=\d+(?:\.\d+)*\.?\s+[A-ZÉ])",                 # numbered sections: "1. Les chèques", "11.2 Cette demande"
    r"\n(?= ?> )",                                      # rules introduced by ">"
    r"(?<=[.;])\s",                                     # end of a sentence or of a list item
    r"\s",                                              # any space or line break
    r"",                                                # anywhere, as a last resort
]

fee_brochure_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=FEE_BROCHURE_SEPARATORS,
)

legal_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=LEGAL_TEXT_SEPARATORS,
    is_separator_regex=True,
)

# Each document type is mapped to a splitting strategy. Several types can share one.
SPLITTERS = {
    "fee_brochure": fee_brochure_splitter,
    "account_agreement": legal_text_splitter,
    "card_contract": legal_text_splitter,
}


def merge_short_chunks(page_chunks: list[Document]) -> list[Document]:
    """Attach chunks too short to stand alone (mostly titles) to a neighbor on the same page.

    A short chunk is glued to the start of the next chunk, where a title belongs.
    If it is the last chunk of the page, it is glued to the end of the previous one.
    A page whose whole content is shorter than MIN_CHUNK_CHARS is dropped.
    """
    merged = []
    pending = ""
    for chunk in page_chunks:
        text = f"{pending}\n{chunk.page_content}" if pending else chunk.page_content
        if len(text) < MIN_CHUNK_CHARS:
            pending = text
        else:
            merged.append(Document(page_content=text, metadata=chunk.metadata))
            pending = ""
    if pending and merged:
        last = merged[-1]
        merged[-1] = Document(page_content=f"{last.page_content}\n{pending}", metadata=last.metadata)
    return merged


def add_context_header(chunk: Document) -> Document:
    """Return a copy of the chunk with its document title written at the top."""
    header = f"Document : {chunk.metadata['title']} ({chunk.metadata['version']})"
    return Document(
        page_content=f"{header}\n\n{chunk.page_content}",
        metadata=chunk.metadata,
    )


def chunk_documents(documents: list[Document]) -> list[Document]:
    """Split each page with the splitter of its type, merge short chunks, then add headers."""
    chunks = []
    for doc in documents:
        splitter = SPLITTERS[doc.metadata["doc_type"]]
        page_chunks = splitter.split_documents([doc])
        chunks.extend(merge_short_chunks(page_chunks))
    return [add_context_header(chunk) for chunk in chunks]