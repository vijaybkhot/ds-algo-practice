class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        arrows = []

        for start, end in points:
            if arrows and arrows[-1] >= start:
                continue
            arrows.append(end)
        
        return len(arrows)
        