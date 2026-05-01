# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = head
        second = None
        at_tail = False

        for _ in range(k):
            second = front
            if front is not None:
                front = front.next
            else:
                at_tail = True
        
        if at_tail:
            return head

        back = head
        new_head = second
        
        while not at_tail:
            curr = back
            flip_head = None
            old_front = front
            for _ in range(k):
                if front is not None:
                    second = front
                    front = front.next
                else:
                    at_tail = True
                next_back = back.next
                back.next = flip_head
                flip_head = back
                back = next_back
            if not at_tail:
                curr.next = second
            else:
                curr.next = old_front
            back = old_front

        return new_head