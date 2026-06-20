class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # helper function to compare negative distance
        def distance(point: List[int]):
            return -(point[0]**2 + point[1]**2)     
        
        # push all points into min-heap, sort by negative distance
        heap = []
        for point in points:
            heapq.heappush(heap, (distance(point), point))
        # keep only k smallest distance (pop out the most negatives)
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res