class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)
        stones.append(0) # 如果最後兩顆石頭等重的話heap會變空的 所以加上0 又因為最後回傳第零個元素 所以這只會對上述的情況有影響
        return abs(stones[0])