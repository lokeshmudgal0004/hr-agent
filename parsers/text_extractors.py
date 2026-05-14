from langchain_community.document_loaders import PyMuPDFLoader
import fitz 
from docx import Document


def extract_text_from_pdf(file_path):
    loader = PyMuPDFLoader(file_path)

    documents = loader.load()

    text = "\n".join([doc.page_content for doc in documents])

    return text


def extract_text_from_docx(file_path): 
    doc = Document(file_path) 
    text = "\n".join([para.text for para in doc.paragraphs]) 
    
    return text