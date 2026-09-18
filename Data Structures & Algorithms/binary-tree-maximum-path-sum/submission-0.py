# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        # dfs(node) = max sum you can get if going down from me
        def dfs(node):
            if not node:
                return 0

            # ignore negative path
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # update max sum through this node
            nonlocal res
            res = max(res, left + node.val + right)

            # return max sum from a branch if going down from this node
            # dfs(20) = 20 + max(15, 7) = 35
            return node.val + max(left, right)
        
        dfs(root)
        return res 