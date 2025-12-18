from pdf_loader import load_pdf_text
from section_parser import split_into_sections

if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"

    raw_text = load_pdf_text(pdf_path)
    sections = split_into_sections(raw_text)

    print("SECTIONS FOUND:\n")

    for section, content in sections.items():
        print(f"\n--- {section.upper()} ---")
        print(content[:500])
