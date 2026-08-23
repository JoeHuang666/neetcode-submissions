class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlength = 1

        if not nums:
            return 0

        for n in nums:
            if n - 1 not in numset:
                cv = n
                length = 1
                while cv + 1 in numset:
                    length += 1
                    cv += 1
                maxlength = max(maxlength, length)

        return maxlength
