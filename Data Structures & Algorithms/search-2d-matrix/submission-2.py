class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r = 0
        c = len(matrix[0]) - 1
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            val = matrix[r][c]
            if val < target:
                r += 1
            elif val > target:
                c -= 1
            else:
                return True
        return False