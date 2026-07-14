from abc import ABC, abstractmethod
from io import BytesIO


class BaseInvoiceTemplate(ABC):

    @abstractmethod
    def render(self, invoice) -> BytesIO:
        pass
