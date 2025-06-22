class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # # First attempt:
        # if not intervals:
        #     return [newInterval]
        # temp, res = [], []
        # new_start, new_end = newInterval
        # hasAppended = False
        # curr_start, curr_end = intervals[0] if intervals[0][0] < newInterval[0] else newInterval
        # for start, end in intervals:
        #     if start < new_start or hasAppended:
        #         temp.append([start, end])
        #     else:
        #         temp.append([new_start, new_end])
        #         temp.append([start, end])
        #         hasAppended = True
        # if not hasAppended:
        #     temp.append(newInterval)

        # res.append(temp[0])
        # # merge overlapping intervals
        # for i in range(1, len(temp)):
        #     prev = res[-1]
        #     curr = temp[i]
        #     if prev[1] >= curr[0]:
        #         res.pop()
        #         res.append([min(prev[0], curr[0]), max(prev[1], curr[1])])
        #     else:
        #         res.append([curr[0], curr[1]])
        
        # return res
            

        # More readable solution O(n) time and O(1) space. O(n) for output list
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res