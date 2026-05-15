class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ Iteration: O(n x 2ⁿ)
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
        """

        """
        Build all possible subsets by INclude or EXclude a number
        Backtracking - subset.pop() helps us explore both choices:
        - Add the current number -> explore subsets with it 
        - Remove current number -> explore subsets without it
        Whenever reach the end of array, that's when the var subset represent one complete subset
        """
        res = []
        subset = []   # current subset being built

        # Explore all subsets from index i
        def dfs(i):
            # Base case: When reach the end of an array, store current subset into res
            if i == len(nums):
                res.append(subset.copy())
                return     # Return to previous decision
            
            # Decision 1: INclude nums[i]
            subset.append(nums[i])   # Add current number
            dfs(i + 1)   # Recurse to next index

            # Backtrack: remove added number
            subset.pop()      

            # Decision 2: EXclude nums[i]
            dfs(i + 1)   # Skip current index
        
        # Start DFS from index 0
        dfs(0)
        return res



        