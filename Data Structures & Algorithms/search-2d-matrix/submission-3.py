class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col1 = [row[0] for row in matrix]

        ct = 0
        cb = len(col1)

        while cb - ct > 1:
            m = (ct + cb) // 2
            if target < col1[m]:
                cb = m
            elif target >= col1[m]:
                ct = m

        c = ct
        row = matrix[c]

        l = 0
        r = len(row)
        while r - l > 1:
            m = (l + r) // 2
            if target < row[m]:
                r = m
            elif target >= row[m]:
                l = m
        
        return row[l] == target

        