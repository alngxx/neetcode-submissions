class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []     # stack [index, temp] pair
        
        # Give (index, temp) pairs
        for i, t in enumerate(temperatures):
            # While stack is not empty and current temp > top of stack
            while stack and t > stack[-1][1]:
                # Pop the top element
                index, temp = stack.pop()
                res[index]  = i - index    # number of days to warmer
            stack.append([i, t])
        
        return res
            