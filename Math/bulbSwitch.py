class Solution:
    # TLE
    def bulbSwitch(self, n: int) -> int:
        bulb = [True]*n 
        for i in range(1, n): 
            for j in range(i, n, i+1): 
                bulb[j] = not bulb[j] 
        # bulb[0] = True
        return sum(bulb)

    def bulbSwitch1(self, n: int) -> int:
        # bulb i ends up on if and only if i is a square 
        # 1 4 9
        # 12 = 1*12 2*6 3*4 pairs
        # 9 = 1*9 3 odd 
        # factors is odd -> on
        # factors is even -> off 
        return int(__import__('math').sqrt(n))

    def bulbSwitch2(self, n: int) -> int:
        # factors is odd -> on
        # factors is even -> off 
        c = 0 
        i = 1 
        while i*i <= n: 
            i += 1 
            c += 1 
        return c 