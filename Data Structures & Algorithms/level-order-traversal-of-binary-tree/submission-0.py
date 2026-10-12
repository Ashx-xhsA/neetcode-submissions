# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q = deque()
        ans = []
        q.append(root)
        l = len(q)
        while q:
            res = []
            for _ in range(l):
                cur = q.popleft()
                res.append(cur.val)
                left = cur.left
                right = cur.right
                if left:q.append(left)
                if right:q.append(right)
            l = len(q)
            ans.append(res)
        return ans

        
        