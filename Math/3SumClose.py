class Solution:
    def threeSumClosest(self, num, target: int) -> int:
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            l, r = i+1, len(num) - 1
            while l < r:
                sum = num[i] + num[l] + num[r]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
            
        return result

    # optimization
    def threeSumClosest1(self, nums, target):
        nums.sort()
        res = nums[0]+nums[1]+nums[2]

        diff = target - res if target > res else res - target
        
        
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i+1, len(nums)-1

            largest = nums[i] + nums[r-1] + nums[r]
            smallest = nums[i] + nums[l] + nums[l+1]

            if largest <= target:
                # compare with the largest   
                if largest == target:
                    return largest

                if target - largest < diff:
                    res = largest
                    diff = target - largest
                continue

            elif smallest >= target:
                # compare with the smallest
                if smallest == target:
                    return smallest

                if smallest - target < diff:
                    res = smallest
                    diff = smallest - target
                continue

            else:
                while l < r:
                    s = nums[i] + nums[l] + nums[r]

                    if s == target:
                        return s
                    elif s < target:
                        l += 1
                        if target - s < diff:
                            res = s
                            diff = target - s
                    else:
                        r -= 1
                        if s - target < diff:
                            res = s
                            diff = s - target
        return res