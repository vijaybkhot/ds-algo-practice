class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Solution using extra space
        n = len(height)
        left_max_arr = [0] * n
        right_max_arr = [0] * n
        min_of_l_and_r = [0] * n
        left_max_arr[0], right_max_arr[-1] = 0, 0
        # Calculate left max for each position
        for i in range(1, n):
            left_max_arr[i] = max(height[i-1], left_max_arr[i-1])
        # Calculate right max for each position
        for i in range(n-2, -1, -1):
            right_max_arr[i] = max(height[i+1], right_max_arr[i+1])
        # Caclulate the min of left_max and right_max at each position
        for i in range(n):
            min_of_l_and_r[i] = min(left_max_arr[i], right_max_arr[i])
        rain_water = 0
        # Count Rain water trapped at each position by subtracting input from min_of_l_and_r
        for i in range(n):
            curr_water = min_of_l_and_r[i] - height[i]
            if curr_water > 0:
                rain_water += curr_water
        return rain_water

        
       