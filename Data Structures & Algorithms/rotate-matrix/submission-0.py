class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix) // 2): # reverse the rows
            for c in range(len(matrix[0])):
                matrix[r][c], matrix[len(matrix) - 1 - r][c] = matrix[len(matrix) - 1 - r][c], matrix[r][c]

        for r in range(len(matrix)): # transpose
            for c in range(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]