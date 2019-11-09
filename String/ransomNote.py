class Solution:
    # brute force 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        d = {} 
        for r in ransomNote: 
            if r not in d: 
                d[r] = 1  
            else: 
                d[r] += 1 
        for m in magazine: 
            if m in d: 
                d[m] -= 1 
        for v in d.values(): 
            if v > 0: 
                return False 
        return True 
    
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):#using set and count if their set have the same number, return true, else False
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool: 
        return # not collections.Counter(ransomNote) - collections.Counter(magazine)