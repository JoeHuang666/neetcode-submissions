class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hs = {}
        for r in board:
            for i in range(1, 10, 1):
                hs[str(i)] = 0
            for s in r:
                if s != ".":
                    hs[s] += 1
            for k, v in hs.items():
                if v >= 2:
                    return False
        
        hs = {}
        for i in range(0, 9, 1):
            for j in range(1, 10, 1):
                hs[str(j)] = 0
            for k in range(0, 9, 1):
                if board[k][i] != ".":
                    hs[board[k][i]] += 1
            for n, m in hs.items():
                if m >= 2:
                    return False
        
        hs = {}
        l, r = 0, 2
        for _ in range(3):
            u, d = 0, 2
            for n in range(3):
                for i in range(1, 10, 1):
                    hs[str(i)] = 0
                for k in range(l, r + 1, 1):
                    for m in range(u, d + 1, 1):
                        if board[m][k] != ".":
                            hs[board[m][k]] += 1
                for k, v in hs.items():
                    if v >= 2:
                        return False
                u += 3
                d += 3
            l += 3
            r += 3
        
        return True
