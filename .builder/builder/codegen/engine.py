from builder.codegen.generator import generator
from builder.codegen.parser import cleaner, extractor
from builder.codegen.request import CodeGenerationRequest
from builder.codegen.response import CodeGenerationResponse

class CodeEngine:

    def generate(self, request: CodeGenerationRequest):

        result = generator.generate(request)

        code = cleaner.clean(
            extractor.code(result.text)
        )

        return CodeGenerationResponse(
            success=result.success,
            provider=result.provider,
            model=result.model,
            code=code,
            raw=result.raw,
        )

engine = CodeEngine()
