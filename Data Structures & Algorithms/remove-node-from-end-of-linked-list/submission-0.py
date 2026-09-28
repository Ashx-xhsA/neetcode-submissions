# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if not head.next:
            return None
        s=f=dummy
        for _ in range(n):
            f=f.next
        while f.next:
            s=s.next
            f=f.next
        ## s in the to remove-1
        toRemove = s.next
        newNext = s.next.next
        s.next = newNext

        return dummy.next









        