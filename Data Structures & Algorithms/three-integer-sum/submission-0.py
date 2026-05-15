class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   # Sort array to easily handle duplicates
        res = []

        # For every element nums[i], assign two pointers i & j
        for i in range(len(nums) - 1):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1            # left pointer
            k = len(nums) - 1    # right pointer

            # Check until left = right pointer
            while j < k: 
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1    # move left pointer to find next triplet
                    while j < k and nums[j] == nums[j-1]:
                        j += 1    # skip duplicate triplet
        
        return res
             


        




        