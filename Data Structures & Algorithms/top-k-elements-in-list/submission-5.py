class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frq = [[] for i in range(len(nums) + 1)]
        for i, n in enumerate(nums):
            count[n] = 1 + count.get(n, 0)
        for n, i in count.items():
            frq[i].append(n)
        res = []
        for i in range(len(frq) - 1, -1, -1):
            for n in frq[i]:
                res.append(n)
            if len(res) == k:
                return res