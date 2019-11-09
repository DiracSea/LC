class UglyNum: 
    def __init__(self, maxnum): 
        self.nums = nums = [1,] 
        i2 = i3 = i5 = 0 
        
        for i in range(maxnum): 
            u = min(nums[i2]*2, nums[i3]*3, nums[i5]*5) 
            nums.append(u) 
            
            if u == nums[i2]*2: 
                i2 += 1 
            if u == nums[i3]*3: 
                i3 += 1 
            if u == nums[i5]*5: 
                i5 += 1 
                
class Solution:
    # generate all
    u = UglyNum(1690)
    def nthUglyNumber(self, n: int) -> int: 
         
        return self.u.nums[n-1]

    def nthUglyNumber1(self, n: int) -> int: 
        # generate first 
        u = [1] 
        i2 = i3 = i5 = 0
        while len(u) < n: 
            while u[i2]*2 <= u[-1]: i2 += 1 
            while u[i3]*3 <= u[-1]: i3 += 1 
            while u[i5]*5 <= u[-1]: i5 += 1 
            u.append(min(u[i2]*2, u[i3]*3, u[i5]*5)) 
        return u[-1] 




    u = sorted(2**a * 3**b * 5**c
                for a in range(32) for b in range(20) for c in range(14)) 
    def nthUglyNumber3(self, n: int) -> int: 
        # generate ugly num 
        return self.u[n-1]

    ######### TLE
    def nthUglyNumber4(self, n: int) -> int: 
        if n == 1: 
            return 1
        n -= 1 
        i = 1 
        while n: 
            i += 1
            if self.isUgly(i):    
                n -= 1 
        return i
        
    def isUgly(self, num): 
        while not num%30: 
            num /= 30 
        while not num%10: 
            num /= 10 
        while not num%15: 
            num /= 15 
            
        while not num%5: 
            num /= 5 
        while not num%3: 
            num /= 3 
        while not num%2: 
            num /= 2 
        
        if num == 1: 
            return True 
        else: 
            return False 