# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        while tail.next:
            newhead = tail.next
            tmp = newhead.next

            newhead.next = head
            tail.next = tmp

            head = newhead
        return head
            

        


        