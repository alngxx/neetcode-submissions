class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """ BFS + Queue: O(n), O(w)
        Similar to normal level-order traversal
        But when comes to even level, append reverse of that level
        """
        if not root:
            return []
        
        res = []
        q = deque()
        q.append([root, 1])
        
        while q:
            cur_level = []
            for _ in range(len(q)):
                node, level = q.popleft()
                cur_level.append(node.val)

                if node.left:
                    q.append([node.left, level + 1])
                if node.right:
                    q.append([node.right, level + 1])
            if level % 2 == 0:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level)
        return res