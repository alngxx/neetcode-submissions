class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Intuition: 
        - Modify list into set
        - If len(set) = len(list): No duplicates -> False
        - Else: Duplicates exist -> True
        '''
        set_nums = set(nums)

        if len(set_nums) - len(nums) == 0:
            return False
        else: 
            return True
        