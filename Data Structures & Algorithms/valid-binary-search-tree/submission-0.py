# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isBST =True
        def traverseFindBoundary(node):
            nonlocal isBST
            if node.left:
                lleft,lright =traverseFindBoundary(node.left)
            else:
                lleft = float('inf')
                lright = float('-inf')
            if node.right:
                rleft,rright = traverseFindBoundary(node.right)
            else:
                rleft = float('inf')
                rright = float('-inf')
            if lright >= node.val or rleft <= node.val:
                isBST = False
            return (min(lleft,node.val),max(rright,node.val))
        traverseFindBoundary(root)
        return isBST
        