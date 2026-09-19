class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ DFS in-order: O(n), O(h)
        In-order in BST give nodes in ascending order
        Thus, just maintain prev and compare to current node
        1. prev, res = None, True
        2. Recurse left
        3. If prev and prev.val >= node.val: update res and exit
        4. Else, advance prev to current node, recurse left
        """
        prev, res = None, True

        def dfs(node):
            nonlocal prev, res
            if not node:
                return
            
            dfs(node.left)
            if prev and prev.val >= node.val:
                res = False
                return
            # advance prev -> current node
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res