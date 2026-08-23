class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = list(strs[0])
        for word in strs[1:]:
            while lcp and not word.startswith("".join(lcp)):
                lcp.pop()
        if lcp:
            ans = "".join(lcp)
            return ans
        else:
            return ""