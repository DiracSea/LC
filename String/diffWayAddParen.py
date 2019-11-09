class Solution:
    def diffWaysToCompute(self, input: str):
        # divide and conquer
        if input.isdigit():
            return [int(input)]
        memo = {} 
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(int(j), int(k), input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n