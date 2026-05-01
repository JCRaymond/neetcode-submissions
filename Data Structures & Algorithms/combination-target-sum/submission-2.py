class Solution:
    def combinationSum(self, nums: List[int], target: int, nums_sorted=False) -> List[List[int]]:
        if not nums_sorted:
            nums.sort()
        combos = []
        for i, num in enumerate(nums):
            if target == num:
                combos.append([num])
            elif target-num > 0:
                combos.extend([[num, *combo] for combo in self.combinationSum(nums[i:], target-num, True)])
            else:
                break

        return combos