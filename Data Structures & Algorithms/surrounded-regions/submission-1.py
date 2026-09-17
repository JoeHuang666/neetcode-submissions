class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c, visit):
            if ((r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or board[r][c] == "X"):
                return
            visit.add((r, c))
            board[r][c] = "Z"
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

        for r in range(rows):
            if board[r][0] == "O" and (r, 0) not in visit:
                dfs(r, 0, visit)
            if board[r][cols - 1] == "O" and (r, cols - 1) not in visit:
                dfs(r, cols - 1, visit)
        
        for c in range(cols):
            if board[0][c] == "O" and (0, c) not in visit:
                dfs(0, c, visit)
            if board[rows - 1][c] == "O" and (rows - 1, c) not in visit:
                dfs(rows - 1, c, visit)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Z":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"