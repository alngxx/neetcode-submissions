class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ Naive approach: Sorting - O(n•logn)"""
        count = {}          
        for num in nums:
            count[num] = count.get(num, 0) + 1       

        # freq is list store [count, num] pairs
        freq = []       
        for num, cnt in count.items():
            freq.append([cnt, num])
        freq.sort()

        n = len(freq)
        res = []
        # append the num of top k frequent pair
        for i in range(n - 1, n - 1 - k, -1):
            res.append(freq[i][1])
        
        return res