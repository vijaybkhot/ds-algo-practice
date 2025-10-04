class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            left = height[l]
            right= height[r]

            res = max(res, min(left, right)* (r-l))

            if left < right:
                l += 1
            else:
                r -= 1
        
        return res