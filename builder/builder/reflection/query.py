from builder.reflection.database import database

class ReflectionQuery:

    def classes(self):
        return [
            s for s in database.symbols
            if s.kind == "class"
        ]

    def functions(self):
        return [
            s for s in database.symbols
            if s.kind == "function"
        ]

query = ReflectionQuery()
