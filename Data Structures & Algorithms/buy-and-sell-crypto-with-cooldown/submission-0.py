class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for i in range(len(prices) + 1)] #0:holding stock , 1: can buy stock, dp[i][j]: max profit in time i at state j
        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][0] - prices[i] if i + 1 < len(prices) else -prices[i]
                    cooldown = dp[i + 1][1] if i + 1 < len(prices) else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][1] + prices[i] if i + 2 < len(prices) else prices[i]
                    cooldown = dp[i + 1][0] if i + 1 < len(prices) else 0
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]