class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        first = nums[0]

        while r - l > 1:
            m = (l + r)//2
            if first < nums[m]:
                l = m
            else:
                r = m

        print(l,r)
        
        if target >= first:
            r = l+1
            l = 0
        else:
            l = r
            r = len(nums)
        print(l,r)
        
        while r - l > 1:
            m = (l + r)//2
            if target < nums[m]:
                r = m
            else:
                l = m
        
        return l if l < len(nums) and nums[l] == target else -1