class Solution:
    def is_valid_to_row(self, queen_cols):
        for row, col in enumerate(queen_cols):
            for other_row in range(row):
                row_diff = row - other_row
                other_col = queen_cols[other_row]
                if other_col == col or other_col == col + row_diff or other_col == col - row_diff:
                    return row
        return len(queen_cols)

    def find_next_valid(self, n, queen_cols):
        curr_row = self.is_valid_to_row(queen_cols)
        while curr_row < n:
            queen_cols[curr_row] += 1
            while queen_cols[curr_row] == n:
                queen_cols[curr_row] = 0
                curr_row -= 1
                if curr_row < 0:
                    break
                queen_cols[curr_row] += 1
            if curr_row < 0:
                return None
            curr_row = self.is_valid_to_row(queen_cols)
        return queen_cols 

    def get_board(self, n, queen_cols):
        k = n - 1
        return ['.'*c + 'Q' + '.'*(k-c) for c in queen_cols]

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        queen_cols = [0]*n
        queen_cols = self.find_next_valid(n, queen_cols)

        result = []
        while queen_cols:
            result.append(self.get_board(n, queen_cols))
            
            incr_idx = n-1
            queen_cols[incr_idx] += 1
            while queen_cols[incr_idx] == n:
                queen_cols[incr_idx] = 0
                incr_idx -= 1
                if incr_idx < 0:
                    break
                queen_cols[incr_idx] += 1
            if incr_idx < 0:
                break
            queen_cols = self.find_next_valid(n, queen_cols)        
        return result
