class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        results = []
        cleaned_nums = set(nums)
        if len(cleaned_nums) == 0: return 0

        for n in cleaned_nums:
            if n - 1 in cleaned_nums:
                continue

            c = 1
            while n+1 in cleaned_nums:
                n += 1
                c += 1

            results.append(c)

        return max(results)