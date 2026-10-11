class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frq = [[] for i in range(len(nums) + 1)]
        for i, n in enumerate(nums):
            count[n] = 1 + count.get(n, 0)
        count_key = sorted(count, key = count.get, reverse = True)
        return count_key[:k]