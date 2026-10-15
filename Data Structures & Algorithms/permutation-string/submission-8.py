class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        list_s1 = [0] * 26
        for _ in range(len(s1)): list_s1[ord(s1[_]) - ord("a")] += 1
        list_s2 = [0] * 26
        for _ in range(len(s1)): list_s2[ord(s2[_]) - ord("a")] += 1
        l, r = 0, len(s1) - 1

        while r < len(s2) - 1:
            if list_s1 == list_s2:
                return True
            list_s2[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            list_s2[ord(s2[r]) - ord("a")] += 1
        if list_s1 == list_s2:
            return True
        return False