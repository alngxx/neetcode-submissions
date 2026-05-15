class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # New set stores element as we iterate the list
        seen = set()
        # Iterate the list & add to set
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        