from ingestion.pdf_loader import load_pdf_text
from ingestion.section_parser import split_into_sections
from ingestion.metadata_extractor import build_research_paper
from indexing.chunking import chunk_paper
from search.semantic_search import SemanticSearchEngine
from rag.rag_qa import RAGQuestionAnswering


if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"

    # Build semantic index
    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)
    paper = build_research_paper(pdf_path, raw_text, sections)

    chunks = chunk_paper(paper.paper_id, paper.sections)

    search_engine = SemanticSearchEngine()
    search_engine.index_chunks(chunks)

    # Ask a question
    question = "What problem does the Transformer model solve?"

    results = search_engine.search(question, top_k=4)
    context_chunks = [res["text"] for res in results]

    # RAG Answer
    rag = RAGQuestionAnswering()
    answer = rag.generate_answer(context_chunks, question)

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer)
