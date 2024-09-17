import os
import requests
from urllib.parse import urlparse
from utils.support import get_file_extension
from utils.fileprocess import read_file_pdf

def get_content(response: requests.Response, type: str) -> str:
    if type=='pdf':
        file_path = os.path.join('uploads','temporary.pdf')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return read_file_pdf(file_path)

class URL:
    def __init__(self, response: requests.Response) -> None:
        self.parsed_url = urlparse(response.url)
        self.type = 'ytvideo' if '/watch' in self.parsed_url.path else get_file_extension(self.parsed_url.path)[1:] if get_file_extension(self.parsed_url.path)[1:] in ('pdf','txt') else None
        self.content = get_content(response, self.type)