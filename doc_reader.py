from bs4 import BeautifulSoup
import PyPDF2
import docx 
import os

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        parsed_html = BeautifulSoup(file.read(), 'html.parser')
        text = parsed_html.get_text()
        return text

def read_pdf_file(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text += page.extract_text()
    return text

def read_docx_file(file_path):
    doc = docx.Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        return text


def read_doc(file_path):
    if os.path.exists(file_path):
        extension = os.path.splitext(file_path)[1].lower()
        if extension == '.html':
            text = read_html_file(file_path)
            return text
        elif extension == '.pdf':
            text = read_pdf_file(file_path)
            return text
        elif extension == '.docx':
            text = read_docx_file(file_path)
            return text
        elif extension == '.txt':
            text = read_txt_file(file_path)
            return text
        else:
            print('Unsupported file format')
    else:
        print('File not found')