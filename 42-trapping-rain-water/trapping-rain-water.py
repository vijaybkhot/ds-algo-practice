class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0]*n
        r_max = [0]*n
        for i in range(n):
            l_max[i] = max(l_max[i-1] if i-1 >= 0 else 0, height[i])
        
        for i in range(n-1, -1, -1):
            r_max[i] = max(r_max[i+1] if i+1 < n else 0, height[i])
        
        rain_water = 0

        for i in range(1, n-1):
            left_max = l_max[i-1]
            right_max = r_max[i+1]
            curr_height = height[i]
            if left_max > curr_height and curr_height < right_max:
                rain_water += min(left_max, right_max) - curr_height
                
        
        return rain_water

            

            
        