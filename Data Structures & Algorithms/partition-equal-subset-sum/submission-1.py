class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for n in nums:
            newdp = set()
            for t in dp:
                if t + n == target:
                    return True
                newdp.add(n + t)
                newdp.add(t)
            dp = newdp
        return False