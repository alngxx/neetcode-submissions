class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            # if distance > k
            if r - l > k:
                window.remove(nums[l])   # remove current left pointer
                l += 1                   # move left forward to reduce distance
            
            # if nums[r] in the set, it's the duplicate
            if nums[r] in window:
                return True
            
            # keep expanding window as pointer r move forward
            window.add(nums[r])
        
        return False
        