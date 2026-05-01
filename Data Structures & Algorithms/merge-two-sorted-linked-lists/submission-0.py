# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged_head = None
        if list1.val <= list2.val:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next
        
        merged_curr = merged_head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged_curr.next = list1
                list1 = list1.next
            else:
                merged_curr.next = list2
                list2 = list2.next
            merged_curr = merged_curr.next
        if list1 is not None:
            merged_curr.next = list1
        elif list2 is not None:
            merged_curr.next = list2
        return merged_head

