# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)

        res = []        
        # While queue is not empty (still have unprocessed children )
        while q:
            cur_level = []     # all nodes of current level
            # Iterate all nodes in current level
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)

                # Enqueue left/right children if exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(cur_level)
        return res