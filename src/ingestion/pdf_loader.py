from pypdf import PdfReader

def load_pdf_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        if page.extract_text():
            text.append(page.extract_text())
    return "\n".join(text)
