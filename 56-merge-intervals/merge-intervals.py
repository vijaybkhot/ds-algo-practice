class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
            
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            if curr[0] <= prev[1]:
                res.pop()
                curr = [min(prev[0], curr[0]), max(curr[1], prev[1])]
            res.append(curr)
        
        return res
        