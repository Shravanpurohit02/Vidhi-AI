from __future__ import annotations

class StatuteMapper:

    MAP={
        "murder":"IPC",
        "bail":"CrPC",
        "contract":"Indian Contract Act",
        "property":"Transfer of Property Act",
        "evidence":"Indian Evidence Act",
    }

    def map(self,issues:list[str])->dict:

        return {
            issue:self.MAP.get(issue,"Unknown")
            for issue in issues
        }
