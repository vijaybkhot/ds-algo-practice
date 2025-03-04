class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # First attempt, partially correct solution.
        # left, right = 0, len(height)-1
        # max_area = min(height[left], height[right]) * (right - left)
        # while left < right:
        #     left += 1
        #     if left == right:
        #         break
        #     curr_max_area = min(height[left], height[right]) * (right - left)
        #     if curr_max_area > max_area:
        #         max_area = curr_max_area
        #     right -= 1
        #     if left == right:
        #         break
        #     curr_max_area = min(height[left], height[right]) * (right - left)
        #     if curr_max_area > max_area:
        #         max_area = curr_max_area

        # return max_area

        # Improved solution - Greedy approach to moving pointer
        left, right = 0, len(height)-1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            curr_max_area = min(height[left], height[right]) * (right - left)
            if curr_max_area > max_area:
                max_area = curr_max_area
        
        return max_area
            



