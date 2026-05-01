class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, num in enumerate(nums):
            if num in need:
                return [need[num], i]
            need[target-num] = i