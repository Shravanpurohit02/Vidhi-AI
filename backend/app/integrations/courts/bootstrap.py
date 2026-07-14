import re

from bs4 import BeautifulSoup

from app.court.session import BASE_URL, session_manager


class ECourtsBootstrap:

    SEARCH_URL = BASE_URL + "/?p=cnr_status/index"

    def bootstrap(self, session_id: str):
        data = session_manager.get_data(session_id)
        session = data.session

        response = session.get(
            self.SEARCH_URL,
            timeout=30,
        )
        response.raise_for_status()

        html = response.text

        token = ""  # nosec B105

        match = re.search(r'"app_token"\s*:\s*"([^"]+)"', html)
        if match:
            token = match.group(1)

        if not token:
            match = re.search(
                r'name="app_token"\s+value="([^"]*)"',
                html,
            )
            if match:
                token = match.group(1)

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        hidden = {}

        for inp in soup.select("input[type=hidden]"):
            name = inp.get("name")
            if name:
                hidden[name] = inp.get("value", "")

        session_manager.set_token(
            session_id,
            token,
        )

        session_manager.set_hidden_fields(
            session_id,
            hidden,
        )

        return {
            "token": token,
            "hidden_fields": hidden,
        }


bootstrap_service = ECourtsBootstrap()
