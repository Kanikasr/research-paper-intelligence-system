from ingestion.pdf_loader import load_pdf_text
from ingestion.section_parser import split_into_sections
from ingestion.metadata_extractor import build_research_paper
from indexing.chunking import chunk_paper

if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"

    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)
    paper = build_research_paper(pdf_path, raw_text, sections)

    chunks = chunk_paper(paper.paper_id, paper.sections)

    print(f"Total chunks created: {len(chunks)}\n")
    print("Sample chunk:\n")
    print(chunks[0])
