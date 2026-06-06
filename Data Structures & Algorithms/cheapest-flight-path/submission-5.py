import heapq
from collections import defaultdict

class Solution:
    inf = float('inf')

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s, e, p in flights:
            graph[s][e] = p

        costs = [[Solution.inf]*(k+2) for _ in range(n)]
        costs[src][0] = 0
        
        queue = []
        heapq.heappush(queue, (0, 0, src))

        while queue:
            curr_cost, curr_steps, curr = heapq.heappop(queue)
            
            if curr == dst:
                return curr_cost

            if curr_cost > costs[curr][curr_steps]:
                continue
            
            for neighbor, price in graph[curr].items():
                new_cost = curr_cost + price
                if curr_steps <= k and new_cost < costs[neighbor][curr_steps+1]:
                    costs[neighbor][curr_steps + 1] = new_cost
                    heapq.heappush(queue, (new_cost, curr_steps + 1, neighbor))
        
        return -1
