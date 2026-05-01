import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        oA = ord('A')
        task_freqs = [0]*26
        for task in tasks:
            task_freqs[ord(task)-oA] += 1
        task_queue = []
        for task, freq in enumerate(task_freqs):
            if freq > 0:
                heapq.heappush_max(task_queue, (freq, task))

        time = 0
        cooldown = deque()
        while task_queue or cooldown:
            if task_queue:
                freq, task = heapq.heappop_max(task_queue)
                if freq > 1:
                    cooldown.append((time + n, freq-1, task))
            if cooldown:
                if cooldown[0][0] == time:
                    _, freq, task = cooldown.popleft()
                    heapq.heappush_max(task_queue, (freq, task))
            time += 1
        
        return time
                

        
