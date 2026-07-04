from app.integrations.courts.provider_registry import CourtProviderRegistry


class CourtIntegrationService:

    def __init__(self):
        self.registry = CourtProviderRegistry()

    async def search_by_cnr(self, cnr: str):

        provider = self.registry.get()

        return await provider.search_by_cnr(cnr)

    async def search_case(
        self,
        *,
        state: str = "",
        district: str = "",
        court: str = "",
        case_number: str = "",
        year: str = "",
    ):

        provider = self.registry.get()

        return await provider.search_case(
            state=state,
            district=district,
            court=court,
            case_number=case_number,
            year=year,
        )
