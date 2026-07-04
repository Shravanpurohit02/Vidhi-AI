import re

from bs4 import BeautifulSoup

from app.court.session import BASE_URL, session_manager


class ECourtsBootstrap:

    SEARCH_URL = BASE_URL + "/?p=cnr_status/index"

    def bootstrap(self, session_id: str):
        data = session_manager.get_data(session_id)
        session = data.session

        print("BOOTSTRAP: GET", self.SEARCH_URL)
        print("\n========== BOOTSTRAP REQUESTS ==========")
        def hook(resp,*args,**kwargs):
            print(resp.request.method, resp.url, "->", resp.status_code)
        session.hooks['response']=[hook]

        r = session.get(self.SEARCH_URL, timeout=30)

        print("BOOTSTRAP: STATUS", r.status_code)
        r.raise_for_status()

        html = r.text
        print("BOOTSTRAP: HTML LENGTH", len(html))
        from pathlib import Path
        Path("bootstrap.html").write_text(html, encoding="utf-8")
        print("BOOTSTRAP: HTML SAVED")

        from pathlib import Path
        Path("backend/bootstrap.html").write_text(html, encoding="utf-8")

        token = ""

        m = re.search(r'"app_token"\s*:\s*"([^"]+)"', html)
        if m:
            token = m.group(1)

        if not token:
            m = re.search(r'name="app_token"\s+value="([^"]*)"', html)
            if m:
                token = m.group(1)

        soup = BeautifulSoup(html, "html.parser")

        hidden = {}

        for inp in soup.select("input[type=hidden]"):
            name = inp.get("name")
            if not name:
                continue
            hidden[name] = inp.get("value", "")

        session_manager.set_token(session_id, token)
        session_manager.set_hidden_fields(session_id, hidden)

        return {
            "token": token,
            "hidden_fields": hidden,
        }


bootstrap_service = ECourtsBootstrap()
