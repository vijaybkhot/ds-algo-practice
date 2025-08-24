class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def smallest(arr):
            next_smallest = [0]*len(arr)
            prev_smallest = [0]*(len(arr))
            stack = []
            for idx, num in enumerate(arr):
                while stack and stack[-1][0] > num:
                    _, i = stack.pop()
                    next_smallest[i] = idx - i
                last_idx = stack[-1][1] if stack else -1
                prev_smallest[idx] = idx - last_idx
            
                stack.append((num, idx))
            for _, idx in stack:
                if next_smallest[idx] == 0:
                    next_smallest[idx] = len(arr) - idx
            return next_smallest, prev_smallest
        
        next_smallest, prev_smallest = smallest(heights)
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, (next_smallest[i]+prev_smallest[i]-1)*heights[i])
        
        return max_area
        


        