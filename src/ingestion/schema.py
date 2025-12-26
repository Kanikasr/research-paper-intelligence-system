from pydantic import BaseModel
from typing import Dict, List, Optional


class ResearchPaper(BaseModel):
    paper_id: str
    title: str
    authors: List[str] = []
    abstract: str
    sections: Dict[str, str]
    year: Optional[int]
    venue: Optional[str] = None
    keywords: List[str] = []
    references: List[str] = []
