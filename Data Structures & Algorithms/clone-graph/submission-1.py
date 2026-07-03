"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone Graph (BFS): O(V + E), O(V)
        1. Clone the start node, store mapping old -> new in visited dict
        2. BFS through original graph using queue
        3. For each node popped, go through its neighbors
        4. If neighbor not cloned yet, clone it and add to queue
        5. Connect current clone's neighbors list to the neighbor's clone
        """
        if not node:
            return None

        # map store original node -> cloned node
        clone_map = {}
        # create new Node object with same value as node, but neighbors defaults to []
        clone_map[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # clone_map[cur] = clone of current node popped from queue
                # clone_map[neighbor] = clone of one of cur's original neighbors
                clone_map[cur].neighbors.append(clone_map[neighbor])
        
        return clone_map[node]


        