# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class ListContainer:

    def __init__(self, head):
        self.head = head

    def pop_front(self):
        res = self.head
        self.head = self.head.next
        return res

    def has_elements(self):
        return self.head is not None

    def __eq__(self, other):
        return self.head.val == other.head.val

    def __lt__(self, other):
        return self.head.val < other.head.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [ListContainer(list_head) for list_head in lists if list_head is not None]
        if not lists:
            return None

        heapq.heapify(lists)
        least_list = heapq.heappop(lists)
        head = least_list.pop_front()
        curr = head
        if least_list.has_elements():
            heapq.heappush(lists, least_list)
        while lists:
            least_list = heapq.heappop(lists)
            curr.next = least_list.pop_front()
            curr = curr.next
            if least_list.has_elements():
                heapq.heappush(lists, least_list)
        
        return head
        