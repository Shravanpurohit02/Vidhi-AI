class CourtParser:

    def parse(self, payload):

        if not isinstance(payload, dict):
            return {
                "success": False,
                "type": "unknown",
                "raw": payload,
            }

        error = payload.get("errormsg", "").strip()
        error_lower = error.lower()

        if "captcha" in error_lower:
            return {
                "success": False,
                "type": "invalid_captcha",
                "message": error,
                "raw": payload,
            }

        if "case" in error_lower or "cnr" in error_lower:
            return {
                "success": False,
                "type": "case_not_found",
                "message": error,
                "raw": payload,
            }

        if error:
            return {
                "success": False,
                "type": "provider_error",
                "message": error,
                "raw": payload,
            }

        history = payload.get("historytable", "")

        if history:
            return {
                "success": True,
                "type": "case_found",
                "history_html": history,
                "raw": payload,
            }

        return {
            "success": False,
            "type": "unknown_response",
            "raw": payload,
        }


court_parser = CourtParser()
