import re

SECTION_HEADERS = ["abstract", "introduction", "model", "method", "results", "conclusion", "references"]

def split_into_sections(text: str):
    sections = {}
    current = "unknown"
    sections[current] = []

    for line in text.split("\n"):
        lower = line.lower().strip()
        if lower in SECTION_HEADERS:
            current = lower
            sections[current] = []
        sections[current].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}
