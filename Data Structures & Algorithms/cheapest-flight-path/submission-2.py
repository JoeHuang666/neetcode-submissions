class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0

        for i in range(k + 1):
            tmp = price.copy()
            for s, d, c in flights: #source, destination, cost
                if price[s] == float("inf"):
                    continue
                if price[s] + c < tmp[d]:
                    tmp[d] = price[s] + c
            price = tmp
        
        return -1 if price[dst] == float("inf") else price[dst]