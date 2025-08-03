class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        prev = float('-inf')
        arrows = 0
        res = 0

        for start, end in points:
            if prev >= start:
                continue
            arrows += 1
            prev = end
        
        return arrows
