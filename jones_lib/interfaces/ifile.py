from abc import ABC, abstractmethod
from typing import Dict, Any

class IFile(ABC):
    @abstractmethod
    def read(self) -> Dict[str, Any]:
        pass
