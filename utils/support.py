import os

def preprocess_text(text : str) -> str:
    text = ' '.join(paragraph.strip() for paragraph in text.splitlines() if paragraph.strip() != '')
    return text

def get_file_extension(path):
    _, extension = os.path.splitext(path)
    return extension