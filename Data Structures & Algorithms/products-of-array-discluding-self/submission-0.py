class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cumu_prod = [1]*n
        rev_cumu_prod = [1]*n

        for i in range(1, n):
            cumu_prod[i] = cumu_prod[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            rev_cumu_prod[i] = rev_cumu_prod[i+1]*nums[i+1]
        
        return [a*b for a,b in zip(cumu_prod, rev_cumu_prod)]