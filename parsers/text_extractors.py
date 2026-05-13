import fitz
from docx import Document


def extract_text_from_pdf(file_path):
    text = ""

    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    return text


def extract_text_from_docx(file_path):
    doc = Document(file_path)

    text = "\n".join([para.text for para in doc.paragraphs])

    return text