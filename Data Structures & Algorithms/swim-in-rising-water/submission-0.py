class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        s = 0
        e = n*n

        while e - s > 1:
            m = (s + e)//2

            if grid[0][0] > m:
                s = m
                continue
            
            seen = [[False]*n for _ in range(n)]
            seen[0][0] = True

            stack = [(0,0)]
            while stack:
                r, c = stack.pop()

                if r == n-1 and c == n-1:
                    break
                
                if grid[r][c] > m:
                    continue
                
                for dr, dc in Solution.deltas:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue

                    if not seen[nr][nc]:
                        seen[nr][nc] = True
                        if grid[nr][nc] <= m: 
                            stack.append((nr, nc))

            else:
                s = m
                continue
            
            e = m
        
        return e