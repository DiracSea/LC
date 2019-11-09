class Solution: 
    def countPrimes(self, n: int) -> int: 
        # sieve method 
        if n < 2: 
            return 0 
        isPrime = [1]*n 
        isPrime[0] = isPrime[1] = 0 
        # loop's end is i < sqrt(n) 
        for i in range(2, int(n**0.5)+1): 
            if isPrime[i]: 
                isPrime[i*i : n : i] = [0]*len(isPrime[i * i: n: i])
        return sum(isPrime)
        
    def countPrimes2(self, n: int) -> int: 
        # TLE 
        if n < 2: 
            return 0 
        c = 0 
        for i in range(2, n): 
            if self.isPrime(i): 
                # print(i) 
                c += 1 
        return c 
    def isPrime(self, n): 
        for i in range(2, n//2+1): 
            if n%i == 0: 
                return False 
        return True 