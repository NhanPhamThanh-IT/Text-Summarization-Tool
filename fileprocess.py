from typing import Any

def read_file_txt(file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                return text
        except FileNotFoundError:
            return "Error: The file was not found !"
        except IOError:
            return "Error: An I/O error occurred while reading the file !"

def read_file(path : str, extension : str):
    if extension=='txt':
        return read_file_txt(path)
    return None

class ReadFile:
    def __init__(self, path : str) -> None:
        self.path = path.replace('\\', '/')
        self.name = self.path.split('/')[-1]
        self.extension = self.name.split('.')[-1]
        self.content = read_file(self.path, self.extension)
    
    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)