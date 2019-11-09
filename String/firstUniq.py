class Solution:
    # brute force 
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)): 
            if s[i] not in s[0:i]+s[i+1:]: 
                return i 
        return -1 
    
    # alphabet
    def firstUniqChar1(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    # ord    
    def firstUniqChar2(self, s: str) -> int: 
        freq = [0]*26 
        for i in range(0, len(s)): 
            freq[ord(s[i]) - ord('a')] += 1 
        for i in range(0, len(s)): 
            if freq[ord(s[i]) - ord('a')] is 1: 
                return i 
        return -1       