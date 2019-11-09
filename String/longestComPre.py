class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len) # the smallest one 
        for i, ch in enumerate(shortest): # iterate char of the shortest 
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
    
    def longestCommonPrefix1(self, m):
        if not m: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1