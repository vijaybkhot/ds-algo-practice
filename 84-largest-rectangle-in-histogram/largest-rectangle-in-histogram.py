class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, (height*(i-idx)))
                start = idx
            stack.append((start, h))
        for idx, h in stack:
            max_area = max(max_area, (h*(len(heights)-idx)))
        
        return max_area
