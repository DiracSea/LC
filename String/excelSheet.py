class Solution:
    def convertToTitle(self, n: int) -> str:
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))

    def convertToTitle1(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26]) # from small to large 
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)