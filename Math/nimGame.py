class Solution:
    def canWinNim(self, n: int) -> bool:
        # 4s will lose 
        # not 4s can easily change to 4s -> win 
        return n%4 != 0 

    def canWinNim1(self, n: int) -> bool:
        # 4s will lose 
        # not 4s can easily change to 4s -> win 
        return bool(n%3) 