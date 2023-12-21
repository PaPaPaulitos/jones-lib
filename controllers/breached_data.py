import os
from typing import List

import pandas as pd

from interfaces.ifile import IFile
from models.file_csv import FileCSV
from models.file_xlsx import FileXLSX
from models.file_json import FileJSON

class BreachedData:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def filter(self,dict_data:list):
        new_dict_data = list()

        for i in dict_data:
            df  = pd.DataFrame([i])
            df = df[['username', 'email']]

            dict_output = df.to_dict(orient='records')[0]
            new_dict_data.append(dict_output)

        return new_dict_data
    
    def search(self,dict_data:list,username:str,email:str):
        for i in dict_data:
            if i['username'] == username or i['email'] == email:
                return True
        return False
    
    def get_files_list(self) -> List[str]:
        try:
            entries = os.listdir(self.directory_path)
            files = [entry for entry in entries if os.path.isfile(os.path.join(self.directory_path, entry))]
            return files
        except FileNotFoundError:
            print(f"O diretório {self.directory_path} não foi encontrado.")
            return []
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return []
        
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


    def read(self,filepath:str):
        self.file = self._get_file_handler(filepath)
        return self.file.read()


        