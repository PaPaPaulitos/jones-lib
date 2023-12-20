import os
from interfaces.ifile import IFile
from models.file_csv import FileCSV
from models.file_xlsx import FileXLSX
from models.file_json import FileJSON

class ReadFile:
    def __init__(self, filepath: str):
        self.file = self._get_file_handler(filepath)

    def read(self):
        return self.file.read()

    def _get_file_handler(self, filepath: str) -> IFile:
        _, file_extension = os.path.splitext(filepath)
        if file_extension.lower() == '.csv':
            return FileCSV(filepath)
        elif file_extension.lower() == '.xlsx':
            return FileXLSX(filepath)
        elif file_extension.lower() == '.json':
            return FileJSON(filepath)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")



