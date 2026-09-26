class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0 for a in range(amount + 1)] for i in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                if a - coins[i] >= 0:
                    dp[i][a] = dp[i][a - coins[i]]
                    dp[i][a] += dp[i + 1][a]
        
        return dp[0][amount]