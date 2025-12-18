from pathlib import Path
from pypdf import PdfReader


def load_pdf_text(pdf_path: str) -> str:
    """
    Load a research paper PDF and extract raw text from all pages.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Combined text from all pages
        """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    reader = PdfReader(pdf_path)
    full_text = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            cleaned_text = text.strip()
            full_text.append(cleaned_text)

    return "\n".join(full_text)
