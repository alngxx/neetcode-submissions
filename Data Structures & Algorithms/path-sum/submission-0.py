# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """ DFS: O(n), O(n) for recursion stack 
        1. dfs(node, cur_sum): return if a valid path exist from this node
        2. If node is None, return False
        3. If node is leaf, return whether cur_sum == target
        4. Otherwise, recursively check left/right path. 
        5. Return True if either child has valid path
        """
        def dfs(node, cur_sum):
            if not node:
                return False

            cur_sum += node.val
            # return only if node is leaf
            if not node.left and not node.right:
                return cur_sum == targetSum
            
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)