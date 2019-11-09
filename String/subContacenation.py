class Solution:
    # time exceeds limit but work 
    def findSubstring(self, s: str, words): 
        if not s or not words: 
            return [] 
        elif len(s) < len(words): 
            return [] 
        
        for w in set(words):  
            if w not in s:
                return [] 
        first = set(w[0] for w in words)
        length = len(words[0]) 
        d = __import__("collections").Counter(words) 
        req = len(d) 
        
        f_all = [] 
        heads = []
        # f_num = []
        
        for i in range(len(s) - len(words)*length + 1): 
            if s[i] in first: 
                heads.append(i)
        
        for i in heads: 
            f = [] 
            head = i; tail = i + length # window of a word 
            c_f = 0
            while tail <= len(s): # filtered s, remove diff words and short sentences
                # need to find all phase in "length"  
                word = s[head:tail]

                if word in words: 
                    c_f += 1 
                    f.append((head, word)) 
                    #f_num.append(head)
                    head = tail
                    tail += length 
                else: 
                    head += 1 
                    tail += 1 
                    if c_f < len(words): 
                        while c_f > 0: 
                            f = f[:-1] 
                            c_f -= 1 
                    else: 
                        c_f = 0 
            if f not in f_all: 
                f_all.append(f)
        print(f_all) 
        output = [] 
        
        for f in f_all: 
            win = {} 
            c_win = 0 
            l = r = 0 
            start = 0 
            prev = 0  
            while r < len(f):  
                w = f[r]
                if w[0] > prev + length: 
                    win = {} 
                    c_win = 0 
                    l = r 
                prev = w[0] 

                win[w[1]] = win.get(w[1],0) + 1 
                if win[w[1]] == d[w[1]]: 
                    c_win += 1 
                
                flag = w[1] 
                while l <= r and win[w[1]] > d[w[1]]: 
                    ch = f[l][1]
                    win[ch] -= 1 
                    if ch != flag and win[ch] < d[ch]: 
                        c_win -= 1 
                    l += 1 


                while l <= r and c_win == req: 
                    if f[l][0] not in output: 
                        output.append(f[l][0])
                    ch = f[l][1] 

                    win[ch] -= 1 
                    if win[ch] < d[ch]: 
                        c_win -= 1                 
                    l += 1 

                r += 1 
        return output 
        


    def findSubstring1(self, s: str, words): 
        if not s or not words: 
            return [] 
        wordBag = __import__('collections').Counter(words) # count freq of each word
        wordLen, numWords = len(words[0]), len(words) 
        totalLen, res = wordLen*numWords, [] 
        for i in range(len(s) - totalLen + 1): 
            seen = {} 
            for j in range(i, i+totalLen, wordLen): 
                curWord = s[j:j+wordLen] 
                if curWord in wordBag: 
                    seen[curWord] = seen.get(curWord, 0) + 1  
                    if seen[curWord] > wordBag[curWord]: 
                        break 
                else: 
                    break 
            if seen == wordBag: 
                res.append(i) 
        return res 
        
    def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words==[]:
            return []
        lenstr=len(s)
        lenword=len(words[0])
        lensubstr=len(words)*lenword
        times={}
        for word in words:
            if word in times:
                times[word]+=1
            else:
                times[word]=1
        ans=[]
        for i in range(min(lenword,lenstr-lensubstr+1)):
            self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
        return ans
    def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)
            