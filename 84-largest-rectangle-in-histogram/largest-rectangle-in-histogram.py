class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller = [n] * n
        prev_smaller = [-1] * n

        # find prev smaller (left)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        # find next smaller (right)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        # compute max area
        max_area = 0
        for i in range(n):
            width = next_smaller[i] - prev_smaller[i] - 1
            max_area = max(max_area, width * heights[i])

        return max_area
