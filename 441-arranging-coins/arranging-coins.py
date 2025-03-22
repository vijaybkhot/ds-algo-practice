class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        def isValidRow(row, coins):
            return (row * (row + 1)) // 2 > coins
        
        if n == 1:
            return 1
        
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isValidRow(mid, n):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return right
        