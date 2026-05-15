class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res =  []

        # Append larger square to res, so res stores squares in decreasing order
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                res.append(nums[j]**2)
                j -= 1
            else:
                res.append(nums[i]**2)
                i += 1
        
        return res[::-1]