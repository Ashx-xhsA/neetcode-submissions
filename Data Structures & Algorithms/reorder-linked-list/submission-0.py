# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next
        if len(li) == 1:
            return 
        dummy = ListNode(0,None)
        pair = dummy
        i = 0
        n = len(li)
        while n - i - 1 >= i:
            if n-i-1 == i:
                pair.next = li[i]
                pair = li[i]
                break
            li[i].next = li[n-i-1]
            pair.next = li[i]
            pair = li[n-i-1]
            i += 1
        pair.next = None
    
      

        