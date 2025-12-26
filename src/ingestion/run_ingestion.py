from pathlib import Path

from ingestion.pdf_loader import load_pdf_text
from ingestion.section_parser import split_into_sections
from ingestion.metadata_extractor import (
    build_research_paper,
    citation_graph,
    trend_analyzer
)

DATA_DIR = Path("data/raw_papers")


def run_ingestion():
    print(">>> Starting ingestion pipeline <<<")

    pdf_files = list(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return []

    papers = []

    for pdf_path in pdf_files:
        print(f"\nProcessing: {pdf_path.name}")

        raw_text = load_pdf_text(str(pdf_path))
        sections = split_into_sections(raw_text)

        paper = build_research_paper(
            pdf_path=str(pdf_path),
            raw_text=raw_text,
            sections=sections
        )

        references_text = sections.get("references", "")
        citations = citation_graph.extract_and_add(
            paper.paper_id,
            references_text
        )

        if paper.year and paper.abstract:
            trend_analyzer.add_paper(
                year=paper.year,
                abstract=paper.abstract
            )

        papers.append(paper)

        print(f"Title: {paper.title}")
        print(f"Year: {paper.year}")
        print(f"Citations found: {len(citations)}")

    print("\n>>> Ingestion completed <<<")
    return papers


if __name__ == "__main__":
    run_ingestion()
