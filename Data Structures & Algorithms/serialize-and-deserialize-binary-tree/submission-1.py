# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return '#'
        if root.left is None and root.right is None:
            return str(root.val) + '#'
        ret = str(root.val) + '<' + self.serialize(root.left) + '|' + self.serialize(root.right) + '>'
        return ret
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        n = len(data)
        
        node_stack = []
        
        i = 0
        while i < len(data):
            if data[i] == '#':
                node_stack.append(None)
            elif data[i] == '|':
                left = node_stack.pop()
                node_stack[-1].left = left
            elif data[i] == '>':
                right = node_stack.pop()
                node_stack[-1].right = right
            else:
                scan = i
                while data[scan] not in '<#':
                    scan += 1
                root_val = int(data[i:scan])
                node_stack.append(TreeNode(root_val))
                i = scan
            i += 1
        
        return node_stack[-1]
            


