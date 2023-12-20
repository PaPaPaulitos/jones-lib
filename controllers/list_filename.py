import os
from typing import List

class DirectoryScanner:
    def __init__(self, directory_path):
        self.directory_path = directory_path

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

# Exemplo de uso:

