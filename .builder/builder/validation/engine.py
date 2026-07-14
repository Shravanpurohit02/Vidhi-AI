from builder.validation.project import project


class ValidationEngine:

    def _summary(self, results):

        return {
            "files": len(results),
            "passed": sum(r.success for r in results),
            "failed": sum(not r.success for r in results),
            "errors": [
                r
                for r in results
                if not r.success
            ],
        }

    def validate(self, workspace: str):

        return self._summary(
            project.validate(workspace)
        )

    def validate_files(self, paths):

        return self._summary(
            project.validate_files(paths)
        )


engine = ValidationEngine()
