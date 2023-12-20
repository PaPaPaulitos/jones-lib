import json
from interfaces import IFile
from typing import Dict, Any

class FileJSON(IFile):
    def __init__(self, file):
        self.file = file

    def read(self) -> Dict[str, Any]:
        with open(self.file, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data