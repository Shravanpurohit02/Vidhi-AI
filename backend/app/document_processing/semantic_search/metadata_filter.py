from __future__ import annotations

class MetadataFilter:

    @staticmethod
    def apply(results,filters):

        if filters is None:
            return results

        output=[]

        for item in results:

            meta=item.metadata or {}

            ok=True

            for field,value in filters.model_dump(exclude_none=True).items():

                if field=="metadata":
                    continue

                if meta.get(field)!=value:
                    ok=False
                    break

            if ok:
                output.append(item)

        return output
