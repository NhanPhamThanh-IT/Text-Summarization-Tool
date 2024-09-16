def preprocess_text(text : str) -> str:
    text = ' '.join(paragraph.strip() for paragraph in text.splitlines() if paragraph.strip() != '')
    return text