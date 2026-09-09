class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ Sort: O(n²logn), O(1) """
        """ Min-Heap: O(nlogn), O(n)
        1. Convert all stones negative and build a negative max-heap
        2. Pop the two smallest (two heaviest stones)
        3. Push res into heap
        """

        # turn stones into a min-heap (negative max-heap)
        stones = [-s for s in stones]
        heapq.heapify(stones)           

        while len(stones) > 1:
            cur = heapq.heappop(stones) - heapq.heappop(stones)
            if cur != 0:
                heapq.heappush(stones, cur)
        
        return -stones[0] if stones else 0