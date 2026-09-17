# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """ DFS: O(n), O(h) 
        1. dfs(node): return max depth at this node
        2. If node is None, return 0
        3. Get left and right depth from this node: dfs(node.left), dfs(node.right)
        4. Update res: longest path through this node is just left depth + right depth
        5. Update max depth at this node
        """
        res = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal res    # access global variable
            left = dfs(node.left)
            right = dfs(node.right)

            # longest path through this node = left depth + right depth
            # update res
            res = max(res, left + right)

            # return max depth at this node
            return 1 + max(left, right)
        dfs(root)
        return res