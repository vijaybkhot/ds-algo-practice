class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # Solution using extra space - O(n) time and O(n) space complexity
        # n = len(height)
        # left_max_arr = [0] * n
        # right_max_arr = [0] * n
        # min_of_l_and_r = [0] * n
        # left_max_arr[0], right_max_arr[-1] = 0, 0
        # # Calculate left max for each position
        # for i in range(1, n):
        #     left_max_arr[i] = max(height[i-1], left_max_arr[i-1])
        # # Calculate right max for each position
        # for i in range(n-2, -1, -1):
        #     right_max_arr[i] = max(height[i+1], right_max_arr[i+1])
        # # Caclulate the min of left_max and right_max at each position
        # for i in range(n):
        #     min_of_l_and_r[i] = min(left_max_arr[i], right_max_arr[i])
        # rain_water = 0
        # # Count Rain water trapped at each position by subtracting input from min_of_l_and_r
        # for i in range(n):
        #     curr_water = min_of_l_and_r[i] - height[i]
        #     if curr_water > 0:
        #         rain_water += curr_water
        # return rain_water

        # Solution using constant extra space - O(n) time and O(1) space complexity
        if not height or len(height) == 1:
            return 0

        n = len(height)
        left, right = 0, n-1
        max_l, max_r = height[left], height[right]
        total_rain_trapped = 0
        while left < right:
            if max_l < max_r:
                left += 1
                max_l = max(max_l, height[left])
                curr_rain_trapped = max_l - height[left]
                if curr_rain_trapped > 0:
                    total_rain_trapped += curr_rain_trapped

            
            else:
                right -= 1
                max_r = max(max_r, height[right])
                curr_rain_trapped = max_r - height[right]
                if curr_rain_trapped > 0:
                    total_rain_trapped += curr_rain_trapped
        return total_rain_trapped
            
        
       