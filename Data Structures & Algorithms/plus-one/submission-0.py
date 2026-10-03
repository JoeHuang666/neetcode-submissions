class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dLen = len(digits)
        num = 0
        for i in range(dLen):
            num += digits[i] * (10 ** (dLen - 1))
            dLen -= 1
        return [s for s in str(num + 1)]