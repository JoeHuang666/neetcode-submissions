class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, hei = stack.pop()
                maxarea = max(maxarea, (i - index) * hei)
                start = index
            stack.append([start, h])
        for i, h in stack:
            maxarea = max(maxarea, (len(heights) - i) * h)
        return maxarea