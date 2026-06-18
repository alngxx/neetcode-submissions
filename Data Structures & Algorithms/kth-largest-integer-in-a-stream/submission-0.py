class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k                          # init self.k since add method can't access k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:       # keep only the top k elements
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        # keep only the top k elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]             # return largest element of heap

