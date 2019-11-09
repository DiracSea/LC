class Solution:
    def palindromePairs(self, words):
        # TLE
        head = []
        tail = [] 
        pair = []
        for w in words: 
            if w: 
                head.append(w[0])
                tail.append(w[-1])
            else: 
                head.append(w)
                tail.append(w)
            
        def palin(s): 
            return s == s[::-1]
        
        for i, h in enumerate(head): 
            for j, t in enumerate(tail): 
                
                if (h == t or not h or not t) and i != j: 
                    if palin(words[i]+words[j]): 
                        pair.append([i, j])
                    
        return pair 
    def palindromePairs1(self, words):
        # dict 
        d = dict([(w[::-1], i) for i, w in enumerate(words)]) # reverse word dict 
        res = [] 
        for i, w in enumerate(words): 
            for j in range(len(w)+1): 
                pre, post = w[:j], w[j:] # divide 
                if pre in d and i != d[pre] and post == post[::-1]: # find another half , post is palin
                    res.append([i, d[pre]])
                if j > 0 and post in d and i != d[post] and pre == pre[::-1]: # if j == 0, repeated 
                    res.append([d[post], i]) 
        return res 