class Solution: 
    # brute force Omn
    def compare(self, A, B): 
        A_str = A.split(',') 
        B_str = B.split(',') 
        A_len = len(A_str) 
        B_len = len(B_str) 

        res = [] 
        for b in B_str: 
            sum = 0
            for a in A_str: 
                if a.count(min(a)) < b.count(min(b)): 
                    sum += 1 
            res.append(sum) 
        return res 

    # O(m+n) 
    def compare1(self, A, B): 
        A_str = A.split(',') 
        B_str = B.split(',') 
        freq = [0 for i in range(10)]

        for a in A_str: 
            min_word_freq = a.count(min(a)) 
            freq[min_word_freq] += 1 

        ans = [] 
        for b in B_str: 
            min_word_freq = b.count(min(b)) 
            compare_res = sum(freq[0:min_word_freq])
            ans.append(compare_res)

        return ans


