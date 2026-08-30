class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            eattime = 0
            m = (l + r) // 2
            for banana in piles:
                eattime += banana//m if banana%m == 0 else banana//m + 1
            if eattime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res