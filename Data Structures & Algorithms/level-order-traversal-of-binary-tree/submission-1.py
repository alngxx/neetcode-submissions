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
        # process all node
        while q:
            cur_level = []
            # iterate all nodes in current level
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(cur_level)
        return res