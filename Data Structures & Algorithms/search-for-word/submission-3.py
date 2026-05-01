class Solution:
    deltas = [(0,1), (0,-1), (1,0), (-1,0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] != word[0]:
                    continue
                
                used = set(((r,c),))
                stack = [(r,c,1,used)]
                while stack:
                    r, c, i, used = stack.pop()
                    #print(r,c,i,used)
                    if i == len(word):
                        return True
                    
                    for dr, dc in Solution.deltas:
                        nr = r + dr
                        nc = c + dc
                        if not (0 <= nr < num_rows and 0 <= nc < num_cols):
                            continue
                        if (nr, nc) in used:
                            continue
                        if board[nr][nc] != word[i]:
                            continue
                        stack.append((nr, nc, i+1, used | set(((nr, nc),))))

        return False
