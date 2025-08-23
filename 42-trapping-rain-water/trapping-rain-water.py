class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Two pointer approach
        l, r = 0, len(height)-1
        l_max, r_max = 0, 0
        rain = 0

        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                rain += l_max - height[l]
                l += 1 
            else:
                r_max = max(r_max, height[r])
                rain += r_max - height[r]
                r -= 1 
            
        return rain
