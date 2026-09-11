class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= row or c >= col or board[r][c] == "#" or board[r][c] != word[i]):
                return False
            
            board[r][c] = "#" # If arrive here, means board[r][c] == word[i]
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
