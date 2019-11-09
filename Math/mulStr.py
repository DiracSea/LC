class Solution:
    def multiply(self, a: str, b: str) -> str:
        if a == '0' or b == '0': 
            return '0' 
        def add(ans, num): 
            carry = 0 
            m = max(len(ans), len(num)) 
            res = ''
            for i in range(m): 
                c = int(ans[i]) if i < len(ans) else 0 
                d = int(num[i]) if i < len(num) else 0
                plus = c + d + carry
                if plus > 9: 
                    carry = 1 
                    cur = str(plus-10)
                else: 
                    carry = 0 
                    cur = str(plus) 
                res += cur
            if carry: 
                res += '1'
                
            return res
        
        ans = '0'
        if len(a) > len(b): 
            a, b = b[::-1], a[::-1] 
        else: 
            a, b = a[::-1], b[::-1] 
        
        for i in range(len(a)): 
            s = ''
            carry = 0
            for j in range(len(b)): 
                mul = int(a[i])*int(b[j]) + carry 
                carry = mul//10 
                cur = mul - carry*10 
                s += str(cur)
            if carry: 
                s += str(carry)
            print(s)
            ans = add(ans, '0'*i + s) 
        return ans[::-1]

    def multiply1(self, a: str, b: str) -> str:
        return str(int(a)*int(b))

    ## best one 
    def multiply2(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0': return '0'
        anw = [0]*(len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):      
                mul = int(num1[i]) * int(num2[j]) + anw[i+j+1]
                anw[i+j+1] = mul%10
                anw[i+j] += mul//10
        return ''.join(str(i) for i in anw).lstrip('0')