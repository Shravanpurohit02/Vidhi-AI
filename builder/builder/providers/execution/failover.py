from __future__ import annotations


RETRY_STATUS = {
    408,
    409,
    425,
    429,
    500,
    502,
    503,
    504,
}


class FailoverEngine:

    def should_retry(self, response):

        if response is None:
            return True

        if getattr(response, "is_success", False):
            return False

        status = getattr(response, "status_code", 0)

        return status in RETRY_STATUS

    def providers(self, router):

        try:
            return list(router.available())
        except Exception:
            return []


engine = FailoverEngine()
