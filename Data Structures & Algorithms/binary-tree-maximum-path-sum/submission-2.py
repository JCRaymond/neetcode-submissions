# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _maxPathSum(self, root: Optional[TreeNode]) -> (int, int):
        if root is None:
            return -float('inf'), -float('inf')
        
        max_path_left, max_leg_left = self._maxPathSum(root.left)
        max_path_right, max_leg_right = self._maxPathSum(root.right)
        rv = root.val

        max_leg = max(rv, rv + max_leg_left, rv + max_leg_right)
        max_path = max(max_path_left, max_path_right, rv, rv + max_leg_right, max_leg_left + rv, max_leg_left + rv + max_leg_right)

        return max_path, max_leg

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self._maxPathSum(root)[0]