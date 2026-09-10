class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # lambda x: x[0] means "given x, return x[0]"
        intervals.sort(key = lambda interval: interval[0])
        res = [intervals[0]]

        for interval in intervals:
            # current greatest end
            last_end = res[-1][1]

            # if overlap interval, merge them by update greatest_end
            if interval[0] <= last_end:
                res[-1][1] = max(last_end, interval[1])
            # else, just append non-overlap interval
            else:
                res.append(interval)

        return res