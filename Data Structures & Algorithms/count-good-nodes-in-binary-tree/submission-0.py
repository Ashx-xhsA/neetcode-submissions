# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverseMax(node,prevMax):
            if not node:
                return
            nonlocal count
            if prevMax <= node.val:
                count += 1
            curMax = max(prevMax,node.val)
            traverseMax(node.left,curMax)
            traverseMax(node.right,curMax)
        traverseMax(root,float('-inf'))
        return count


        
        