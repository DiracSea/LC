class Solution: 
    # overlapping 
    def merge(self, intervals):
        output = [] 
        intervals.sort(key=lambda x: x[0])
        for i in intervals: 
            if not output: 
                output.append(i) 
                
            elif output[-1][1] >= i[0]: 
                output[-1][1] = max(output[-1][1], i[1]) 
            else: 
                output.append(i) 
        return output 


    def merge1(self, intervals):
        
        (lastStart, lastEnd) = (None, None)
        
        intervals.sort()
        
        result = []
        
        for (start, end) in intervals:
            
            if(lastStart is None and lastEnd is None):
                lastStart, lastEnd = start, end
            
            if(start <= lastEnd): # merge the two intervals
                lastEnd = max(lastEnd, end)
            else: # otherwise
                result.append((lastStart, lastEnd))
                lastStart, lastEnd = (start, end)
        
        if(lastStart is None and lastEnd is None):
            return result
        
        result.append((lastStart, lastEnd))
        return result