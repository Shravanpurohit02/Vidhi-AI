import ast

class PatchValidator:

    def validate(self, source: str):

        try:
            ast.parse(source)
            return True
        except Exception:
            return False

validator = PatchValidator()
