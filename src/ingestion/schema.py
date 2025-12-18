from typing import List, Dict, Optional
from pydantic import BaseModel


class PaperSection(BaseModel):
    section_name: str
    content: str


class Citation(BaseModel):
    cited_title: str
    cited_authors: Optional[List[str]] = None
    cited_year: Optional[int] = None


class ResearchPaper(BaseModel):
    paper_id: str
    title: str
    authors: List[str]
    abstract: str
    sections: Dict[str, str]
    year: Optional[int]
    venue: Optional[str]
    keywords: Optional[List[str]] = []
    references: Optional[List[Citation]] = []
