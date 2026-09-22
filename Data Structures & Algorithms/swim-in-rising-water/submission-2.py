class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        minHeap = [[grid[0][0], 0, 0]] # time, r, c
        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return t
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visit or nr == rows or nc == cols or nr < 0 or nc < 0:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])
            