class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Hashmap + Stack: O(m + n), O(n)
        1. Iterate nums2 and keep a stack of numbers waiting for its next greater
        2. If current number > stack's top, num is its next greater
        3. Keep popping and save next greater in hashmap until num is also pushed to stack
        4. Now num waits for its next greater
        """
        next_greater = {}       # dict stores each number's next greater (if exists)
        stack = []              # stack of numbers waiting for its next greater

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            next_great = next_greater.get(num, -1)
            res.append(next_great)
        return res