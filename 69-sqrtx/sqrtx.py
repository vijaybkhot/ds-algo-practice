class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if int(mid * mid) == x:
                return mid
            elif int(mid * mid) < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
        