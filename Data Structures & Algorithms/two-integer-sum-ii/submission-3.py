class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        l = 0
        r = 1

        while r < n-1 and numbers[l] + numbers[r] < target:
            r += 1

        while l < r and numbers[l] + numbers[r] != target:
            l += 1

            while l < r-1 and numbers[l] + numbers[r-1] >= target:
                r -= 1
        
        return [l+1, r+1]