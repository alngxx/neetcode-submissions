class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums        
        self.k = k                      # init self.k since add function can't access k
        heapq.heapify(self.heap)        # make nums a min-heap first

        while len(self.heap) > k:
            heapq.heappop(self.heap)    # always keep the top k elements

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)    # always keep the top k elements
        
        return self.heap[0]             # return largest element