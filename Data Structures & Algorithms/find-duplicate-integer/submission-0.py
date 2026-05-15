class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            if freq[num] > 1:
                return num