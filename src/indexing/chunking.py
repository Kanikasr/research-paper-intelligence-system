from typing import Dict, List


def chunk_sections(
    sections: Dict[str, str],
    paper_id: str,
    max_words: int = 200
) -> List[dict]:
    """
    Split section text into smaller chunks (by word count).

    Returns a list of dicts with:
    - paper_id
    - section
    - text
    """

    chunks = []

    for section_name, text in sections.items():
        if not text:
            continue

        words = text.split()

        for i in range(0, len(words), max_words):
            chunk_text = " ".join(words[i:i + max_words])

            if len(chunk_text.strip()) < 30:
                continue

            chunks.append({
                "paper_id": paper_id,
                "section": section_name.lower(),
                "text": chunk_text
            })

    return chunks
