class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        res = []
        board = [["."] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or c + r in posDiag or r - c in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(c + r)
                negDiag.add(r - c)
                board[r][c] = "Q" #important
                
                backtracking(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtracking(0)
        return res
