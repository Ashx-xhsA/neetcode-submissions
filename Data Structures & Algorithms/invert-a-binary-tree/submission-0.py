# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertChildren(root):
            if not root:
                return None
            newRight = invertChildren(root.left)
            newLeft = invertChildren(root.right)
            root.right = newRight
            root.left = newLeft
            return root
        return invertChildren(root)