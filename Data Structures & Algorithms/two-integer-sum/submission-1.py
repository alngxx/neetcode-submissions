class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Intuition: Hashmap - which is Dictionary in Python
        - Dictionary stores seen numbers as key & their indices as value
        - seen = {key : value}
        - key = nums[i]; value = i
        '''
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            # If complement of current number (nums[i]) found in seen, return complement's index and current number's index
            if complement in seen:
                return [seen[complement], i]
            
            # If complement not found, store current number's index into dictionary
            seen[nums[i]] = i
        