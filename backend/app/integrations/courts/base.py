from abc import ABC, abstractmethod


class BaseCourtProvider(ABC):

    name: str = ""

    @abstractmethod
    async def search_by_cnr(self, cnr: str) -> dict: ...

    @abstractmethod
    async def search_case(
        self,
        *,
        state: str = "",
        district: str = "",
        court: str = "",
        case_number: str = "",
        year: str = "",
    ) -> dict: ...
