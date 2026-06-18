class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ Min Heap: Time: O(n•logk), Space: O(n+k)
        Tree where the smallest value is always at the top:
        - When push items in, it auto-sorts.
        - When pop, it always remove the smallest
        """
        count = {}          
        for num in nums:
            count[num] = count.get(num, 0) + 1       

        heap = []   # empty heap
        for num in count:
            heapq.heappush(heap, (count[num], num))  # push all (freq, number) - heap auto sorts by freq
            while len(heap) > k:
                heapq.heappop(heap)                 # pop smallest freq, keep only top k
        
        res = []
        # append top k frequent numbers
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
            
