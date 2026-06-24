class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:      
        """ Min-Heap: O(k logn), O(n)
        1. Build min-heap of (num, index) pairs
        2. For each of k operation: pop x, multiply it, and push back to heap
        Note: (num, index) handles the "multi occurences of min value" case
        """
        # min-heap stores (num, index) pair
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        # pop x, modify nums in-place, and push new x back to heap
        for _ in range(k):
            (x, i) = heapq.heappop(heap)
            nums[i] = x * multiplier
            heapq.heappush(heap, (nums[i], i))
        
        return nums