class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0 
        for idx, l in enumerate(s[::-1]): 
            p = 1 
            for i in range(idx): p *= 26
            num += (ord(l) - ord('A') + 1)*p
        return num 