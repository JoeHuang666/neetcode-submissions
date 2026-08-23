class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstr = "".join(filter(str.isalnum, s))
        cleanstr = cleanstr.lower()
        if not cleanstr:
            return True
        if len(cleanstr) % 2 == 0:
            mid = len(cleanstr) // 2
            l, r = mid - 1, mid
            while cleanstr[l] == cleanstr[r]:
                l -= 1
                r += 1
                if l == -1:
                    return True
            return False

        if len(cleanstr) % 2 == 1:
            mid = len(cleanstr) // 2
            l, r = mid, mid
            while cleanstr[l] == cleanstr[r]:
                l -= 1
                r += 1
                if l == -1:
                    return True
            return False