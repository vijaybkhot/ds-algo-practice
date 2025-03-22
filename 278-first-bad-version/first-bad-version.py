# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        res = right
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                res = mid
                right = mid -1
            else:
                left = mid + 1
        
        return res
        