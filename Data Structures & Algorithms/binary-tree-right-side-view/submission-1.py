# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []

        while stack:
            tmp = 101
            for i in range(len(stack)):
                pop = stack.pop(0)
                if pop:
                    tmp = pop.val
                    stack.append(pop.left)
                    stack.append(pop.right)
            if tmp != 101:
                res.append(tmp)
        
        return res
            