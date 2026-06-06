class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        max_profit = [[0,0] for _ in range(n)]

        max_profit[-1][1] = nums[-1]

        for house in range(n-2, -1, -1):
            max_profit[house][0] = max(max_profit[house+1][0], max_profit[house+1][1])
            max_profit[house][1] = nums[house] + max_profit[house+1][0]
        
        return max(max_profit[0][0], max_profit[0][1])