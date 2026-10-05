class CountSquares:

    def __init__(self):
        self.ptrCount = {}
        self.ptr = []

    def add(self, point: List[int]) -> None:
        self.ptrCount[tuple(point)] = 1 + self.ptrCount.get(tuple(point), 0)
        self.ptr.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point[0], point[1]
        for x, y in self.ptr:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            res += self.ptrCount.get((x, py), 0) * self.ptrCount.get((px, y), 0)
        return res
