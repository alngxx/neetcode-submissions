class Solution:
    def countBits(self, n: int) -> List[int]:
        # Function to count number of 1's (Problem 191 LeetCode)
        def count1(n):
            total = 0
            for i in range(32):
                if (n >> i) & 1:
                    total += 1
            return total
        
        ans = []
        for i in range(n+1):
            ans.append(count1(i))

        return ans
        


        