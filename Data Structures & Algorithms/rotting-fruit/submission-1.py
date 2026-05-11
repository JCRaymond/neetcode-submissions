from collections import deque

class Solution:
    deltas =  ((0,1), (1,0), (0,-1), (-1,0))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = [[False]*m for _ in range(n)]

        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen[r][c] = True
                elif grid[r][c] == 0:
                    seen[r][c] = True
        
        max_curr = 2
        while q:
            curr_r, curr_c = q.popleft()
            curr_val = grid[curr_r][curr_c]
            max_curr = max(max_curr, curr_val)

            for dr, dc in Solution.deltas:
                nr = curr_r + dr
                nc = curr_c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if seen[nr][nc]:
                    continue
                seen[nr][nc] = True
                if grid[nr][nc] > curr_val + 1:
                    continue
                grid[nr][nc] = curr_val + 1
                q.append((nr, nc))
        
        return (max_curr-2) if all(all(seen_row) for seen_row in seen) else -1