from app.court.provider import CourtProvider


class CourtService:

    def __init__(self):
        self.provider = CourtProvider()

    async def create_session(self):
        return await self.provider.provider.create_session()

    async def fetch_captcha(self, session_id: str):
        return await self.provider.provider.fetch_captcha(session_id)

    async def search_by_cnr(
        self,
        session_id: str,
        cnr: str,
        captcha: str,
    ):
        return await self.provider.provider.search_by_cnr(
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
