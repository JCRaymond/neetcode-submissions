class Solution:
    deltas = ((0,1), (1,0), (0,-1), (-1,0))

    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        unsurrounded = [[False]*m for _ in  range(n)]
        stack = []

        for r, c in ((0,0), (0,m-1), (n-1,0), (n-1, m-1)):
            if board[r][c] == 'O':
                unsurrounded[r][c] = True
                stack.append((r,c))
        for r in range(1, n-1):
            if board[r][0] == 'O':
                unsurrounded[r][0] = True
                stack.append((r,0))
            if board[r][m-1] == 'O':
                unsurrounded[r][m-1] = True
                stack.append((r,m-1))
        for c in range(1, m-1):
            if board[0][c] == 'O':
                unsurrounded[0][c] = True
                stack.append((0,c))
            if board[n-1][c] == 'O':
                unsurrounded[n-1][c] = True
                stack.append((n-1,c))
        
        while stack:
            curr_r, curr_c = stack.pop()

            for dr, dc in Solution.deltas:
                nr = curr_r + dr
                nc = curr_c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                if unsurrounded[nr][nc] or board[nr][nc] == 'X':
                    continue
                
                unsurrounded[nr][nc] = True
                stack.append((nr, nc))
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and not unsurrounded[r][c]:
                    board[r][c] = 'X'
        
        
