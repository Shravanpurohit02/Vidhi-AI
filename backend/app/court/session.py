import secrets
import threading
import time
from dataclasses import dataclass, field

import requests

BASE_URL = "https://services.ecourts.gov.in/ecourtindia_v6"

SESSION_TTL = 900  # 15 minutes


@dataclass
class SessionData:
    session_id: str
    session: requests.Session
    app_token: str = ""
    hidden_fields: dict = field(default_factory=dict)
    created_at: float = field(default_factory=time.time)
    last_used: float = field(default_factory=time.time)


class CourtSessionManager:

    def __init__(self):
        self._sessions: dict[str, SessionData] = {}
        self._lock = threading.Lock()

    def _new_requests_session(self) -> requests.Session:
        s = requests.Session()

        s.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0.0.0 Safari/537.36"
                ),
                "Accept": (
                    "text/html,application/xhtml+xml,"
                    "application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
                ),
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
        )

        return s

    def cleanup(self):
        now = time.time()

        expired = [
            sid
            for sid, data in self._sessions.items()
            if now - data.last_used > SESSION_TTL
        ]

        for sid in expired:
            self._sessions.pop(sid, None)

    def create(self) -> str:

        with self._lock:

            self.cleanup()

            sid = secrets.token_urlsafe(32)

            session = self._new_requests_session()

            data = SessionData(
                session_id=sid,
                session=session,
            )

            self._sessions[sid] = data

            return sid

    def get_data(self, sid: str) -> SessionData:

        if sid not in self._sessions:
            raise KeyError(f"Unknown session {sid}")

        data = self._sessions[sid]

        data.last_used = time.time()

        return data

    def get(self, sid: str) -> requests.Session:
        return self.get_data(sid).session

    def set_token(self, sid: str, token: str):
        self.get_data(sid).app_token = token or ""

    def set_hidden_fields(self, sid: str, fields: dict):
        self.get_data(sid).hidden_fields = dict(fields)

    def remove(self, sid: str):
        self._sessions.pop(sid, None)


session_manager = CourtSessionManager()
