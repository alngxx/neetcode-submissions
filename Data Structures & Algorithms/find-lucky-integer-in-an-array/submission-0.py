class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = {}

        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        res = -1
        for num in frequency:
            if num == frequency[num]:
                res = max(res, num)
                
        return res