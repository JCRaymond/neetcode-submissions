# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = l1.val + l2.val
        carry = value // 10
        value %= 10
        l1 = l1.next
        l2 = l2.next

        res_head = ListNode(value)
        res_curr = res_head
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + carry
            carry = value // 10
            value %= 10
            l1 = l1.next
            l2 = l2.next

            res_curr.next = ListNode(value)
            res_curr = res_curr.next
        
        while l1 is not None:
            value = l1.val + carry
            carry = value // 10
            value %= 10
            l1 = l1.next

            res_curr.next = ListNode(value)
            res_curr = res_curr.next

        while l2 is not None:
            value = l2.val + carry
            carry = value // 10
            value %= 10
            l2 = l2.next

            res_curr.next = ListNode(value)
            res_curr = res_curr.next

        if carry > 0:
            res_curr.next = ListNode(carry)
        
        return res_head

            
