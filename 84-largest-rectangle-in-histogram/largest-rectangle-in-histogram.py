class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # # Brute force approach:
        # stack = []
        # max_area = 0
        
        # for i in range(len(heights)):
        #     curr_height = heights[i]
        #     # Calculate max area starting from the current graph
        #     curr_area = curr_height
        #     curr_max = curr_height
        #     curr_min = curr_height
        #     j = 1
        #     while stack:
        #         prev_height = stack.pop()
        #         j += 1
        #         curr_max = max(curr_max, prev_height)
        #         curr_min = min(curr_min, prev_height)
        #         area = curr_min * j
        #         curr_area = max(curr_area, area)
            
        #     max_area = max(curr_area, max_area)
        #     stack = heights[:i+1]
        
        # return max_area

        # Optimized monotonic stack approach
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (height * (i - index)))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area