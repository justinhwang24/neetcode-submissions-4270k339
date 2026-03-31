class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            m = (left + right) // 2
            r = m // len(matrix[0])
            c = m % len(matrix[0])
            if matrix[r][c] < target:
                left = m + 1
            elif matrix[r][c] > target:
                right = m - 1
            else:
                return True
        return False