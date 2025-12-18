from pdf_loader import load_pdf_text
from section_parser import split_into_sections
from metadata_extractor import build_research_paper

if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"

    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)

    paper = build_research_paper(
        pdf_path=pdf_path,
        raw_text=raw_text,
        sections=sections
    )

    print("\n--- RESEARCH PAPER OBJECT ---\n")
    print("Paper ID:", paper.paper_id)
    print("Title:", paper.title)
    print("Authors:", paper.authors)
    print("Year:", paper.year)
    print("Abstract (first 300 chars):\n", paper.abstract[:300])
    print("\nSections:", list(paper.sections.keys()))
