class Solution:
    inf = float('inf')

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        dist = [Solution.inf]*n

        min_cost = 0

        dist[0] = 0
        curr = 0
        for _ in range(n-1):
            print(curr, min_cost)
            visited[curr] = True
            cx, cy = points[curr]

            next_point = None
            next_dist = Solution.inf
            for neighbor in range(n):
                if visited[neighbor]:
                    continue
                
                nx, ny = points[neighbor]
                n_dist = abs(nx - cx) + abs(ny - cy)

                if n_dist < dist[neighbor]:
                    dist[neighbor] = n_dist
                
                if dist[neighbor] < next_dist:
                    next_point = neighbor
                    next_dist = dist[neighbor]
            
            curr = next_point
            min_cost += next_dist
        print(curr, min_cost)

        return min_cost 



