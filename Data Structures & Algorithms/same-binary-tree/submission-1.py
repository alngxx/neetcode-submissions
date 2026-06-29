"""
1. If both nodes are None → same, return True
2. If one is null and other isn't → different, return False
3. If values differ → return False
4. Otherwise recurse: both left AND both right subtrees must match
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)