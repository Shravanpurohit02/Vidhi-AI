import json

class JSONParser:

    def parse(self, raw):

        if isinstance(raw, dict):
            return raw

        return json.loads(raw)

parser = JSONParser()
