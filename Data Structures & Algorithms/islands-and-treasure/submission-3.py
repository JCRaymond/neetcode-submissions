from collections import deque

class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        seen = [[False]*m for _ in range(n)]

        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen[r][c] == True

        while q:
            curr_r, curr_c = q.popleft()
            curr_val = grid[curr_r][curr_c]

            for dr, dc in Solution.deltas:
                nr = curr_r + dr
                nc = curr_c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if grid[nr][nc] == -1 or seen[nr][nc]:
                    continue
                seen[nr][nc] = True
                if grid[nr][nc] <= curr_val + 1:
                    continue
                grid[nr][nc] = curr_val + 1
                q.append((nr,nc))
                    