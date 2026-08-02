class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        # 1st pass: negate index of seen numbers
        for i in range(n):
            # take abs since that number has already negated
            index = abs(nums[i]) - 1

            # mark current number's true index as negated
            if nums[index] > 0:
                nums[index] *= -1
        
        # 2nd pass: every positive number means those are indexes of missing number
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res