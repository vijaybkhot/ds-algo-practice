class Solution:
    def mySqrt(self, x: int) -> int:

        res = 0
        for i in range(1, x+1):
            temp = i
            temp_power = temp*temp
            if temp_power > x:
                return res
            res = temp
        
        return res