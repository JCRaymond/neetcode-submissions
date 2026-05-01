# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = [root]
        curr = root
        while curr.val != p.val:
            if p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            p_path.append(curr)
        
        q_path = [root]
        curr = root
        while curr.val != q.val:
            if q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            q_path.append(curr)

        max_i = min(len(p_path), len(q_path))
        i = 0
        while i+1 < max_i and p_path[i+1] == q_path[i+1]:
            i += 1
        return p_path[i]