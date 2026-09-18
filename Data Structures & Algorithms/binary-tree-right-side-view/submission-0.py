class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """ BFS: O(n), O(n)
        Append the last element of each level to result list
        """
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            cur_level = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur_level[-1])
        return res