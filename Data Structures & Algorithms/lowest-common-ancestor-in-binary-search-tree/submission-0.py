# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ DFS: O(n), O(h)
        1. dfs(node): return p, q, or LCA if found, else None
        2. If node is None, return None
        3. Recurse left and right
        4. If current node is p or q, return current node
        5. If both left and right returned something, this node is the LCA
        6. Otherwise return whichever side found something (or None)
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # recurse left/right branch to find LCA
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both on different side (both is not None), return this node as LCA
        if left and right:
            return root
        else:
            return left or right