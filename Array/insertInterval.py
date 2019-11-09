class Solution:
    # overlapping  
    # brute force 
    def insert(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]': 
        if len(intervals) == 0: 
            return [newInterval] 
        L, R = newInterval[0], newInterval[1] 
        mergeL, mergeR = float("inf"), float("-inf")
        flag = 1 
        output = [] 
        for i in intervals: 
            if flag: 
                if i[0] > R and mergeL == float("inf"): 
                    mergeL = min(mergeL, L) 
                    mergeR = max(mergeR, R) 
                    flag = 0 
                if(i[0] > R or mergeR == intervals[-1][1]): 
                    output.append([mergeL, mergeR]) 
                    flag = 0 
            if (i[1] < L or i[0] > R): 
                output.append(i) 
            # 5 phase 
            # []{} or {}[]
            # [{ | ]}
            # [{ | }]
            # {[ | }]
            # {[ | ]} 
            else: 
                mergeL = min(mergeL, i[0]) 
                mergeL = min(mergeL, L) 
                mergeR = max(mergeR, i[1]) 
                mergeR = max(mergeR, R)
                
            '''
            elif i[0] <= L and i[1] <= R: 
                mergeL = min(mergeL, i[0]) 
                mergeR = max(mergeR, R) 
            elif i[0] >= L and i[1] <= R: 
                mergeL = min(mergeL, L) 
                mergeR = max(mergeR, R) 
            elif i[0] >= L and i[1] >= R: 
                mergeL = min(mergeL, L) 
                mergeR = max(mergeR, i[1]) 
            elif i[0] <= L and i[1] >= R: 
            ''' 
        if flag: 
            mergeL = min(mergeL, L) 
            mergeR = max(mergeR, R) 
            output.append([mergeL, mergeR])
        return output 

    # tail !!!
    def insert1(self, intervals, newInterval): 
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0]) # sort according to 1st element 
        
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
                
        return result

    # idx 
    def insert2(self, intervals, newInterval): 
        newStart, newEnd = newInterval
        idx, n, output = 0, len(intervals), []
        
        # First add everything that starts before newinterval
        while idx < n and intervals[idx][0] < newStart :
            output.append(intervals[idx])
            idx += 1 
        # Now add newInterval in its appropriate spot, either directly if no overlap with last
        # in output or merge it appropriately
        # Also output could have no element at this point 
        if not output or newStart > output[-1][1]: # no overlap
            output.append(newInterval)
        else: # There is overlap , adjust y value of last element in output
            output[-1][1] = max(output[-1][1], newEnd) 
        
        # Now go through all remaining elements in intervals, add them one by one
        # at each step checking for overlap with last in output or not 
        while idx < n:
            currentInterval = intervals[idx]
            currStart, currEnd = currentInterval 
            if currStart > output[-1][1] : # No overlap
                output.append(currentInterval)
            else: #overlap
                output[-1][1] = max(output[-1][1], currEnd)
            idx += 1 
        return output