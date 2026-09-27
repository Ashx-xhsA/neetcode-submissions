# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        cur = dummy = ListNode(0,None)
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                tmp = p1.next
                cur = p1
                p1 = tmp
            else:
                cur.next = p2
                tmp = p2.next
                cur = p2
                p2 = tmp
        if not p1:
            cur.next = p2
        if not p2:
            cur.next = p1
        return dummy.next
            
        