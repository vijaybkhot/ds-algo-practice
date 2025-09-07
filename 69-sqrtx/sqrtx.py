class Solution:
    def mySqrt(self, x: int) -> int:

        # res = 0
        # for i in range(1, x+1):
        #     temp = i
        #     temp_power = temp*temp
        #     if temp_power > x:
        #         return res
        #     res = temp
        
        # return res
        left, right = 0, x
        res = 0
        while left <= right:
            mid = (left+right)//2
            if mid*mid > x:
                right = mid - 1
            else:
                res = mid
                left = mid+1
        
        return res