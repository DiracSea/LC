class Solution:
    # set
    def findRepeatedDnaSequences(self, s: str):
        seen = set() 
        repeated = set() 
        for i in range(len(s)-9): 
            ten = s[i:i+10] 
            if ten in seen:  
                repeated.add(ten) 
            else:
                seen.add(ten)
            
        return list(repeated)

    # dict
    def findRepeatedDnaSequences1(self, s: str):
        seq = {} 
        for i in range(len(s)): 
            seq[s[i:i+10]] = seq.get(s[i:i+10], 0) + 1 
        return [key for (key, value) in seq.items() if value > 1]