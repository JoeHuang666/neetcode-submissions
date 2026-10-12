class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        maxlength = 1

        if not nums:
            return 0
        
        for n in nums:
            if n - 1 in num:
                continue
            length = 0
            while n + length in num:
                length += 1
            maxlength = max(maxlength, length)

        return maxlength