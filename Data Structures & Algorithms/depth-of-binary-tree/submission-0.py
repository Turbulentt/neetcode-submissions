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

        leftDepth = 1
        rightDepth = 1

        if root.left:
            leftDepth = 1 + self.maxDepth(root.left)
        
        if root.right:
            rightDepth = 1 + self.maxDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth
        else:
            return rightDepth