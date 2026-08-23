class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxlen = 0
        l = 0
        for r in range(len(s)):
            if s[r] in dic:
                l = max(l, dic[s[r]] + 1) #如果出現重複的字母就把左指標移到該字母出現的地方的右邊
            dic[s[r]] = r #紀錄字母最後一次出現的位置
            maxlen = max(maxlen, r - l + 1) #防止左指標往回跑

        return maxlen