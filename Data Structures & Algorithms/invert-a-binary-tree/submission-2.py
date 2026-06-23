# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Recursive DFS (pre-order): O(n), O(h) where h = tree height
        1. Base case: if node is None, return None
        2. Swap left and right children at current node
        3. Recurse on left subtree, then right subtree
        4. Return current node
        """
        if not root: 
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)      # DFS on new left child
        self.invertTree(root.right)     # DFS on new right child

        return root