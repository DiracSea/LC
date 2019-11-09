class Solution:
    def jump(self, nums) -> int: 
        step, reach, tail = 0, 0, 0 
        
        for i, j in enumerate(nums[:-1]): 
            reach = max(reach, i + j) # greedy 
            
            if i == tail: # record the path 
                step += 1 
                tail = reach # record the nodes
                
        return step   