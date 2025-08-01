class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        res = []
        while first < len(firstList) and second < len(secondList):
            f_start, f_end = firstList[first]
            s_start, s_end = secondList[second]

            if f_start <= s_end and s_start <= f_end:
                start = max(f_start, s_start)
                end = min(f_end, s_end)
                res.append([start, end])
            
            if f_end <= s_end:
                first += 1
            else:
                second += 1
        
        return res
        