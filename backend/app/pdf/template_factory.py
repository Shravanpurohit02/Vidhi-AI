from app.pdf.templates.classic import ClassicTemplate
from app.pdf.templates.modern import ModernTemplate


class TemplateFactory:

    _templates = {
        "classic": ClassicTemplate,
        "modern": ModernTemplate,
    }

    @classmethod
    def get(cls, name: str = "classic"):
        template = cls._templates.get((name or "classic").lower())

        if template is None:
            template = ClassicTemplate

        return template()
