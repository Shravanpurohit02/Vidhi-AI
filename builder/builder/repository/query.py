from builder.repository.database import database

class RepositoryQuery:

    def by_extension(self, extension: str):
        return [
            f for f in database.all()
            if f.extension == extension
        ]

    def by_name(self, text: str):
        text = text.lower()
        return [
            f for f in database.all()
            if text in f.name.lower()
        ]

query = RepositoryQuery()
