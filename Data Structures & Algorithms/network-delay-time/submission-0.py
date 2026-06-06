from collections import deque, defaultdict

class Solution:
    inf = float('inf')

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)

        for u, v, t in times:
            graph[u-1][v-1] = t
        
        dist = [Solution.inf]*n
        dist[k-1] = 0
        queue = deque()
        queue.append((k-1, 0))
        while queue:
            curr, time = queue.popleft()

            if time > dist[curr]:
                continue
            
            for neighbor, weight in graph[curr].items():
                newtime = time + weight
                if newtime < dist[neighbor]:
                    dist[neighbor] = newtime
                    queue.append((neighbor, newtime))
        
        max_dist = max(dist)
        return -1 if max_dist == Solution.inf else max_dist





