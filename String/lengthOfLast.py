class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        l = 0  
        for i in reversed(s): 
            if l is 0 and i is ' ': 
                continue
            elif i is ' ': 
                break  
            l += 1 
        return l 
    
    def lengthOfLastWord1(self, s: str) -> int: 
        return len(s.rstrip(' ').split(' ')[-1])

    def lengthOfLastWord2(self, s):
        ls = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow-=1
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast