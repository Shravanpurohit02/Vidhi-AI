from builder.codegen.parser.json import parser as json_parser
from builder.codegen.parser.markdown import parser as markdown_parser

class Extractor:

    def code(self, response):

        data = json_parser.parse(response)

        text = data["choices"][0]["message"]["content"]

        return markdown_parser.extract(text)

extractor = Extractor()
