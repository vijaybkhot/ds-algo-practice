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
        stack = []
        max_area = 0
        for idx, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                popped_index = stack.pop()
                height = heights[popped_index]
                # If the stack is empty, it means this height spans from index 0 to idx
                width = idx if not stack else idx - stack[-1] - 1
                area = height * width
                max_area = max(area, max_area)
            stack.append(idx)
        
        # Process any remaining elements in the stack
        while stack:
            popped_index = stack.pop()
            height = heights[popped_index]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = height * width
            max_area = max(area, max_area)
        
        return max_area
                    

                