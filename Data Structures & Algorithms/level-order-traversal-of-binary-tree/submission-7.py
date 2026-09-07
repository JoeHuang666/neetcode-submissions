# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        res = []
        while stack:
            tmp = []
            for i in range(len(stack)):
                if stack[i]:
                    tmp.append(stack[i].val)
            if tmp:
                res.append(tmp)

            for _ in range(len(stack)):
                pop = stack.pop(0)
                if pop:
                    stack.append(pop.left)
                    stack.append(pop.right)
        return res