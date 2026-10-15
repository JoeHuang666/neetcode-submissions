class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = {}
        l = 0
        maxl, maxf = 0, 0
        for r in range(len(s)):
            res[s[r]] = 1 + res.get(s[r], 0)
            maxf = max(maxf, res[s[r]])
            while r - l + 1 - maxf > k:
                res[s[l]] -= 1
                l += 1
            maxl = max(maxl, r - l + 1)
        return maxl