from abc import ABC, abstractmethod

class Data(ABC):
    
    @abstractmethod
    def create_dict(self):
        pass