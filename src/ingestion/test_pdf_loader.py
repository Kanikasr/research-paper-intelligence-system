from pdf_loader import load_pdf_text

if __name__ == "__main__":
    pdf_path = "../../data/raw_papers/attention_is_all_you_need.pdf"
    text = load_pdf_text(pdf_path)

    print("PDF LOADED SUCCESSFULLY")
    print("First 1000 characters:\n")
    print(text[:1000])
