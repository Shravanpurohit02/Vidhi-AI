from app.integrations.courts.ecourts import ECourtsProvider


class CourtProviderRegistry:

    def __init__(self):

        self.providers = {
            "official_ecourts": ECourtsProvider(),
        }

    def get(self, name="official_ecourts"):
        return self.providers[name]
