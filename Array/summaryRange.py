class Solution:
    def summaryRanges(self, A):
        n = len(A) 
        if n == 0: return [] 
        elif n == 1: return [str(A[0])]
        output = [] 
        flag = 0
        head = tail = A[0] 
        s1 = s2 = str(A[0])
        for i in range(1, n): 
            if A[i] == tail + 1: 
                tail = A[i] 
            else: 
                head = tail = A[i] 
                if flag == 1: 
                    output.append(s1) 
                elif flag == 2: 
                    output.append(s2)
                else: 
                    output.append(s1)
                
            if head == tail: 
                s1 = str(head) 
                flag = 1 
            else: 
                s2 = str(head)+'->'+str(tail)
                flag = 2 
        if flag == 1: 
            output.append(s1) 
        elif flag == 2: 
            output.append(s2)
        return output 

    def summaryRanges1(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
        
    def summaryRanges2(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]