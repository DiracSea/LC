'''
class Comparable:
    # object that can be sorted thanks to magic methods.
    def __init__(self, num):
        self.value = str(num)
    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value
    def __gt__(self, other):
        return self.value + other.value < other.value + self.value
    def __eq__(self, other):
        return self.value + other.value == other.value + self.value
'''
class LNK(str): 
    def __lt__(x, y): 
        return x + y > y + x # compare str 
    # map and sorted key
class Solution:
    def largestNumber(self, nums) -> str:
        ln = ''.join(sorted(map(str, nums), key = LNK)) # sorted key is LNK 
    
        return '0' if ln[0] == '0' else ln 

    # cmp 
    def largestNumber1(self, nums) -> str:
        num_strs = [str(num) for num in nums]
        num_strs.sort(key=cmp_to_key(lambda x, y: -1 if x + y < y + x else 1))
        print(num_strs[::-1])
        return str(int("".join(num_strs[::-1])))