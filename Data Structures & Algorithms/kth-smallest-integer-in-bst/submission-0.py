# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ In-order Traversal: O(n), O(h)
        1. BST: left < root < right
        2. Thus, in-order traversal give nodes in ascending order
        3. So we return k-th node while traverse
        4. Init res, count (global variable)
        5. When count == k, return res
        """
        res = count = 0

        def dfs(node):
            nonlocal res, count

            # stop when found res or null node
            if not node or res != 0:
                return

            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res