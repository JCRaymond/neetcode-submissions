class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        stack = []

        flows_pacific = [[False]*m for _ in range(n)]
        flows_atlantic = [[False]*m for _ in range(n)]

        flows_pacific[0][m-1] = True
        flows_atlantic[0][m-1] = True
        stack.append((0,m-1))

        flows_pacific[n-1][0] = True
        flows_atlantic[n-1][0] = True
        stack.append((n-1, 0))

        flows_pacific[0][0] = True # No need to dfs from this space
        
        flows_atlantic[n-1][m-1] = True # No need to dfs from this space

        for c in range(1, m-1):
            flows_pacific[0][c] = True
            stack.append((0,c))

            flows_atlantic[n-1][c] = True
            stack.append((n-1,c))
        
        for r in range(1, n-1):
            flows_pacific[r][0] = True
            stack.append((r,0))

            flows_atlantic[r][m-1] = True
            stack.append((r,m-1))
        
        while stack:
            curr_r, curr_c = stack.pop()
            curr_height = heights[curr_r][curr_c]
            curr_flows_pacific = flows_pacific[curr_r][curr_c]
            curr_flows_atlantic = flows_atlantic[curr_r][curr_c]

            for dr, dc in Solution.deltas:
                nr = curr_r + dr
                nc = curr_c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                visit_neighbor = False
                if curr_flows_pacific and not flows_pacific[nr][nc] and heights[nr][nc] >= curr_height:
                    flows_pacific[nr][nc] = True
                    visit_neighbor = True
                if curr_flows_atlantic and not flows_atlantic[nr][nc] and heights[nr][nc] >= curr_height:
                    flows_atlantic[nr][nc] = True
                    visit_neighbor = True
                if visit_neighbor:
                    stack.append((nr, nc))
        
        results = []
        for r in range(n):
            for c in range(m):
                if flows_pacific[r][c] and flows_atlantic[r][c]:
                    results.append([r,c])

        return results
        
        
        



