from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        result = []
        curr_level = []
        q.append(root)
        q.append(None)
        while q:
            curr = q.popleft()
            if curr is None:
                result.append(curr_level)
                curr_level = []
                if q:
                    q.append(None)
                continue
            curr_level.append(curr.val)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return result

