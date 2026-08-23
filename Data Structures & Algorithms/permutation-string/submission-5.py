class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        dic_s1 = {}
        for _ in range(26): dic_s1[_] = 0
        for _ in s1: dic_s1[ord(_) - ord("a")] += 1
        dic_s2 = {}
        for _ in range(26): dic_s2[_] = 0
        for _ in range(r + 1): dic_s2[ord(s2[_]) - ord("a")] += 1

        while r < len(s2) - 1:
            if dic_s1 == dic_s2:
                return True
            dic_s2[ord(s2[l]) - ord("a")] -= 1
            r += 1
            l += 1
            dic_s2[ord(s2[r]) - ord("a")] += 1

        if dic_s1 == dic_s2:
                return True

        return False
            