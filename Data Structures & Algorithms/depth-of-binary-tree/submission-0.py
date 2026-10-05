# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mx = depth = 0
        def traverse(root,depth):
            nonlocal mx
            if not root:
                mx = max(mx,depth)
                return 
            depth += 1
            traverse(root.left,depth)
            traverse(root.right,depth)
        traverse(root,depth)

        return mx
        

            



        