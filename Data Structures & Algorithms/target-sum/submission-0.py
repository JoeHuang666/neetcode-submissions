class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # 1 way to sum up for the current sum 0

        for i in range(len(nums)):
            nextdp = defaultdict(int)
            for cursum, count in dp.items():
                nextdp[cursum + nums[i]] += count
                nextdp[cursum - nums[i]] += count
            dp = nextdp
        
        return dp[target]