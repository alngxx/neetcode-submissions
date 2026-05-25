class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The height is limited by the shorter line
        Hence, to increase area, only move shorter line inward and update max_area every move
        Since if move taller line inward, width decrease while height still the same
        """
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)     # current area
            max_area = max(max_area, area)               # update max_area every side move

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area