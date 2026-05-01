# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p1 = head
        p2 = head.next

        while p1 is not None and p2 is not None:
            if p1 == p2:
                return True
            p1 = p1.next
            if p2.next is None:
                return False
            p2 = p2.next.next

        return False 
        