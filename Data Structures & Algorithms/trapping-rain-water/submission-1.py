class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]
        res = 0
        while l < r:
            if maxleft <= maxright:
                res += maxleft - height[l]
                l += 1
                maxleft = max(maxleft, height[l])
            else:
                res += maxright - height[r]
                r -= 1
                maxright = max(maxright, height[r])
        return res