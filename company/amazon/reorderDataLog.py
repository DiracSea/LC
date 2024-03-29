class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort(log): 
            idx, rest = log.split(" ", 1) 
            return (0, rest, idx) if rest[0].isalpha() else (1,) # (1, rest, idx) 
        return sorted(logs, key = sort)