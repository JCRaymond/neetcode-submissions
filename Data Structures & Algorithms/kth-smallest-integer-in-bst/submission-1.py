# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sizes = {None: 0}
        stack = [root]
        while stack:
            curr = stack[-1]
            if curr.left in sizes and curr.right in sizes:
                stack.pop()
                sizes[curr] = 1 + sizes[curr.left] + sizes[curr.right]
            else:
                if curr.left is not None:
                    stack.append(curr.left)
                if curr.right is not None:
                    stack.append(curr.right)
        
        curr = root
        idx = sizes[root.left] + 1
        while idx != k:
            if k < idx:
                curr = curr.left
                idx -= sizes[curr.right] + 1
            else:
                curr = curr.right
                idx += sizes[curr.left] + 1
        
        return curr.val