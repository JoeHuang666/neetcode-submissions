# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "n"
        res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                res.append("n")
            else:
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "n":
            return None
        root = TreeNode(int(vals[0]))
        stack = [root]
        index = 1
        while stack:
            node = stack.pop(0)
            if vals[index] != "n":
                node.left = TreeNode(int(vals[index]))
                stack.append(node.left)
            index += 1
            if vals[index] != "n":
                node.right = TreeNode(int(vals[index]))
                stack.append(node.right)
            index += 1
        return root