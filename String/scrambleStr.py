class Solution: 
    def isScramble(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m != n or sorted(s1) != sorted(s2): 
            return False 
        if m < 4 or s1 == s2: return True 
        # if len(s1) is not len(s2): return False 
        
        '''
        letters = [0]*26 
        for i in range(0, len(s1)): 
            letters[ord(s1[i]) - ord('a')] += 1 
            letters[ord(s2[i]) - ord('a')] -= 1 
        for i in range(0, 26): 
            if letters[i] is not 0: return False 
        '''
        
        '''
        for i in range(0, len(s1)): 
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i], s2[i]): return True 
            if self.isScramble(s1[0:i], s2[len(s2)-i]) and self.isScramble(s1[i], s2[0:len(s2)-i]): return True 
        '''
        f = self.isScramble 
        for i in range(1, m): 
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]): 
                return True 
        return False 

    # quick ??? 
     def isScramble1(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        l, a, b, c = len(s1), [], [], []
        for i in range(1, l):
            bisect.insort(a, s1[i - 1])
            bisect.insort(b, s2[-i])
            bisect.insort(c, s2[i - 1])
            if a == b and self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[0:-i]):
                return True
            elif a == c and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
        return False