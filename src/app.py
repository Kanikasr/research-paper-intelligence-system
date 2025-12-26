import streamlit as st
import json
from pathlib import Path

from src.search.semantic_search import SemanticSearchEngine
from src.rag.rag_qa import RAGPipeline


ARTIFACT_DIR = Path("data/artifacts")


# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Research Paper Intelligence System",
    layout="wide"
)

st.title("📄 Research Paper Intelligence System")

st.write("""
This AI-powered research assistant allows users to:
- Perform semantic search over research papers
- Ask questions using Retrieval-Augmented Generation (RAG)
- View citations and research trends
""")


# -------------------------
# Load backend
# -------------------------
search_engine = SemanticSearchEngine()
rag = RAGPipeline()


# -------------------------
# Question input
# -------------------------
st.subheader("🔍 Ask a question")

question = st.text_input(
    "Enter your research question:",
    placeholder="What problem does the Transformer model solve?"
)

if question:
    results = search_engine.search(question, top_k=3)

    if not results:
        st.warning("No relevant sections found.")
    else:
        context = "\n\n".join(r["text"] for r in results)
        answer = rag.generate(context, question)

        st.subheader("🤖 Answer")
        st.write(answer)

        # -------------------------
        # Retrieved context (KEEP THIS)
        # -------------------------
        with st.expander("📚 Retrieved Context"):
            for r in results:
                st.markdown(f"**{r['paper_id']} — {r['section']}**")
                st.write(r["text"])


# -------------------------
# Citations
# -------------------------
st.subheader("📖 Citations")

citations_path = ARTIFACT_DIR / "citations.json"
if citations_path.exists():
    with open(citations_path) as f:
        citations = json.load(f)

    if citations:
        for paper_id, refs in citations.items():
            st.markdown(f"**{paper_id}**")
            if refs:
                for r in refs:
                    st.write("-", r)
            else:
                st.write("No citations found.")
    else:
        st.write("No citation data available.")
else:
    st.write("No citations extracted yet.")


# -------------------------
# Research trends
# -------------------------
st.subheader("📈 Research Trends (Keyword Frequency by Year)")

trends_path = ARTIFACT_DIR / "trends.json"
if trends_path.exists():
    with open(trends_path) as f:
        trends = json.load(f)

    if trends:
        for year, keywords in trends.items():
            st.markdown(f"**{year}**")
            for k, c in keywords:
                st.write(f"- {k} ({c})")
    else:
        st.write("No trend data available.")
else:
    st.write("No trend data available.")
