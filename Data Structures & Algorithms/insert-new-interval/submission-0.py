class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """ Linear Search: O(n), O(n) 
        Simply split the work into 3 parts, and append to result:
        1. Non-overlap intervals before new: intervals[i][1] < newInterval[0]
        2. Overlap intervals: intervals[i][1] >= newInterval[0] or intervals[i][0] <= newInterval[1]
        3. Non-overlap intervals after new: intervals[i][0] > newInterval[1]
        """
        res = []
        n = len(intervals)
        i = 0               # current inverval in original intervals
        
        # 1. intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. intervals overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        # 3. intervals completely after newInterval, append the rest
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res