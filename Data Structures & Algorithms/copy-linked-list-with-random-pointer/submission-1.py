"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        node_clones = defaultdict(lambda: Node(0))
        node_clones[None] = None
        
        curr = head
        while curr is not None:
            node_clones[curr].val = curr.val
            node_clones[curr].next = node_clones[curr.next]
            node_clones[curr].random = node_clones[curr.random]
            curr = curr.next
        
        return node_clones[head]