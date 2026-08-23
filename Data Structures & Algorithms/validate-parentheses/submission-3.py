class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for c in s:
            if c in dic: # 檢查c是否屬於這個dict的key
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False