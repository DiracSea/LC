class Solution: 
    # hash map 
    def isAnagram1(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
        
    def isAnagram2(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
    
    # sorted 
    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)
    
    # quick 
    def isAnagram(self, s: str, t: str) -> bool:
        import string
        alpha = list(string.ascii_letters)
        if len(s) != len(t):
            return len(s) == len(t)
            exit()
        else:
            for i in alpha:
                if s.count(i) != t.count(i):
                    return s.count(i) == t.count(i)
                    exit()
        return len(s) == len(t)