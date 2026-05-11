"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_copies = {}
        node_copies[node] = Node(node.val)

        stack = [node]
        while stack:
            curr = stack.pop()
            curr_copy = node_copies[curr]
            for neighbor in curr.neighbors:
                if neighbor not in node_copies:
                    node_copies[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                curr_copy.neighbors.append(node_copies[neighbor])
        
        return node_copies[node]
