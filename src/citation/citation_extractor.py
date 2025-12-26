import re

def extract_citations(reference_text: str):
    """
    Extract cited paper titles from a References section.
    Uses a relaxed heuristic suitable for GA03.
    """
    citations = []

    if not reference_text:
        return citations

    lines = reference_text.split("\n")

    for line in lines:
        line = line.strip()

        # Skip numbering lines
        if not line or line.startswith("["):
            continue

        # Heuristic: sentence ending before year
        match = re.search(r"^(.*?)(?:,\s*\d{4}|\.\s*\d{4})", line)
        if match:
            title = match.group(1).strip()
            if len(title.split()) > 3:
                citations.append(title)

    return list(set(citations))
