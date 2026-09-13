class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """ 0/1 Knapsack: O(n*target), O(target)
        1. target = sum(nums) // 2: we check if sum target is achievable
        2. dp[i] = True if sum i is achievable using nums processed so far
        3. For each num, try to extend every achievable sum i:
        if dp[i - num] == True, then dp[i] = True (adding num reaches i)
        """
        # if total is odd, return False
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        
        dp = [False] * (target + 1)     # dp[i] = if sum i is achievable using numbers so far
        dp[0] = True                    # sum 0 is always achievale

        for num in nums:
            # iterate from target down to num, so each num is used once per pass
            for i in range(target, num - 1, -1):
                if dp[i - num] == True:
                    dp[i] = True
                
        return dp[target]        