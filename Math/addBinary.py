class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        if len(b) > len(a): 
            a, b = b[::-1], a[::-1]
        else: 
            a, b = a[::-1], b[::-1]
        carry = 0 
        c = ""
        for i in range(len(a)): 
            b_num = b[i] if i < len(b) else 0 
            num = int(b_num) + int(a[i]) + carry 
            cur = num%2
            carry = num//2 
            c = str(cur) + c 
        if carry: 
            c = str(carry) + c 
        return c 

    def addBinary1(self, a: str, b: str) -> str: 
        return bin(int(a,2) + int(b,2))[2:]