import json
import re

from app.court.captcha import captcha_service
from app.court.session import BASE_URL, session_manager
from app.integrations.courts.bootstrap import bootstrap_service


class ECourtsProvider:

    async def create_session(self):
        sid = session_manager.create()
        bootstrap_service.bootstrap(sid)
        return sid

    async def fetch_captcha(self, session_id: str):
        data = session_manager.get_data(session_id)

        if not data.app_token:
            bootstrap_service.bootstrap(session_id)

        return captcha_service.fetch(session_id)

    async def search_by_cnr(
        self,
        *,
        session_id: str,
        cnr: str,
        captcha: str,
    ):
        data = session_manager.get_data(session_id)

        if not data.app_token:
            bootstrap_service.bootstrap(session_id)
            data = session_manager.get_data(session_id)

        session = data.session

        payload = dict(data.hidden_fields)

        payload.update(
            {
                "cino": cnr.strip().upper(),
                "fcaptcha_code": captcha.strip(),
                "ajax_req": "true",
                "app_token": data.app_token,
            }
        )

        response = session.post(
            BASE_URL + "/?p=cnr_status/searchByCNR/",
            headers={
                "User-Agent": session.headers["User-Agent"],
                "Referer": BASE_URL + "/?p=cnr_status/index",
                "Origin": "https://services.ecourts.gov.in",
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json,text/plain,*/*",
            },
            data=payload,
            timeout=30,
        )

        response.raise_for_status()

        text = response.text

        try:
            body = response.json()

            if isinstance(body, dict):
                if body.get("app_token"):
                    session_manager.set_token(
                        session_id,
                        body["app_token"],
                    )

                return {
                    "success": True,
                    "provider": "ecourts",
                    "raw": body,
                }

        except Exception:
            body = None

        match = re.search(
            r'(\{"errormsg".*)',
            text,
            re.S,
        )

        if match:
            return {
                "success": True,
                "provider": "ecourts",
                "raw": json.loads(match.group(1)),
            }

        return {
            "success": True,
            "provider": "ecourts",
            "raw_text": text,
        }

    async def search_case(
        self,
        *,
        state="",
        district="",
        court="",
        case_number="",
        year="",
    ):
        return {
            "success": False,
            "message": "Search by case details not implemented yet.",
        }
