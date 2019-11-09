class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # visit row 
        '''n=numRows
        Δ=2n-2    0         {2n-2}            2n-2         {2n-2}          4n-4
        Δ=        1                     2n-3  2n-1                  4n-5   4n-3
        Δ=        2               2n-4        2n                4n-6       .
        Δ=        .           .               .               .            .
        Δ=        .       n-1                 .           3n-1             .
        Δ=        n-2 n                       3n-4    3n-2                 5n-6
        Δ=2n-2    n-1                         3n-3                         5n-5
        '''
        '''
        n = numRows
        0     k(2n-2)  
        n-1   k(2n-2)+n-1 
        inner rows k(2n-2)+i; (k+1)(2n-2) - i 
        '''
        if s == None: 
            return s 
        elif numRows == 0: 
            return s 
        elif numRows == 1: 
            return s 
        rstr = "" 
        for i in range(numRows): 
            if i == 0: 
                rstr += s[::2*numRows - 2] # interval = 2n-2
            elif i == numRows - 1: 
                rstr += s[i::2*numRows - 2] # phase = n - 1 = i
            else: 
                j = i 
                flag = 1 # or counter = 0 
                while j < len(s): 
                    rstr += s[j] 
                    if flag: 
                        flag = 0
                        j += 2*(numRows - i - 1) 
                    else: 
                        flag = 1
                        j += 2*i
        return rstr 
    # distribute row 
    def convert1(self, s: str, numRows: int) -> str:
        results = [''] * numRows
        
        if numRows == 1:
            return s
        times = 2
        index = 0
        for each in s:
            results[index] = results[index] + each

            if index == numRows - 1:
                times += 1
            elif index == 0:
                times -= 1

            if times == 1: # zigzag line |/|/
                index += 1
            else:
                index -= 1

        results = ''.join(results)

        return results