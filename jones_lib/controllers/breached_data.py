import re
import os
from typing import List, Dict

import pandas as pd

from ..interfaces.ifile import IFile
from ..models.file_csv import FileCSV
from ..models.file_xlsx import FileXLSX
from ..models.file_json import FileJSON

class BreachedData:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def filter(self,dict_data:list)-> Dict:
        new_dict_data = list()

        for i in dict_data:
            df  = pd.DataFrame([i])
            df = df[['username', 'email']]

            dict_output = df.to_dict(orient='records')[0]
            new_dict_data.append(dict_output)

        return new_dict_data
    
    def search(self,dict_data:list,username:str=None,email:str=None) -> bool:
        for i in dict_data:
            if i['username'] == username or i['email'] == email:
                return True
        return False
    
    def get_files_list(self) -> List[str]:
        try:
            files_list = list()
            entries = os.listdir(self.directory_path)
            files = [entry for entry in entries if os.path.isfile(os.path.join(self.directory_path, entry))]
            for filename in files:
                new_dict = dict()

                match = re.match(r'(.+?)\.', filename)
                if match:
                    website_name = match.group(1)
                    new_dict[filename] = website_name
                    files_list.append(new_dict)
                else:
                    raise ValueError(f"Invalid filename: {filename}")
            
            return files,files_list

        except FileNotFoundError:
            print(f"PATH {self.directory_path} not found")
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


    def read(self,file:str) -> Dict:
        self.file = self._get_file_handler(self.directory_path + file)
        return self.file.read()


    def scan(self,username=None,email=None)-> list:
        files,file_list = self.get_files_list()

        list_websites = list()

        for file in files:
            data = self.read(file)
            filtered_data = self.filter(data)

            in_breached_data = self.search(filtered_data,username,email)

            try:
                if in_breached_data:
                    for f in file_list:
                        if file in f.keys():
                            new_dict = dict()
                            new_dict[f[file]] = True
                            list_websites.append(new_dict)
                elif not in_breached_data:
                    for f in file_list:
                        if file in f.keys():
                            new_dict = dict()
                            new_dict[f[file]] = False
                            list_websites.append(new_dict)

            except Exception as e:
                print(e)

        return list_websites

        