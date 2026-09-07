# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, maxSofar):
            nonlocal count
            if not root:
                return 0
            if root.val >= maxSofar:
                count += 1
            maxSofar = max(root.val, maxSofar)
            dfs(root.left, maxSofar)
            dfs(root.right, maxSofar)
        dfs(root, root.val)
        return count
