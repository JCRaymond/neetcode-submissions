class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)

        triples = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n-1
            while j < k:
                threesum = a + nums[j] + nums[k]
                if threesum < 0:
                    j += 1
                elif threesum > 0:
                    k -= 1
                else:
                    triples.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j <  k and nums[k] == nums[k+1]:
                        k -= 1
            
        return triples
