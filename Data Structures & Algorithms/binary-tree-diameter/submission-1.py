# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = {None: 0}
        stack = [root]
        diameter = 0
        while stack:
            curr = stack[-1]
            if curr.left in depth and curr.right in depth:
                left_depth = depth[curr.left]
                right_depth = depth[curr.right] 
                diameter = max(diameter, left_depth + right_depth)
                depth[curr] = 1 + max(left_depth, right_depth)
                stack.pop()
            else:
                if curr.left is not None:
                    stack.append(curr.left)
                if curr.right is not None:
                    stack.append(curr.right)
        return diameter