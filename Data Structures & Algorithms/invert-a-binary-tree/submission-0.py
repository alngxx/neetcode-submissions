# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Iterative DFS """
        # Base case
        if not root: return None
        stack = [root]   # Iterative DFS using a stack
        
        # Pop top node until stack is empty
        while stack:
            node = stack.pop()     # Take the top node out
            # Swap its children
            node.left, node.right = node.right, node.left

            # Push its children to stack and keeps swapping the children's children
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
        

        