class Solution: 
    # same as isomophicString
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = list(pattern) 
        str = str.split() 
        if len(pattern) is not len(str): return False 
        return len(set(zip(pattern,str))) == len(set(pattern)) == len(set(str)) 