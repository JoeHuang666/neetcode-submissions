class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            hs = {}
            for i in range(1, 10, 1):
                hs[str(i)] = 0
            for c in r:
                if c != ".":
                    hs[c] += 1
            for k, v in hs.items():
                if v >= 2:
                    return False

        for j in range(0, 9, 1):
            hs = {}
            for i in range(1, 10, 1):
                hs[str(i)] = 0
            for r in board:
                if r[j] != ".":
                   hs[r[j]] += 1 
            for k, v in hs.items():
                if v >= 2:
                    return False

        lp, rp = 0, 2
        for _ in range(3):
            up, dp = 0, 2
            for n in range(3):
                hs = {}
                for i in range(1, 10, 1):
                    hs[str(i)] = 0
                for j in range(lp, rp+1, 1):
                    for m in range(up, dp+1, 1):
                        if board[m][j] != ".":
                            hs[board[m][j]] += 1
                up += 3
                dp += 3
                for k, v in hs.items():
                    if v >= 2:
                        return False
            lp += 3
            rp += 3
        
        return True

