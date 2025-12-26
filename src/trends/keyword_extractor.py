import re
from collections import Counter

STOPWORDS = {
    "this", "that", "with", "from", "using", "have",
    "which", "their", "into", "between", "based"
}

def extract_keywords(text: str, top_k: int = 10):
    """
    Simple keyword extraction using word frequency.
    """
    if not text:
        return []

    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    words = [w for w in words if w not in STOPWORDS]

    counts = Counter(words)
    return counts.most_common(top_k)
