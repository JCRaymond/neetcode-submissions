import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small) > 0 and num <= self.small[0]:
            heapq.heappush_max(self.small, num)
            if len(self.small) > len(self.big):
                val = heapq.heappop_max(self.small)
                heapq.heappush(self.big, val)
        else:
            heapq.heappush(self.big, num)
            if len(self.big) > len(self.small) + 1:
                val = heapq.heappop(self.big)
                heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (self.small[0] + self.big[0])/2
        return self.big[0] 
        
        