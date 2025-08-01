class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            prev_end = end
            while i < len(intervals)-1 and intervals[i+1][0] <= prev_end:
                i += 1
                prev_end =  intervals[i][1] if intervals[i][1] > prev_end else prev_end
            res.append([start, prev_end])
            i += 1
        
        return res