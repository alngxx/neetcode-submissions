class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Intuition: Hashmap - O(n)
        seen = {nums[i] : i}
        '''
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:
                return [seen[complement], i]
                
            seen[nums[i]] = i
        