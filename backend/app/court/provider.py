from app.integrations.courts.ecourts import ECourtsProvider


class CourtProvider:

    def __init__(self):
        self.provider = ECourtsProvider()

    async def search_by_cnr(
        self,
        *,
        session_id: str,
        cnr: str,
        captcha: str = "",
    ):
        return await self.provider.search_by_cnr(
            session_id=session_id,
            cnr=cnr,
            captcha=captcha,
        )

    async def search_case(
        self,
        *,
        state: str = "",
        district: str = "",
        court: str = "",
        case_number: str = "",
        year: str = "",
    ):
        return await self.provider.search_case(
            state=state,
            district=district,
            court=court,
            case_number=case_number,
            year=year,
        )
