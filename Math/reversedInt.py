class Solution:
    # int 2 str 2 int 
    def reverse(self, x):
        s = (x > 0) - (x < 0) # symbol 
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31) # if r >= 2**31: 0

    def reverse1(self, x):
        s = (x > 0) - (x < 0)
        x = x*s
        # prevRev = 0 
        rev = 0 
        while x != 0: 
            rev = rev*10 + x%10 
            
            # if (rev - x%10)//10 != prevRev: # overflow 
            #    return 0
            # prevRev = rev 
            x = x//10
        return rev*s*(rev < 2**31)