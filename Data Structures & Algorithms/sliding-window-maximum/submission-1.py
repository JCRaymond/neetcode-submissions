import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        n = len(nums)

        for i in range(k):
            heapq.heappush_max(maxheap, (nums[i], i))

        window_maxes = [maxheap[0][0]]
        
        for r in range(k, n):
            l = r - k + 1
            heapq.heappush_max(maxheap, (nums[r], r))

            while maxheap[0][1] < l:
                heapq.heappop_max(maxheap)
            
            window_maxes.append(maxheap[0][0])
        
        return window_maxes

