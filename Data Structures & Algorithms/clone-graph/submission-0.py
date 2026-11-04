from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        copyNodes = {1:Node(1)}
        seen = set()
        seen.add(node)
        while q:
            cur = q.popleft()
            curVal = cur.val
            if curVal not in copyNodes:
                copyNodes[curVal] = Node(curVal)

            for n in cur.neighbors:
                if n.val not in copyNodes:
                    copyNodes[n.val]= Node(n.val)
                copyNodes[curVal].neighbors.append(copyNodes[n.val])

                if n not in seen:
                    q.append(n)
                    seen.add(n)
        return copyNodes[1]



        