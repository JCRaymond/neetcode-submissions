"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        node_clones = {}
        node_clones[None] = None

        curr = head
        while curr is not None:
            node_clones[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        new_head = node_clones[head]
        new_curr = new_head
        while curr is not None:
            new_curr.next = node_clones[curr.next]
            new_curr.random = node_clones[curr.random]
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head