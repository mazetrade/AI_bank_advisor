"""Streamlit chat interface for the AI bank advisor (demonstration project)."""

import logging
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.assistant import AssistantReply, BankAssistant

load_dotenv()

EXAMPLES = [
    "Combien coûte la tenue de compte par mois ?",
    "J'ai combien de temps pour contester une opération que je n'ai pas faite ?",
    "Je peux encore utiliser Facilidom pour changer de banque ?",
    "How much does the Reflets option cost?",
    "On m'a volé ma carte, je fais quoi ?",
]

CUSTOM_CSS = """
<style>
.app-header {
    background: linear-gradient(135deg, #0B5D45 0%, #13866A 100%);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 0.8rem;
}
.app-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.18);
    color: #FFFFFF;
    border-radius: 999px;
    padding: 0.15rem 0.7rem;
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
}
.app-title {
    color: #FFFFFF;
    font-size: 1.7rem;
    font-weight: 700;
}
.app-subtitle {
    color: #DCEFE7;
    font-size: 0.95rem;
    margin-top: 0.3rem;
}
[data-testid="stSidebar"] {
    background-color: #EEF6F2;
}
.stButton > button {
    width: 100%;
    background-color: #FFFFFF;
    color: #0B5D45;
    border: 1px solid #13866A;
    border-radius: 10px;
}
.stButton > button:hover {
    background-color: #13866A;
    color: #FFFFFF;
    border-color: #13866A;
}
</style>
"""

HEADER = """
<div class="app-header">
    <span class="app-badge">PROJET DE DÉMONSTRATION</span>
    <div class="app-title">Assistant bancaire IA</div>
    <div class="app-subtitle">Vos questions sur les frais, les cartes et les démarches, avec les sources officielles.</div>
</div>
"""

st.set_page_config(page_title="Assistant bancaire IA", page_icon="🏦")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


@st.cache_resource(show_spinner="Chargement de l'assistant...")
def get_assistant() -> BankAssistant:
    return BankAssistant()


def format_sources(reply: AssistantReply) -> list[str]:
    return [
        f"[{number}] {doc.metadata['title']} ({doc.metadata['version']}), p. {doc.metadata['page']}"
        for number, doc in reply.cited_sources
    ]


def show_message(message: dict) -> None:
    with st.chat_message(message["role"]):
        if message.get("category") == "emergency":
            st.error(message["content"])
        elif message.get("category") == "crisis":
            st.info(message["content"])
        else:
            st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.markdown(f"- {source}")


st.markdown(HEADER, unsafe_allow_html=True)
st.caption(
    "Projet de démonstration, non affilié à BNP Paribas. Vous échangez avec une IA dont les réponses "
    "s'appuient sur les documents publics de la banque (tarifs au 1er janvier 2026, conditions "
    "générales d'avril 2026). Ne partagez aucune donnée personnelle."
)

with st.sidebar:
    st.header("À propos")
    st.markdown(
        "Cet assistant répond à partir de trois documents publics : la brochure tarifaire, "
        "la convention de compte et le contrat carte. Il cite ses sources, refuse le conseil "
        "personnalisé, et oriente vers les bons canaux en cas d'urgence ou de réclamation."
    )
    st.header("Exemples")
    for example in EXAMPLES:
        if st.button(example):
            st.session_state.pending_question = example

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    show_message(message)

question = st.chat_input("Posez votre question sur les tarifs, les cartes ou les démarches...")
if question is None:
    question = st.session_state.pop("pending_question", None)

if question:
    user_message = {"role": "user", "content": question}
    st.session_state.messages.append(user_message)
    show_message(user_message)

    with st.spinner("Je cherche dans les documents..."):
        try:
            reply = get_assistant().reply(question)
            assistant_message = {
                "role": "assistant",
                "content": reply.text,
                "category": reply.category,
                "sources": format_sources(reply),
            }
        except Exception:
            logging.exception("Error while answering a question")
            assistant_message = {
                "role": "assistant",
                "content": "Désolé, une erreur technique est survenue. Réessayez dans un instant.",
            }

    st.session_state.messages.append(assistant_message)
    show_message(assistant_message)