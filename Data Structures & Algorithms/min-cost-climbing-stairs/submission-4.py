class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2], cost[-1]
        res = 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        if len(cost) == 3:
            return min(cost[0] + cost[2], cost[1])
        for i in range(len(cost) - 3, -1, -1):
            tmp = one
            one = min(cost[i] + one, cost[i] + two)
            two = tmp
            if i == 1:
                res = one
            if i == 0:
                res = min(res, one)
        return res