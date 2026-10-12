class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s))
        clean = clean.lower()

        if len(clean) % 2: # odd
            mid = len(clean) // 2
            i = 1
            while (mid - i) != -1:
                if clean[mid - i] != clean[mid + i]:
                    return False
                i += 1
            return True
        else: # even
            mid1, mid2 = ((len(clean) // 2) - 1), len(clean) // 2
            i = 0
            while (mid1 - i) != -1:
                if clean[mid1 - i] != clean[mid2 + i]:
                    return False
                i += 1
            return True