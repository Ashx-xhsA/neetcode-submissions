# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        #build root
        #find left and right recursively
        d={}
    
        for idx,val in enumerate(inorder):
            d[val]= idx
        def buildAsRoot(pre_order_pos,inorder_start_pos,tree_size):
            nonlocal d
            if tree_size < 1:
                return None
            root_val = preorder[pre_order_pos]
            root = TreeNode(root_val)
            #define the range of left subtree
            #define the range of right subtree
            pos_in_inorder = d[root_val]
            left_tree_size = pos_in_inorder - inorder_start_pos
            right_tree_size = tree_size - left_tree_size -1

            left_tree_pre_start = pre_order_pos+1
            right_tree_pre_start = left_tree_pre_start + left_tree_size


            #connect left/right subtrees
            root.left = buildAsRoot(left_tree_pre_start,inorder_start_pos,left_tree_size)
            root.right = buildAsRoot(right_tree_pre_start,pos_in_inorder+1,right_tree_size)

            return root
        
        return buildAsRoot(0,0,len(inorder))