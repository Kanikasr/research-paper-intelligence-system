import streamlit as st
import sys
from pathlib import Path

# =========================
# Ensure project root is on PYTHONPATH
# =========================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.ingestion.metadata_extractor import citation_graph, trend_analyzer
from src.search.semantic_search import SemanticSearchEngine
from src.rag.rag_qa import RAGPipeline


# =========================
# Streamlit Page Config
# =========================
st.set_page_config(
    page_title="Research Paper Intelligence System",
    layout="wide"
)

st.title("📄 Research Paper Management & Analysis Intelligence System")

st.write("""
This AI-powered research assistant allows users to:
- Perform semantic search over research papers
- Ask questions using Retrieval-Augmented Generation (RAG)
- View citations and research trends
""")


# =========================
# Initialize backend
# =========================
search_engine = SemanticSearchEngine()
rag = RAGPipeline()


# =========================
# Question Input
# =========================
st.subheader("🔍 Ask a question about the paper")

question = st.text_input(
    "Enter your research question:",
    placeholder="What problem does the Transformer model solve?"
)

if question:
    results = search_engine.search(question, top_k=3)

    if not results:
        st.warning("No relevant sections found for this question.")
    else:
        context_chunks = [r["text"] for r in results]

        answer = rag.generate_answer(context_chunks, question)

        # =========================
        # Display Answer
        # =========================
        st.subheader("🤖 RAG Answer")
        st.write(answer)

        # =========================
        # Show Retrieved Context
        # =========================
        st.subheader("📚 Retrieved Context")

        for i, r in enumerate(results, 1):
            with st.expander(f"Chunk {i} (Section: {r['section']})"):
                st.write(r["text"])


# =========================
# Citations Section
# =========================
st.subheader("📖 Citations")

# Demo-safe: show all known citations
all_citations = []
for paper_id in citation_graph.graph:
    all_citations.extend(citation_graph.get_citations(paper_id))

if all_citations:
    for c in sorted(set(all_citations)):
        st.write("-", c)
else:
    st.write("No citations extracted.")


# =========================
# Trend Analysis Section
# =========================
st.subheader("📈 Research Trends (Keyword Frequency by Year)")

trends = trend_analyzer.get_trends()

if trends:
    for year, keywords in trends.items():
        st.markdown(f"**{year}**")
        for k, count in keywords:
            st.write(f"- {k} ({count})")
else:
    st.write("No trend data available.")
