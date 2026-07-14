from builder.repository.file import RepositoryFile

class RepositoryDatabase:

    def __init__(self):
        self._files = {}

    def add(self, item: RepositoryFile):
        self._files[item.path] = item

    def get(self, path: str):
        return self._files.get(path)

    def all(self):
        return list(self._files.values())

database = RepositoryDatabase()
