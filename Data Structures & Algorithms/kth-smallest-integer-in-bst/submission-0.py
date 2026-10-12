# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # the size of left subtree indicates the rank 
        res = -1
        def traverseRank(node,n):
        # n is the number of node that is known to be smaller than node
        # n comes from sibling left tree and parent node
        # return the number of nodes of both subtrees + 1
            nonlocal res
            if not node:
                return 0
            else:
                left = traverseRank(node.left,n)
                right = traverseRank(node.right,n+left+1)
            rank = n+ left+1
            if rank == k: res = node.val
            return left + right +1
        traverseRank(root,0)
        return res

            


