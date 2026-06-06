class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        n = len(nums)
        
        max_profit = [0 for _ in range(n)]

        max_profit[0] = nums[0]
        max_profit[1] = max(nums[0], nums[1])

        for house in range(2, n-1):
            max_profit[house] = max(max_profit[house-1], nums[house] + max_profit[house-2])
        best_profit = max(max_profit[-2], max_profit[-3])

        max_profit[0] = 0
        max_profit[1] = nums[1]
        for house in range(2, n):
            max_profit[house] = max(max_profit[house-1], nums[house] + max_profit[house-2])
        best_profit = max(best_profit, max_profit[-1], max_profit[-2])
    
        return best_profit