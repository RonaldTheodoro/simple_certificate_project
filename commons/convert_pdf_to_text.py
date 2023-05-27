from io import BytesIO

from pypdf import PdfReader


def convert_pdf_to_text(pdf):
    reader = PdfReader(BytesIO(pdf))
    pages = [p.extract_text() for p in reader.pages]
    return "".join(pages)
