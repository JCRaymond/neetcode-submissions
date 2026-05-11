class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = [[False]*m for _ in range(n)]

        max_island = 0
        for r in range(n):
            for c in range(m):
                if seen[r][c]:
                    continue
                
                seen[r][c] = True

                if grid[r][c] == 0:
                    continue
                
                island_size = 0
                stack = [(r,c)]
                while stack:
                    island_size += 1
                    curr_r, curr_c = stack.pop()

                    for dr, dc in Solution.deltas:
                        nr = curr_r + dr
                        nc = curr_c + dc
                        if nr < 0 or nr >= n or nc < 0 or nc >= m:
                            continue
                        if seen[nr][nc]:
                            continue
                        seen[nr][nc] = True
                        if grid[nr][nc] == 0:
                            continue
                        stack.append((nr,nc))
                max_island = max(max_island, island_size)
                    
        return max_island