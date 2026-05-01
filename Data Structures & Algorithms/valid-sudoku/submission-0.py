class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_masks = [[1 << (int(c)-1) if c != '.' else 0 for c in row] for row in board]

        # Row checks
        for row_masks in board_masks:
            row_set = 0
            for mask in row_masks:
                if row_set & mask != 0:
                    return False
                row_set |= mask

        # Column checks
        for c in range(9):
            col_set = 0
            for r in range(9):
                mask = board_masks[r][c]
                if col_set & mask != 0:
                    return False
                col_set |= mask
        
        # Box checks
        for box_r in (0,3,6):
            for box_c in (0,3,6):
                box_set = 0
                for dr in (0,1,2):
                    for dc in (0,1,2):
                        mask = board_masks[box_r + dr][box_c + dc]
                        if box_set & mask != 0:
                            return False
                        box_set |= mask
        
        return True