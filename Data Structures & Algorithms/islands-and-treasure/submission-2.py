from collections import deque

class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        seen = [[0]*m for _ in range(n)]

        chests_visited = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    continue
                
                chests_visited += 1
                seen[r][c] == chests_visited

                q = deque()
                q.append((r,c))
                while q:
                    curr_r, curr_c = q.popleft()
                    curr_val = grid[curr_r][curr_c]

                    for dr, dc in Solution.deltas:
                        nr = curr_r + dr
                        nc = curr_c + dc
                        if nr < 0 or nr >= n or nc < 0 or nc >= m:
                            continue
                        if grid[nr][nc] == -1 or seen[nr][nc] == chests_visited:
                            continue
                        seen[nr][nc] = chests_visited
                        if grid[nr][nc] <= curr_val + 1:
                            continue
                        grid[nr][nc] = curr_val + 1
                        q.append((nr,nc))
                    