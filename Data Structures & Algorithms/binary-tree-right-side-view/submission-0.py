# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        result = []
        q.append(root)
        q.append(None)
        curr = root
        while q:
            last = curr
            curr = q.popleft()
            if curr is None:
                result.append(last.val)
                if q:
                    q.append(None)
                continue
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return result