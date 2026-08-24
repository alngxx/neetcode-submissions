class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ Intuition 
        Instead of trying all possible jumps, we can think about the problem in reverse:
        ask which positions can eventually reach the end
        then move backward to see if earlier positions can reach those positions
        """
        """ Greedy: O(n), O(1)
        1. Set goal = last index (n - 1)
        2. Check backwards from index n - 2: if i + nums[i] >= goal, i can reach goal
        3. Update new goal = i, now check i - 1
        4. If goal = 0, we can jump from start to end
        """
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0