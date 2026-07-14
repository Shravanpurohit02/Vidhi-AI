from __future__ import annotations

class ResultDeduplicator:

    def deduplicate(self,results):

        seen=set()
        output=[]

        for item in results:

            key=getattr(item,"chunk_id",id(item))

            if key in seen:
                continue

            seen.add(key)
            output.append(item)

        return output
