class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """ Max-Heap: 
        Always keep the heap negative to get max element
        """
        # 1. Create a negative min-heap
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        # 2. Record the new k gifts into heap
        for _ in range(k):
            # take out the max gift and revert it positive to calculate sqrt(gift)
            gift = -heapq.heappop(gifts)      # take out the max gift and revert it positive to calculate sqrt(gift)
            heapq.heappush(gifts, -floor(gift ** 0.5))
        
        # 3. Return sum of gifts
        return -sum(gifts)