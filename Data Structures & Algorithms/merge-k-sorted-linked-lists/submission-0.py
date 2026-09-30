# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeLists(lists,0,len(lists)-1)

    def mergeLists(self,lists,l,r):
        if l == r:
            return lists[l]
        if r == l + 1:
            return self.merge2Lists(lists[l],lists[r])
        if l < r:
            mid = l + (r-l) //2
            mergeLeft = self.mergeLists(lists,l,mid)
            mergeRight = self.mergeLists(lists,mid+1,r)
            
            return self.merge2Lists(mergeLeft,mergeRight)

    def merge2Lists(self,li1,li2):
        dummy = ListNode()
        cur = dummy
        while li1 and li2:
            if li1.val <= li2.val:
                cur.next = li1
                li1 = li1.next
                cur = cur.next
            else:
                cur.next = li2
                li2 = li2.next
                cur = cur.next
        cur.next = li1 if li1 else li2
        return dummy.next
        