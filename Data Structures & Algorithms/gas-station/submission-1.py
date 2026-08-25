class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """ Greedy: O(n), O(1)
        1. If total gas < total cost, impossible → return -1
        2. Track a running tank: 
        - At each station, tank += gas[i] - cost[i]
        - When it goes negative, reset new start = i+1, new tank = 0
        3. Return start (guaranteed unique)
        """
        if sum(gas) < sum(cost):
            return -1
        
        start = tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        
        # after looping, the last start is the only valid solution
        return start