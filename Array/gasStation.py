class Solution:
    # Greedy Method, Step Approxiamtion
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): 
            return -1 
        start, total, Min = 0, 0, float("inf") 
        n = len(gas)
        for i in range(n): 
            total += (gas[i] - cost[i]) 
            if total < Min: 
                start = (i + 1)%n 
                Min = total
        return start

    # 1. Whenever the tank is negative, reset it and let the car start from next point.
    # 2. In the mean time, add up all of the left gas to total. 
    # 3. If it's negative finally, return -1 since it's impossible to finish.
    # 4. If it's non-negative, return the last point saved in res;
    def canCompleteCircuit1(self, gas, cost): 
        n = len(gas) 
        tank, res, idx = 0, 0, 0
        for i in range(n): 
            tank += gas[i] - cost[i] 
            if (tank < 0): 
                res += tank # gas acc
                tank = 0 # clear tank
                idx = i + 1 # next one may be positive
        res += tank # final gas acc
        return -1 if res < 0 else idx # if total gas less than 0 then -1 