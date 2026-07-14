from __future__ import annotations

class ResultFormatter:

    def format(self,results):

        output=[]

        for item in results:

            output.append({
                "document_id":getattr(item,"document_id",None),
                "chunk_id":getattr(item,"chunk_id",None),
                "score":round(getattr(item,"score",0.0),4),
                "metadata":getattr(item,"metadata",{}),
            })

        return output
