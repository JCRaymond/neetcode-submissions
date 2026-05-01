class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        for i, num in enumerate(nums):
            if target == num:
                combos.append([num])
            if target-num > 0:
                combos.extend([[num, *combo] for combo in self.combinationSum(nums[i:], target-num)])

        return combos