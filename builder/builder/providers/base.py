from abc import ABC, abstractmethod

class BaseProvider(ABC):

    name = "base"

    @abstractmethod
    def generate(self, request):
        raise NotImplementedError
