"""Load the official bank documents as LangChain Documents."""

import re
from pathlib import Path

from langchain_core.documents import Document
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"

# Official title, version and type of each document. Title and version are shown in the citations.
DOCUMENT_INFO = {
    "tarifs_particuliers_2026.pdf": {
        "title": "Conditions et tarifs - Particuliers",
        "version": "Tarifs au 1er janvier 2026",
        "doc_type": "fee_brochure",
    },
    "conditions_generales_bienvenue_2026.pdf": {
        "title": "Conditions générales de la convention de compte Bienvenue",
        "version": "Édition avril 2026",
        "doc_type": "account_agreement",
    },
    "conditions_fonctionnement_cartes_2026.pdf": {
        "title": "Conditions de fonctionnement des cartes (Contrat carte)",
        "version": "Édition avril 2026",
        "doc_type": "card_contract",
    },
}

# Pages with no useful information, identified in notebooks/01_load_documents.ipynb.
PAGES_TO_SKIP = {
    ("tarifs_particuliers_2026.pdf", 1),  # cover page
    ("conditions_generales_bienvenue_2026.pdf", 1),  # table of contents only
    ("conditions_generales_bienvenue_2026.pdf", 19),  # blank "NOTES" page
}

# Layout noise identified in notebooks/02_chunking.ipynb.
PAGE_NUMBER_LINE = re.compile(r"\A\s*\d{1,2}\s*\n")  # page number on the first line
DOCUMENT_CODE_LINE = re.compile(r"^SMONCAROSCGPDF\d+\s*\n", flags=re.MULTILINE)  # card contract's internal reference


def clean_page_text(text: str) -> str:
    """Remove layout noise that carries no information."""
    text = PAGE_NUMBER_LINE.sub("", text)
    text = DOCUMENT_CODE_LINE.sub("", text)
    return text


def load_pdf(path: Path) -> list[Document]:
    """Load one PDF as a list of Documents, one per page."""
    info = DOCUMENT_INFO[path.name]
    reader = PdfReader(path)
    documents = []
    for page_number, page in enumerate(reader.pages, start=1):
        if (path.name, page_number) in PAGES_TO_SKIP:
            continue
        documents.append(
            Document(
                page_content=clean_page_text(page.extract_text()),
                metadata={"source": path.name, "page": page_number, **info},
            )
        )
    return documents


def load_all_documents(raw_dir: Path = RAW_DIR) -> list[Document]:
    """Load every PDF in the raw data folder."""
    documents = []
    for path in sorted(raw_dir.glob("*.pdf")):
        documents.extend(load_pdf(path))
    return documents