from typing import Any
import fitz # PyMuPDF
import docx # Python-docx
from docx.opc.exceptions import PackageNotFoundError

def read_file_txt(file_path : str) -> str:
    """
    Reads the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file if successful, or an error message if the file is not found or an I/O error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return "Error: The file was not found !"
    except IOError:
        return "Error: An I/O error occurred while reading the file !"

def read_file_pdf(file_path: str) -> str:
    """
    Reads the content of a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The combined text from all pages of the PDF file if successful, or an error message if an error occurs while opening or reading the file.
    """
    all_text = ""
    try:
        pdf_document = fitz.open(file_path)
        try:
            for page_num in range(len(pdf_document)):
                try:
                    page = pdf_document.load_page(page_num)
                    all_text += page.get_text()
                except Exception as e:
                    return f"Error reading page {page_num}: {e} !"
        finally:
            pdf_document.close()
    except Exception as e:
        return f"Error opening file {file_path}: {e} !"
    return all_text

def read_file_docx(file_path : str) -> str:
    """
    Reads the content from a .docx file and returns it as a string.

    Args:
        file_path (str): The path to the .docx file to be read.

    Returns:
        str: The text content from the .docx file, or an error message if an exception occurs.

    Exceptions:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there are insufficient permissions to access the file.
        PackageNotFoundError: If the file is not a valid .docx document.
        OSError: If an OS-related error occurs (e.g., file system issues).
        Exception: For any other unexpected errors.
    """
    try:
        doc = docx.Document(file_path)
        full_text = [paragraph.text for paragraph in doc.paragraphs]
        return '\n'.join(full_text)
    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except PermissionError:
        return "Error: Permission denied. Please check the file permissions."
    except PackageNotFoundError:
        return "Error: The file is not a valid .docx document."
    except OSError as e:
        return f"Error: An OS error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def read_file(path : str, extension : str) -> str:
    """
    Reads the content of a file based on its extension.

    Args:
        path (str): The path to the file.
        extension (str): The file extension, e.g., 'txt', 'pdf' or 'docx'.

    Returns:
        str: The content of the file if successful, or None if the extension is not supported.
    """
    if extension=='txt':
        return read_file_txt(path)
    if extension=='pdf':
        return read_file_pdf(path)
    if extension=='docx':
        return read_file_docx(path)
    return None

class ReadFile:
    """
    A class to read and store the content of a file based on its path.

    Attributes:
        path (str): The file path with normalized slashes.
        name (str): The name of the file.
        extension (str): The file extension in lowercase.
        content (str): The content of the file read using the appropriate method based on its extension.
    """

    def __init__(self, path : str) -> None:
        """
        Initializes the ReadFile instance and reads the file content.

        Args:
            path (str): The path to the file to be read.
        """
        self.path = path.replace('\\', '/')
        self.name = self.path.split('/')[-1]
        self.extension = self.name.split('.')[-1].lower()
        self.content = read_file(self.path, self.extension)
    
    def __getattribute__(self, name: str) -> Any:
        """
        Retrieves the attribute value of the instance.

        This method is overridden to customize attribute access. It currently calls the superclass method to get the attribute.

        Args:
            name (str): The name of the attribute to retrieve.

        Returns:
            Any: The value of the requested attribute.
        """
        return super().__getattribute__(name)