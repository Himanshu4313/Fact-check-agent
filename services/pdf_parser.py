import fitz

def extract_text(pdf_file):
    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    return text