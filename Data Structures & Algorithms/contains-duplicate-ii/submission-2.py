class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()      # set store elements visited so far, reduce extra memory
        l = 0 

        for r in range(len(nums)):
            # If window size > k, cut off leftmost element
            if r - l > k:
                window.remove(nums[l])     
                l += 1      # Move window left
            
            # As window slide, check if duplicate found
            if nums[r] in window:
                return True

            # As window slide, store rightmost element in window set
            window.add(nums[r])
        
        return False