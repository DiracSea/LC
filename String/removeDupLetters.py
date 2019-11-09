class Solution:
    # lexi sort 
    def removeDuplicateLetters(self, s: str) -> str: 
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

    # stack 
    def removeDuplicateLetters1(self, s: str) -> str:
        m = {}
        
        for i, v in enumerate(s): m[v] = i
        
        stack = []
        
        contain = set()
        for i, v in enumerate(s):
            if v not in contain:
                while stack and stack[-1] > v and m[stack[-1]] > i:
                    contain.remove(stack.pop())
                stack.append(v)
                contain.add(v)
            
        return ''.join(stack)