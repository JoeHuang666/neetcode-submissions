class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #(index, temp)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                ind, tem = stack.pop()
                res[ind] = i - ind
            stack.append([i, t])
        return res