import os

def preprocess_text(text : str) -> str:
    """
    Preprocesses a given text by removing empty lines and leading/trailing whitespace from each paragraph.

    Args:
        text (str): The input text to be preprocessed.

    Returns:
        str: The preprocessed text with empty lines removed and paragraphs trimmed.
    """
    text = ' '.join(paragraph.strip() for paragraph in text.splitlines() if paragraph.strip() != '')
    return text

def get_file_extension(path):
    """
    Extracts the file extension from a given file path.

    Args:
        path (str): The file path from which to extract the extension.

    Returns:
        str: The file extension, including the leading dot (e.g., '.txt'). If there is no extension, returns an empty string.
    """
    _, extension = os.path.splitext(path)
    return extension