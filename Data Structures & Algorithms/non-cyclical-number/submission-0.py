class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            ans = 0
            for s in str(n):
                ans += int(s)*int(s)
            return ans
        slow, fast = happy(n), happy(happy(n))
        while fast != 1:
            if slow == fast:
                return False
            slow = happy(slow)
            fast = happy(happy(fast))
        return True