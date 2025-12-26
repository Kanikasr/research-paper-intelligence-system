from pathlib import Path
import json
import numpy as np

from .pdf_loader import load_pdf_text
from .section_parser import split_into_sections
from .metadata_extractor import build_research_paper, citation_graph, trend_analyzer

from src.indexing.chunking import chunk_sections
from src.indexing.embeddings import embed_text
from src.indexing.faiss_store import FAISSStore

from src.citation.citation_extractor import extract_citations
from src.trends.keyword_extractor import extract_keywords


DATA_DIR = Path("data/raw_papers")
ARTIFACT_DIR = Path("data/artifacts")
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


def run_ingestion():
    print(">>> Starting ingestion pipeline <<<")

    pdf_files = list(DATA_DIR.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found.")
        return

    all_chunks = []

    for pdf_path in pdf_files:
        print(f"\nProcessing: {pdf_path.name}")

        raw_text = load_pdf_text(str(pdf_path))
        sections = split_into_sections(raw_text)

        paper = build_research_paper(
            pdf_path=str(pdf_path),
            raw_text=raw_text,
            sections=sections
        )

        # -------------------------
        # Chunking
        # -------------------------
        chunks = chunk_sections(
            sections=sections,
            paper_id=paper.paper_id
        )
        all_chunks.extend(chunks)

        # -------------------------
        # Citations
        # -------------------------
        references_text = sections.get("references", "")
        citations = extract_citations(references_text)
        citation_graph.add_paper(paper.paper_id, citations)

        # -------------------------
        # Trends
        # -------------------------
        if paper.year and paper.abstract:
            keywords = extract_keywords(paper.abstract)
            trend_analyzer.add_paper(paper.year, keywords)

        print(f"Title: {paper.title}")
        print(f"Year: {paper.year}")
        print(f"Chunks created: {len(chunks)}")
        print(f"Citations found: {len(citations)}")

    # -------------------------
    # Build FAISS index
    # -------------------------
    print("\nBuilding FAISS index...")

    texts = [chunk["text"] for chunk in all_chunks]
    embeddings = embed_text(texts)
    embeddings = np.array(embeddings).astype("float32")

    store = FAISSStore(dim=embeddings.shape[1])
    store.add(embeddings, all_chunks)
    store.save()

    # -------------------------
    # Persist artifacts (CRITICAL FIX)
    # -------------------------
    with open(ARTIFACT_DIR / "citations.json", "w") as f:
        json.dump(citation_graph.get_full_graph(), f, indent=2)

    with open(ARTIFACT_DIR / "trends.json", "w") as f:
        json.dump(trend_analyzer.get_trends(), f, indent=2)

    print(">>> Ingestion completed <<<")


if __name__ == "__main__":
    run_ingestion()
