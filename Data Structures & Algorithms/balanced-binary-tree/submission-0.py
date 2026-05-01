# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        depth = {None: 0}
        stack = [root]
        while stack:
            curr = stack[-1]
            if curr.left in depth and curr.right in depth:
                stack.pop()
                left_depth = depth[curr.left]
                right_depth = depth[curr.right]
                depth[curr] = 1 + max(left_depth, right_depth)
                if abs(left_depth - right_depth) > 1:
                    return False
            else:
                if curr.left is not None:
                    stack.append(curr.left)
                if curr.right is not None:
                    stack.append(curr.right)
        
        return True