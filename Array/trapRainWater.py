class Solution:
    def trap(self, height) -> int: 
        # two pointers 
        '''
        Search from left to right and maintain a max height 
        of left and right separately, which is like a one-side 
        wall of partial container. Fix the higher one and flow 
        water from the lower part. 
        '''
        n = len(height) 
        left, left_max = 0, 0 
        right, right_max = n - 1, 0 
        rest = 0 
        while left <= right: 
            if height[left] <= height[right]: # 
                if height[left] >= left_max: 
                    left_max = height[left] 
                else: 
                    rest += left_max - height[left] 
                left += 1 
            
            else: 
                if height[right] >= right_max: 
                    right_max = height[right] 
                else: 
                    rest += right_max - height[right] 
                right -= 1
        return rest 
                    
        
                