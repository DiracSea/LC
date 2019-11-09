class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # gcd 
        # if x and y are coprime,  then we can and only can reach every integer z in [0, x + y] 
        return z == 0 or x + y >= z and z%__import__('fractions').gcd(x, y) == 0 

    # double 100 
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # gcd 
        if x + y < z: 
            return False 
        if x == z or y == z or x + y == z: 
            return True 
        return z%self.gcd(x, y) == 0 
    
    def gcd(self, a, b): 
        while b != 0: 
            a, b = b, a%b 
        return a