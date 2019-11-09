class Solution:
    def fullJustify(self, words, maxWidth: int):
        res, cur, num = [], [], 0 
        for w in words: 
            if num + len(w) + len(cur) > maxWidth: 
                for i in range(maxWidth - num): 
                    cur[i%(len(cur)-1 or 1)] += ' ' # add space into word # a cur is a line 
                res.append(''.join(cur)) # finish one line 
                cur, num = [], 0 
            cur += [w] 
            num += len(w) 
        return res + [' '.join(cur).ljust(maxWidth)]
    