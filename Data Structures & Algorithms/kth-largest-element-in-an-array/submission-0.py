class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ Min-Heap: O(nlogk), O(k) """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            # always keep the top k elements in min-heap
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]      # return smallest in heap