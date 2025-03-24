class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Sort the meetings array based on the start day
        meetings.sort(key=lambda x: x[0])
        curr_day = 1
        res = 0
    
        for start, end in meetings:
            if start > curr_day:
                res += start - curr_day
            elif start < curr_day and end < curr_day:
                continue
            if end >= curr_day:
                curr_day = end + 1

        if curr_day < days+1:
            res += days+1 - curr_day
        return res
            
        