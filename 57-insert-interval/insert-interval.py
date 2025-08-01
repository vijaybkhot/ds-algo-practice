class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        used = False
        insert = []
        res = []

        # insert newInterval in order
        for start, end in intervals:
            if newStart < start and not used:
                insert.append([newStart, newEnd])
                used = True
            insert.append([start, end])

        if not used:
            insert.append([newStart, newEnd])
        res = [insert[0]]
        # Merge overlapping intervals
        for start, end in insert[1:]:
            prev_start, prev_end = res[-1]
            if start <= prev_end and prev_start <= end:
                res[-1] = [min(start, prev_start), max(end, prev_end)]
            else:
                res.append([start, end])
        
        return res