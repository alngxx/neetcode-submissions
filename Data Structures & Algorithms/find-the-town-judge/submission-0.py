""" Indegree & Outdegree: O(V + E), O(V) where V = n, E = len(trust)
Indegree = # edges coming INTO a node (how many other nodes point to it)
Outdegree = # edges going OUT of a node (how many other nodes it points to)
E.g. if a → b means "a trusts b":
- This edge adds 1 to a's outdegree 
- This edge adds 1 to b's indegree 
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        1. Judge is trusted by everyone else, trusts nobody
        2. So judge has indegree = n - 1, outdegree = 0
        3. For each [a, b] pair, increment outgoing[a] and incoming[b]
        4. Find the person i where outgoing[i] == 0 and incoming[i] == n - 1
        5. If no such person, return -1
        """
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for i in range(1, n + 1):
            if outdegree[i] == 0 and indegree[i] == n - 1:
                return i
        
        return -1

