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
        q = deque([root])
        res = ''
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                if not cur:
                    res += '#'
                else:
                    res = res +'('+str(cur.val)+')'
                    q.append(cur.left)
                    q.append(cur.right)
                if i == l-1:
                    res += '|'
        print(res)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        s =1
        stk = deque()
        first_val = ''
        while data[s] !=')':
            first_val += data[s]
            s += 1
        root = TreeNode(int(first_val))
        stk.append(root)
        s = s+2
        l = 1
        while stk:
            floor_size = 0
            for _ in range(l):
                cur = stk.popleft()
                left = ''
                right = ''
                if data[s] != '#':
                    if data[s] == '(':
                        s += 1
                    while data[s] != ')':
                        left += data[s]
                        s += 1
                s += 1
                if data[s] != '#':
                    if data[s] == '(':
                        s += 1
                    while data[s] != ')':
                        right += data[s]
                        s += 1
                s += 1
                
                if left:
                    left_node = TreeNode(int(left))
                    cur.left = left_node
                    stk.append(left_node)
                    floor_size += 1
                if right: 
                    right_node = TreeNode(int(right))
                    cur.right = right_node
                    floor_size += 1
                    stk.append(right_node)
                    
                if _ == l -1:
                    s += 1
                    l = floor_size
        return root

                


        
        
