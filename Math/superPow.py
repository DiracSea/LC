class Solution:
    def superPow(self, a: int, b) -> int: 
        # Euler's extend theorem 
        # phi(1337) = phi(7)*phi(191) = 6*190 = 1140 
        '''
        a**c === 
        a**(c mod phi(m)), gcd(a, m) = 1
        a**c, gcd(a, m) != 1, c < phi(m) 
        a**(c mod phi(m) + phi(m)), gcd(a, m) != 1, c >= phi(m)
        '''
        return 0 if a%1337 == 0 else pow(a, __import__('functools').reduce(lambda x, y: (x*10+y)%1140, b) +  1140, 1337)