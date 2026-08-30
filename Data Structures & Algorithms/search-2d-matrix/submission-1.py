class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m//col][m%col] < target:
                l = m + 1
            elif matrix[m//col][m%col] > target:
                r = m - 1
            else:
                return True
        return False