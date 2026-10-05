# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseHead(start,l):
            dummy = ListNode(-1)
            dummy.next = start
            prev = dummy
            cur = start
            for i in range(l):
                tmp = cur.next
                cur.next = prev

                prev = cur
                cur = tmp
            return prev

        subhead = []
        s = f = head
        reachEnd = False
        tail = None
        while f and not reachEnd:
            for i in range(k-1):
                f = f.next
                if not f:
                    reachEnd= True
                    tail = s
                    break
            if not reachEnd:
                subhead.append(s)
                s = f.next
                f = f.next
        for i in range(len(subhead)):
            subhead[i] = reverseHead(subhead[i],k)



        
        # merge 
        dummy = ListNode()
        cur = dummy
        for each in subhead:
            print(each.val)
            cur.next = each
            for i in range(k):
                cur = cur.next
        cur.next = tail
        return dummy.next



        