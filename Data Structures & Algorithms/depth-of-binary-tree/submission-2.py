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
        # maxDepth(3) = 1 + max(maxDepth(9), maxDepth(20))
        # maxDepth(9) = 1 + max(maxDepth(None), maxDepth(None)) = 1 + max(0,0) = 1
        # maxDepth(20) = 1 + max(maxDepth(15), maxDepth(7)) = 1 + max(1,1) = 2
        # => maxDepth(3) = 1 + max(1,2) = 3

        # Depth of current node = 1 (itself) + max depth of its children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))