from typing import List, Dict


def chunk_paper(
    paper_id: str,
    sections: Dict[str, str],
    max_words: int = 200
) -> List[Dict]:
    """
    Chunk paper sections into smaller semantic units.

    Each chunk preserves metadata:
    - paper_id
    - section name
    """
    chunks = []

    for section_name, content in sections.items():
        words = content.split()

        for i in range(0, len(words), max_words):
            chunk_text = " ".join(words[i:i + max_words])

            chunk = {
                "paper_id": paper_id,
                "section": section_name,
                "text": chunk_text
            }
            chunks.append(chunk)

    return chunks
