import PyPDF2
import io

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text