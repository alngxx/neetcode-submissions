class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Intuition: Using two pointers - inspired by Binary Search
        # Time: O(n); Space: O(1)
        i = 0
        j = len(numbers) - 1
        while i < j:
            current = numbers[i] + numbers[j]
            # If current sum < target, move left pointer 
            if current < target:
                i += 1
            elif current > target:
                j -= 1
            # If current sum == target, return two positions of pointers
            else:
                return [i+1,j+1]
        # Return [] if no two sum found
        return []
            

        