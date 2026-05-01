import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_k = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.max_k)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_k, val)
        if len(self.max_k) > self.k:
            heapq.heappop(self.max_k)
        return self.max_k[0]
        
