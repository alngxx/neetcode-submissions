class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()             # sort array to handle duplicates
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue        # skip duplicates
            
            # for each nums[i], assign two pointers j, k
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1      # move left pointer to find next triplet
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1  # skip duplicate triplets
        
        return res