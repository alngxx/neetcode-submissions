""" DFS with -1 sentinel — O(n), O(h) 
1. Base case: null → return 0 (height is 0, valid)
2. Recurse left and right to get their heights
3. If either child returned -1 (unbalanced below), bubble -1 up immediately
4. If height diff at current node > 1, return -1 (unbalanced here)
5. Otherwise return actual height: 1 + max(left, right)
6. Final answer: root didn't return -1 → whole tree is balanced
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0                    # null node has height = 0, valid
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1                   # unbalanced somewhere below, or here
            return 1 + max(left, right)     # return actual height
        
        # unbalanced somewhere below, or at root
        if dfs(root) == -1:
            return False
        return True