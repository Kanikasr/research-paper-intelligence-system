import re
from typing import Dict


SECTION_HEADERS = [
    "abstract",
    "introduction",
    "background",
    "related work",
    "method",
    "methodology",
    "approach",
    "model",
    "experiments",
    "results",
    "discussion",
    "conclusion",
    "future work",
    "references"
]


def split_into_sections(text: str) -> Dict[str, str]:
    """
    Split raw paper text into structured sections based on common academic headings.

    Args:
        text (str): Full text extracted from PDF

    Returns:
        Dict[str, str]: section_name -> section_content
    """

    # Normalize text
    clean_text = re.sub(r"\n+", "\n", text.lower())

    sections = {}
    current_section = "unknown"
    sections[current_section] = []

    for line in clean_text.split("\n"):
        line_stripped = line.strip()

        if not line_stripped:
            continue

        # Check if line matches a section header
        for header in SECTION_HEADERS:
            if line_stripped == header:
                current_section = header
                sections[current_section] = []
                break
        else:
            sections[current_section].append(line_stripped)

    # Join lines per section
    final_sections = {
        section: " ".join(content)
        for section, content in sections.items()
        if content
    }

    return final_sections
