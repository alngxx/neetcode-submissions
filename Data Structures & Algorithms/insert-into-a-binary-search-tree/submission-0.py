# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ Iteration: O(h), O(1)
        1. If not root, return new node
        2. cur = root, iterate indefinitely
        3. If val > cur.val, check if cur.right is leaf: 
        - If so, insert 
        - Otherwise, move cur to cur.right
        4. Else cur <= cur.val, similar
        """
        if not root:
            return TreeNode(val)
        
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left