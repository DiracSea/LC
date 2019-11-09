class Slotuin: 
   def isIsomorphic(self, s: str, t: str) -> bool:
        # map s char to t 
        d = {} 
        for i in range(0, len(s)): 
            if s[i] not in d: 
                if t[i] in d.values(): return False 
                d[s[i]] = t[i] 
            else: 
                if d[s[i]] is not t[i]: return False 
        return True 
    
    # initialized space is 256 (Since the whole ASCII size is 256, 128 also works here)
    # test cases include /'. ect
    def isIsomorphic1(self, s: str, t: str) -> bool:
        m1 = [-1]*128; m2 = [-1]*128 
        for i in range(0, len(s)): 
            if m1[ord(s[i])] is not m2[ord(t[i])]: return False 
            m1[ord(s[i])] = m2[ord(t[i])] = i  
            
        return True
    
    # one line
    def isIsomorphic2(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic3(self, s: str, t: str) -> bool:
        #s与t的字符种类的数目相同
        #用zip看两者结构是否相同
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))