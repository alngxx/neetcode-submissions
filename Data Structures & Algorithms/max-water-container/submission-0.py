class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The height is limited by the shorter line
        Hence, to increase area, only move shorter line inward and update maxArea every move
        Since if move taller line inward, width decrease while height still the same
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r: 
            area = min(height[l], height[r]) * (r-l)    # current area
            res = max(res, area)                        # update maxArea every move
            # Only move shorter line inward
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res



        