"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d= {}
        p = head
        while p:
            new = Node(p.val,None,None)
            d[p] = new
            p = p.next
        p = head
        while p:
            nxt = p.next
            rdm = p.random

            corresponsing = d[p]
            if nxt:
                corresponsing.next = d[nxt]
            if rdm:
                corresponsing.random = d[rdm]

            p = p.next
        return d[head]
        