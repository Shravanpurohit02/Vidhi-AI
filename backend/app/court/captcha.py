from app.court.session import BASE_URL, session_manager


class CaptchaService:

    def fetch(self, session_id: str) -> bytes:
        session = session_manager.get(session_id)

        try:
            response = session.get(
                BASE_URL + "/vendor/securimage/securimage_show.php",
                headers={
                    "User-Agent": session.headers["User-Agent"],
                    "Referer": BASE_URL + "/",
                    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                },
                timeout=30,
            )

            response.raise_for_status()
            return response.content

        except Exception as exc:
            raise RuntimeError("Failed to fetch eCourts CAPTCHA.") from exc


captcha_service = CaptchaService()
