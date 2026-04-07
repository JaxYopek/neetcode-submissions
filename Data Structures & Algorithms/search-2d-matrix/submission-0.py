class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        n = len(matrix[0])
        m = len(matrix)
        c = n - 1

        while r < m  and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False