import re
from pathlib import Path
from typing import List, Optional

from .schema import ResearchPaper
from src.citation.citation_extractor import extract_citations

from ..citation.citation_graph import CitationGraph
from ..trends.keyword_extractor import extract_keywords
from ..trends.trend_analyzer import TrendAnalyzer


# =========================
# Global analyzers (OK for GA03)
# =========================
citation_graph = CitationGraph()
trend_analyzer = TrendAnalyzer()


# =========================
# Metadata extraction helpers
# =========================

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


# =========================
# Core builder
# =========================

def build_research_paper(
    pdf_path: str,
    raw_text: str,
    sections: dict
) -> ResearchPaper:
    """
    Build a ResearchPaper object and enrich it with:
    - citations (Part IV)
    - keywords & trends (Part V)
    """
    paper_id = Path(pdf_path).stem

    title = extract_title(raw_text)
    authors = extract_authors(raw_text)
    year = extract_year(raw_text)

    abstract = sections.get("abstract", "")

    # -------------------------
    # Part IV — Citation Tracking
    # -------------------------
    references_text = sections.get("references", "")
    citations = extract_citations(references_text)
    citation_graph.add_paper(paper_id, citations)

    # -------------------------
    # Part V — Trend Analysis
    # -------------------------
    keywords_with_scores = extract_keywords(abstract)
    trend_analyzer.add_paper(year, keywords_with_scores)

    # Store only keyword names in paper object
    keywords = [k for k, _ in keywords_with_scores]

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

