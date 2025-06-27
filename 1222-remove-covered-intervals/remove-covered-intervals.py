class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        max_end = intervals[0][1]
        res = 1
        for start, end in intervals[1:]:
            if end <= max_end:
                continue
            else:
                max_end = max(max_end, end)
                res += 1
        return res


        