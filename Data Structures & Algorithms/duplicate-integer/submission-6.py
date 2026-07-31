class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Intuition: 
        - Modify list into set
        - If len(set) = len(list): No duplicates -> False
        - Else: Duplicates exist -> True
        '''
        return len(nums) > len(set(nums))
        