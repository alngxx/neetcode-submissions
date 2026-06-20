class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ Max-Heap size k: O(n log k), O(k) 
        1. Push each point's negative squared distance onto a heap, sort by dist
        2. If heap size > k, pop the most negatives (farthest point)
        3. Heap now holds the k closest points, return them
        """
        heap = []
        for point in points:
            dist = - (point[0] ** 2 + point[1] ** 2)      
            heapq.heappush(heap, (dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for dist, point in heap]