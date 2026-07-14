from .context import create_context

class EmbeddedBuilder:

    def context(self):
        return create_context()

builder = EmbeddedBuilder()
