class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while r - l > 1:
            m = (l + r)//2
            if target < nums[m]:
                r = m
            elif target >= nums[m]:
                l = m
        
        return l if nums[l] == target else -1