from ingestion.pdf_loader import load_pdf_text
from ingestion.section_parser import split_into_sections
from ingestion.metadata_extractor import build_research_paper
from indexing.chunking import chunk_paper
from search.semantic_search import SemanticSearchEngine
from rag.rag_qa import RAGQuestionAnswering


if __name__ == "__main__":
    # ----------------------------
    # Step 1: Load and parse paper
    # ----------------------------
    pdf_path = "E:/projects/research_paper_intelligence/data/raw_papers/attention_is_all_you_need.pdf"

    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)
    paper = build_research_paper(pdf_path, raw_text, sections)

    # ----------------------------
    # Step 2: Chunk the paper
    # ----------------------------
    chunks = chunk_paper(paper.paper_id, paper.sections)

    # ----------------------------
    # Step 3: Build semantic index
    # ----------------------------
    search_engine = SemanticSearchEngine()
    search_engine.index_chunks(chunks)

    # ----------------------------
    # Step 4: Ask a question
    # ----------------------------
    question = "What problem does the Transformer model solve?"

    results = [
        r for r in search_engine.search(question, top_k=6)
        if r["section"] in ["abstract", "introduction"]
    ][:2]

    context_chunks = [res["text"] for res in results]

    # ----------------------------
    # Step 5: RAG Answering
    # ----------------------------
    rag = RAGQuestionAnswering()
    answer = rag.generate_answer(context_chunks, question)

    # ----------------------------
    # Step 6: Print Output
    # ----------------------------
    print("\n==============================")
    print("QUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer)
    print("==============================\n")
