from typing import Dict, Any
import csv

from ..interfaces import IFile

class FileCSV(IFile):
    def __init__(self, file):
        self.file = file

    def read(self) -> Dict[str, Any]:
        data = []
        with open(self.file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data