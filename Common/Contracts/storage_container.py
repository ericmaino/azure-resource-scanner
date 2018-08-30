from abc import ABC, abstractmethod

class StorageContainer(ABC):

    @abstractmethod
    def upload_text(self, filename, text):
        raise NotImplementedError("Should have implemented upload_text")
