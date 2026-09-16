class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append([r, c])
        
        time = -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visit and nr in range(rows) and nc in range(cols):
                        if grid[nr][nc] == 1:
                            visit.add((nr, nc))
                            q.append([nr, nc])
                            grid[nr][nc] = 2
            time += 1
        
        freshbanana = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshbanana = True
                    break

        if freshbanana:
            ans = -1
        elif time > -1:
            ans = time
        else:
            ans = 0

        return ans