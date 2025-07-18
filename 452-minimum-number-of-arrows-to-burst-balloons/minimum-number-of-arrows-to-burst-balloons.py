class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        prev = float('-inf')
        arrows = 0
        for start, end in points:
            if prev >= start:
                continue
            prev = end
            arrows += 1
        
        return arrows
        