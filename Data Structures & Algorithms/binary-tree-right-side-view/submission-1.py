# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            lenq = len(q)
            for i in range(lenq):
                cur = q.popleft()
                left = cur.left
                right = cur.right
                if left:q.append(left)
                if right:q.append(right)
                if i == lenq -1:
                    res.append(cur.val)
        return res



        