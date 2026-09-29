# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        p1 = l1
        p2 = l2
        overflow = 0
        while l1 and l2:
            digit = (l1.val + l2.val + overflow)% 10
            overflow =  (l1.val + l2.val + overflow)// 10

            digitNode = ListNode(digit)
            cur.next = digitNode
            cur = digitNode

            l1= l1.next
            l2=l2.next
        if l1:
            remainLi = l1
        else:
            remainLi = l2
        while remainLi:
            digit = (remainLi.val + overflow)%10
            overflow = (remainLi.val + overflow)//10

            digitNode = ListNode(digit)
            cur.next = digitNode
            cur = digitNode

            remainLi = remainLi.next
        if overflow:
            cur.next = ListNode(overflow)
        return dummy.next




        