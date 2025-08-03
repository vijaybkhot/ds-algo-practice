class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removals  = 0

        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev:
                removals += 1
                prev = min(end, prev)
            else:
                prev = end
        
        return removals
            
            
