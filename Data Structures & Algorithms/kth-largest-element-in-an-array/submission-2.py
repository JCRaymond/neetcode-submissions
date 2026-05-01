class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        
        s = 0
        e = len(nums)-1
        while s < e:
            pivot = nums[e]

            l = s
            r = e
            while l < r:
                while l < r and nums[l] > pivot:
                    l += 1
                while l < r and nums[r] <= pivot:
                    r -= 1
                
                nums[l], nums[r] = nums[r], nums[l]
            
            pivot_idx = l
            nums[pivot_idx], nums[e] = nums[e], nums[pivot_idx]
            if pivot_idx == k-1:
                return pivot
            elif k <= pivot_idx:
                e = pivot_idx - 1
            else:
                s = pivot_idx + 1

        return nums[s]