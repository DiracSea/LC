class Solution:
    def threeSum(self, num):
        output = [] 
        n = len(num) 
        num = sorted(num) # use sort to eliminate dup combo 
        
        for i in range(n - 2): 
            if num[i] > 0: break # smallest element is positive 
            if i > 0 and num[i] == num[i - 1]: continue # skip dup element 
            
            l, r = i + 1, n - 1 
            
            while l < r: # iterate all combo
                total = num[i] + num[l] + num[r] 
                
                if total < 0: 
                    l += 1 
                elif total > 0: 
                    r -= 1 
                else: 
                    output.append([num[i], num[l], num[r]]) 
                    while l < r and num[l] == num[l+1]: 
                        l += 1 
                    while l < r and num[r] == num[r-1]: 
                        r -= 1
                    l += 1 
                    r -= 1 
        return output 