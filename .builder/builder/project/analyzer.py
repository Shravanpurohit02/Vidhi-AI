from builder.project.registry import registry

class ProjectAnalyzer:

    def summary(self):
        files = registry.all()

        return {
            "files": len(files),
            "python": sum(
                f.extension == ".py"
                for f in files
            ),
            "json": sum(
                f.extension == ".json"
                for f in files
            ),
            "markdown": sum(
                f.extension == ".md"
                for f in files
            ),
        }

analyzer = ProjectAnalyzer()
