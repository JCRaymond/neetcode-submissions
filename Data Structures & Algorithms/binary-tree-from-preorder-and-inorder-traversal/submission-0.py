# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {}
        for idx, val in enumerate(inorder):
            inorder_idx[val] = idx

        nodes = {}
        nodes

        stack = [(0, 0, len(inorder))]
        while stack:
            preorder_s, inorder_s, inorder_e = stack[-1]
            root_val = preorder[preorder_s]
            root_idx = inorder_idx[root_val]
            left_size = root_idx - inorder_s
            right_size = inorder_e - root_idx - 1

            left_preorder_s = preorder_s + 1
            right_preorder_s = preorder_s + 1 + left_size
            if (left_size == 0 or left_preorder_s in nodes) and (right_size == 0 or right_preorder_s in nodes):
                stack.pop()
                left = None
                if left_size >  0:
                    left = nodes[left_preorder_s]
                right = None
                if right_size > 0:
                    right = nodes[right_preorder_s]
                root = TreeNode(root_val, left, right)
                nodes[preorder_s] = root
            else:
                if left_size > 0:
                    stack.append((left_preorder_s, inorder_s, root_idx))
                if right_size > 0:
                    stack.append((right_preorder_s, root_idx+1, inorder_e))

        return nodes[0]               

