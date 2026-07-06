class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Variation of 3Sum: Two loops and two pointers inside second loop - O(n³)
        """
        n = len(nums)
        nums.sort()
        res = []

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue        # skip duplicates
            
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue    # skip duplicates

                c = b + 1
                d = n - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target: 
                        d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        # move both pointers to find next quadruplet
                        c += 1
                        d -= 1
                        # skip duplicate quadruplets
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        return res



