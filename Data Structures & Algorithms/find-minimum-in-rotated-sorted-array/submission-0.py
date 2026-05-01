class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        first = nums[0]

        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > first:
                l = m
            else:
                r = m
        
        return min(nums[l], nums[r%len(nums)])
        