import PyPDF2
import docx
import re

def extract_text_from_file(filepath):
    if filepath.endswith('.pdf'):
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ' '.join([page.extract_text() for page in reader.pages])
    elif filepath.endswith('.docx'):
        doc = docx.Document(filepath)
        text = ' '.join([para.text for para in doc.paragraphs])
    else:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    return clean_text(text)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    return text.strip()