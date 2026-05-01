class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        for i in range(1 << len(nums)):
            keep = bin(i)[2:]
            keep = '0'*(n-len(keep)) + keep
            subsets.append([num for num, is_in in zip(nums, keep) if is_in == '1'])
        return subsets