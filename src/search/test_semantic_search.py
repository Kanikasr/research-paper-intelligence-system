from ingestion.pdf_loader import load_pdf_text
from ingestion.section_parser import split_into_sections
from ingestion.metadata_extractor import build_research_paper
from indexing.chunking import chunk_paper
from search.semantic_search import SemanticSearchEngine


if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"

    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)
    paper = build_research_paper(pdf_path, raw_text, sections)

    chunks = chunk_paper(paper.paper_id, paper.sections)

    search_engine = SemanticSearchEngine()
    search_engine.index_chunks(chunks)

    results = search_engine.search("attention mechanism in transformers")

    print("\nTop semantic search results:\n")
    for res in results:
        print(f"Paper: {res['paper_id']} | Section: {res['section']}")
        print(res["text"][:200])
        print("-" * 60)
