class Solution:
    # one line 
    def reverseWords(self, s: str) -> str: 
        return ' '.join(reversed(s.split())) 


    # no split, two pointers 