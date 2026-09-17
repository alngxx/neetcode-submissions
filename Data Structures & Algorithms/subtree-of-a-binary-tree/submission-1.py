class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """ DFS: O(m * n), O(m + n)
        1. Walk through every node of main tree using DFS
        2. At each node, check if subtree is same tree as subRoot
        """
        # edge case
        if not subRoot:
            return True
        if not root:
            return False
        
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val != subRoot.val:
                return False
            
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        
        if sameTree(root, subRoot):
            return True
        
        # dfs to check if node's subtree is same as subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        