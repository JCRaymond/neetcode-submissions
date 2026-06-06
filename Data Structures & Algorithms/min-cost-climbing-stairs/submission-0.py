class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost_to_top = [0]*(n+2)

        for i in range(n-1, -1, -1):
            min_cost_to_top[i] = cost[i] + min(min_cost_to_top[i+1], min_cost_to_top[i+2])
        
        return min(min_cost_to_top[0], min_cost_to_top[1])