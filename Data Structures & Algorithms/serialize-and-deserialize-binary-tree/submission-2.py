# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = []
        q = deque([root])
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if not cur:
                    res.append('#')
                    continue
                res.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
        return '|'.join(res)
    

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = data.split('|')
        root = TreeNode(int(data[0]))
        stk = deque([root])
        index = 1
        while stk:
            sz = len(stk)
            for _ in range(sz):
                cur = stk.popleft()
                if data[index] != '#':
                    left = TreeNode(int(data[index]))
                    cur.left = left
                    stk.append(left)
                index += 1
                if data[index] != '#':
                    right = TreeNode(int(data[index]))
                    cur.right = right
                    stk.append(right)
                index +=1

        return root

                


        
        
