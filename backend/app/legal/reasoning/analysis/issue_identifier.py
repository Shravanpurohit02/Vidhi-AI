from __future__ import annotations

class IssueIdentifier:

    def identify(self,text:str)->list[str]:

        issues=[]

        keywords=[
            "murder","contract","property","article",
            "section","appeal","bail","evidence",
            "negligence","constitutional","arbitration"
        ]

        lower=text.lower()

        for word in keywords:
            if word in lower:
                issues.append(word)

        return sorted(set(issues))
