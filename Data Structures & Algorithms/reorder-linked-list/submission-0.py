# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        while fast is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        
        prev_slow.next = None
        second_head = None

        curr = slow
        while curr is not None:
            next_ = curr.next
            curr.next = second_head
            second_head = curr
            curr = next_

        first_head = head

        curr = first_head
        first_head = first_head.next
        while second_head is not None:
            curr.next = second_head
            second_head = second_head.next
            curr = curr.next
            if first_head:
                curr.next = first_head
                first_head = first_head.next
                curr = curr.next
