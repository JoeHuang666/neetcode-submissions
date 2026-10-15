class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        dic = {}
        for r in range(len(s)):
            if s[r] in dic:
                l = max(l, dic[s[r]] + 1)
            dic[s[r]] = r
            maxl = max(maxl, r - l + 1)
        return maxl