class Solution:
    def maxArea(self, height) -> int:
        '''       / max{v(i, j), S(i...j-1)};  height(i) >= height(j)
        S(i..j) = |
                  \ max{v(i, j), S(i+1...j)};  height(i) < height(j)
                '''
        v_max = 0 
        l = 0 
        r = len(height) - 1 
        while l < r: 
            gap = min(height[l], height[r])
            v_max = max(v_max, gap*(r - l)) 
            while l <= r and height[l] <= gap: l+=1
            while l <= r and height[r] <= gap: r-=1
        return v_max