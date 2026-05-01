# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_to_root: int = None) -> int:
        if root is None:
            return 0
        max_to_root = max_to_root or root.val
        new_max = max(root.val, max_to_root)
        return int(root.val >= max_to_root) + self.goodNodes(root.left, new_max) + self.goodNodes(root.right, new_max)