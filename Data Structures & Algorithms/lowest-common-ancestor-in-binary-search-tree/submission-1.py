# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        def isAncestor(node):
            nonlocal lca
            if lca:
                return (1,1)
            
            p_ancestor = q_ancestor = 0
            if not node:
                return (0,0)
            left_p,left_q = isAncestor(node.left)
            right_p,right_q = isAncestor(node.right)
        
            if node.val == p.val or left_p or right_p:
                p_ancestor = 1
            if node.val == q.val or right_q or left_q:
                q_ancestor = 1
            if p_ancestor and q_ancestor and not lca:
                lca = node           
            return (p_ancestor,q_ancestor)
        isAncestor(root)
        return lca
