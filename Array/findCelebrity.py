
class Solution:
# method and example
    MATRIX = [[ 0, 0, 1, 0], [ 0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]

    def knows(self, a: int, b: int) -> bool:
        res = False
        if (Solution.MATRIX[a][b] == 1):
            res = True 
        return res

    # recursion not found
    # def findCelebrity(self, n):
    #     if self.knows(n, self.findCelebrity(n-1)) and ~self.knows(self.findCelebrity(n-1), n):
    #         return self.findCelebrity(n-1)
    #     else:
    #         return -1

    # two pointers
    def findCelebrity1(self, n: int) -> int:
        # two pointers from two ends
        a = 0; b = n - 1

        # keep moving util meet
        while a < b: 
            if self.knows(a, b): 
                a+=1
            else: 
                b-=1
        # last a is the candidate 

        for i in range(0,n): 
            if i != a and (self.knows(a,i) or not self.knows(i,a)): 
                return -1 
        return a 