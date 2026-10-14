# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #the max value when you are sure to include the node
        #max(val_node,val_node+max_val_left,val_node+max_val_right)
        res = float('-inf')
        def max_val_across_node(node):
            nonlocal res
            if not node:return 0
            max_left = max_val_across_node(node.left)
            max_right = max_val_across_node(node.right)
            max_val = max(node.val, 
            node.val + max_left,
            node.val + max_right)

            res = max(max_val,res,node.val + max_left+max_right)
            return max_val
        max_val_across_node(root)
        return res

        