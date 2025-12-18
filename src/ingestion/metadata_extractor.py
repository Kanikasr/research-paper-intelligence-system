import re
from pathlib import Path
from typing import List, Optional

from ingestion.schema import ResearchPaper


def extract_title(raw_text: str) -> str:
    """
    Extract title from the first non-empty line of the paper.
    """
    for line in raw_text.split("\n"):
        line = line.strip()
        if line:
            return line
    return "Unknown Title"


def extract_authors(raw_text: str) -> List[str]:
    """
    Heuristic author extraction:
    Assumes authors appear between title and 'Abstract'.
    """
    lines = raw_text.split("\n")
    authors = []

    for line in lines[1:15]:  # scan only early part
        line = line.strip()
        if not line:
            continue
        if "abstract" in line.lower():
            break
        if "@" not in line and len(line.split()) <= 6:
            authors.append(line)

    return authors


def extract_year(raw_text: str) -> Optional[int]:
    """
    Extract publication year using regex.
    """
    match = re.search(r"(19|20)\d{2}", raw_text)
    if match:
        return int(match.group())
    return None


def build_research_paper(
    pdf_path: str,
    raw_text: str,
    sections: dict
) -> ResearchPaper:
    """
    Build a ResearchPaper object from extracted components.
    """
    paper_id = Path(pdf_path).stem

    title = extract_title(raw_text)
    authors = extract_authors(raw_text)
    year = extract_year(raw_text)

    abstract = sections.get("abstract", "")

    return ResearchPaper(
        paper_id=paper_id,
        title=title,
        authors=authors,
        abstract=abstract,
        sections=sections,
        year=year,
        venue=None,
        keywords=[],
        references=[]
    )
