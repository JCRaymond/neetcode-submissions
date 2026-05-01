# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        curr = head
        while curr is not None:
            next_ = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_

        return new_head
        